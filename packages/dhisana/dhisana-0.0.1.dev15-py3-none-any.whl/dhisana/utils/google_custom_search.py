import asyncio
import json
import logging
import os
import re
from typing import List, Optional
from urllib.parse import urlparse
import aiohttp
import urllib
from dhisana.utils.assistant_tool_tag import assistant_tool
from dhisana.utils.cache_output_tools import retrieve_output, cache_output
import backoff
from bs4 import BeautifulSoup

from dhisana.utils.web_download_parse_tools import get_html_content_from_url
from dhisana.utils.serpapi_search_tools import search_google



@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=60,
)
async def search_google_custom(
    query: str,
    number_of_results: int = 10
):
    """
    Search Google using the Google Custom Search JSON API and return the results as an array of serialized JSON strings.
    
    Parameters:
    - **query** (*str*): The search query.
    - **number_of_results** (*int*): The number of results to return.
    """

    API_KEY = os.environ.get('GOOGLE_SEARCH_KEY')
    CX = os.environ.get('GOOGLE_SEARCH_CX')  # Custom Search Engine ID
    if not API_KEY or not CX:
        return {'error': "Google Custom Search API key or CX not found in environment variables"}

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "num": number_of_results
    }

    try:
        cached_response = retrieve_output("search_google_custom", query)
        if cached_response is not None:
            return cached_response
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    result = await response.json()
                    serialized_results = []
                    
                    # Check for spelling corrections in the response
                    if "spelling" in result and "correctedQuery" in result["spelling"]:
                        corrected_query = result["spelling"]["correctedQuery"]
                        logging.warning(f"Spelling suggestion detected: {corrected_query}. Retrying with original query.")

                        # Re-run query using original terms
                        params["q"] = query  # Explicitly force the original query
                        params["spell"] = query
                        async with session.get(url, params=params) as retry_response:
                            if retry_response.status == 200:
                                retry_result = await retry_response.json()
                                serialized_results = [json.dumps(item) for item in retry_result.get('items', [])]
                    else:
                        serialized_results = [json.dumps(item) for item in result.get('items', [])]
                    cached_response = cache_output("search_google_custom", query, serialized_results)
                    await asyncio.sleep(1)  # Wait for 3 seconds before sending the response
                    return serialized_results
                elif response.status == 429:
                    logging.warning("search_google_custom Rate limit hit")
                    raise aiohttp.ClientResponseError(
                        request_info=response.request_info,
                        history=response.history,
                        status=response.status,
                        message="Rate limit exceeded",
                        headers=response.headers
                    )
                else:
                    result = await response.json()
                    logging.warning(f"search_google_custom Failed to run assistant: {result}")
                    return {'error': result}                       
    except aiohttp.ClientResponseError as e:
        raise  # Allow backoff to handle this exception
    except Exception as e:
        return {'error': str(e)}

@assistant_tool
async def search_google_places(
    query: str,
    location_bias: dict = None,
    number_of_results: int = 3
):
    """
    Search Google Places API (New) and return the results as an array of serialized JSON strings.

    Parameters:
    - **query** (*str*): The search query.
    - **location_bias** (*dict*): Optional. A dictionary with 'latitude', 'longitude', and 'radius' (in meters) to bias the search.
    - **number_of_results** (*int*): The number of results to return.
    """
    GOOGLE_SEARCH_KEY = os.environ.get('GOOGLE_SEARCH_KEY')
    if not GOOGLE_SEARCH_KEY:
        return {'error': "Google Places API key not found in environment variables"}

    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': GOOGLE_SEARCH_KEY,
        'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.location,places.websiteUri,places.rating,places.reviews'
    }

    request_body = {
        "textQuery": query
    }

    if location_bias:
        request_body["locationBias"] = {
            "circle": {
                "center": {
                    "latitude": location_bias.get("latitude"),
                    "longitude": location_bias.get("longitude")
                },
                "radius": location_bias.get("radius", 5000)  # Default to 5 km if radius not provided
            }
        }

    # Create a cache key that includes query, number_of_results, and location_bias
    location_bias_str = json.dumps(location_bias, sort_keys=True) if location_bias else "None"
    cache_key = f"{query}:{number_of_results}:{location_bias_str}"
    cached_response = retrieve_output("search_google_places", cache_key)
    if cached_response is not None:
        return cached_response

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=request_body) as response:
                result = await response.json()
                if response.status != 200:
                    return {'error': result.get('error', {}).get('message', 'Unknown error')}

                # Extract the required number of results
                places = result.get('places', [])[:number_of_results]

                # Serialize each place result to JSON string
                serialized_results = [json.dumps(place) for place in places]

                # Cache the response
                cache_output("search_google_places", cache_key, serialized_results)

                return serialized_results
    except Exception as e:
        return {'error': str(e)}


@assistant_tool
async def get_company_domain_from_google_search(
    company_name: str,
    location: str = None
) -> str:
    """
    Tries to find the company domain from the company name using Google search.

    Args:
        company_name (str): The name of the company to search for.

    Returns:
        str: The domain of the company's official website if found, otherwise an empty string.
    """
    company_name_no_spaces = company_name.replace(" ", "")
    
    if not company_name_no_spaces or company_name.lower() in ["none", "freelance"]:
        return ""
    
    # Search for the company name on Google with the query "official website"
    exclude_company_names = ["linkedin", "wikipedia", "facebook", "instagram", "twitter", "youtube", "netflix", "zoominfo", "reditt"]
    exclusions = ' '.join([f"-site:*.{site}.com" for site in exclude_company_names])
    exclusions = ''
    query = f"\"{company_name}\" official website {exclusions}"
    if location:
        query = f"\"{company_name}\" official website, {location}  {exclusions}"
    result = await search_google_custom(query, 1)
    
    # Retry search with relaxed contraint if list is empty
    if not isinstance(result, list) or len(result) == 0:
        query = f"{company_name} official website {exclusions}"
        result = await search_google_custom(query, 1)
        
    if not isinstance(result, list) or len(result) == 0:
        return ''
   
    exclude_compan_names = ["linkedin", "wikipedia", "facebook", "instagram", "twitter", "youtube", "netflix"]
    if any(exclude_compan_name in company_name.lower() for exclude_compan_name in exclude_compan_names):
        return ""
    
    try:
        # Parse the JSON string result
        result_json = json.loads(result[0])
    except (json.JSONDecodeError, IndexError):
        return ''
    
    # Get the link from the first result
    link = result_json.get('link', '')

    # If the link is empty, return an empty string
    if not link:
        return ''

    # Parse the URL to get the domain part
    parsed_url = urlparse(link)
    domain = parsed_url.netloc

    # Remove 'www.' if it's present at the start of the domain
    if domain.startswith('www.'):
        domain = domain[4:]

    # List of domains to exclude
    excluded_domains = ["linkedin.com", 
                        "wikipedia.org", "usa.gov", 
                        "facebook.com", "instagram.com", 
                        "twitter.com", 
                        "x.com",
                        "google.com",
                        "youtube.com",
                        "netflix.com",
                        "freelance.com", "zoominfo.com", "reditt.com"]
    
    # Convert both domain and excluded domains to lowercase for case-insensitive comparison
    domain_lower = domain.lower()
    excluded_domains_lower = [d.lower() for d in excluded_domains]
    
    # Check if the domain or any of its subdomains are in the excluded list
    if any(domain_lower == d or domain_lower.endswith(f".{d}") for d in excluded_domains_lower):
        return ""

    # Return the domain
    return domain

@assistant_tool
async def check_for_signal_from_google_search(
    company_name: str,
) -> str:
    """
    Tries to find the company domain from the company name using Google search.

    Args:
        company_name (str): The name of the company to search for.

    Returns:
        str: The domain of the company's official website if found, otherwise an empty string.
    """
    # Search for the company name on Google with the query "official website"
    result = await search_google_custom(f"{company_name} official website", 1)
    
    # Check if the result is empty or not a list
    if not isinstance(result, list) or len(result) == 0:
        return ''

    try:
        # Parse the JSON string result
        result_json = json.loads(result[0])
    except (json.JSONDecodeError, IndexError):
        return ''
    
    # Get the link from the first result
    link = result_json.get('link', '')

    # If the link is empty, return an empty string
    if not link:
        return ''

    # Parse the URL to get the domain part
    parsed_url = urlparse(link)
    domain = parsed_url.netloc

    # Remove 'www.' if it's present at the start of the domain
    if domain.startswith('www.'):
        domain = domain[4:]

    # Return the domain
    return domain

@assistant_tool
async def get_signal_strength(
    domain_to_search: str,
    keywords: List[str],
    in_title: List[str] = [],
    not_in_title: List[str] = [],
    negative_keywords: List[str] = []
) -> int:
    """
    Find how strong a match for the keywords in search is.

    Args:
        domain_to_search (str): The domain to search inside.
        keywords (List[str]): The keywords to search for.
        in_title (List[str]): Keywords that must appear in the title.
        not_in_title (List[str]): Keywords that must not appear in the title.
        negative_keywords (List[str]): Keywords to exclude from results.

    Returns:
        int: A strength score on a scale of 0 to 5.
    """
    query = ""
    if domain_to_search:
        query = f"site:{domain_to_search} "
    
    for keyword in keywords:
        query += f"\"{keyword}\" "
    
    for keyword in in_title:
        query += f'intitle:"{keyword}" '
    
    for keyword in not_in_title:
        query += f'-intitle:"{keyword}" '
    
    for keyword in negative_keywords:
        query += f'-"{keyword}" '
            
    if not query.strip():
        return 0
    
    # Search for the keywords on Google with the query
    results = await search_google_custom(query.strip(), 5)
    
    # Check if the result is empty or not a list
    if not isinstance(results, list) or len(results) == 0:
        return 0

    score = 0
    try:
        for result in results:
            result_json = json.loads(result)
            # If search result contains all keywords, increment the score
            if all(keyword.lower() in result_json.get('snippet', '').lower() for keyword in keywords):
                print("Found a match: ", result_json.get('snippet', ''))
                score += 1
            if score == 5:
                break
    except (json.JSONDecodeError, KeyError):
        return 0    

    return score

def extract_user_linkedin_page(url: str) -> str:
    """
    Extracts and returns the user page part of a LinkedIn URL.
    Ensures the domain is www.linkedin.com and removes any suffix path or query parameters.
    """
    # Normalize the domain to www.linkedin.com
    normalized_url = re.sub(r"(https?://)?([\w\-]+\.)?linkedin\.com", "https://www.linkedin.com", url)
    
    # Match and extract the company page segment
    match = re.match(r"https://www.linkedin.com/in/([\w\-]+)", normalized_url)
    if match:
        # Construct the cleaned URL
        page = f"https://www.linkedin.com/in/{match.group(1)}"
        return page
    
    # If no valid company page is found, return an empty string or appropriate error message
    return ""

@assistant_tool
async def find_user_linkedin_url_google(
    user_name: str,
    user_title: str,
    user_location: str,
    user_company: str,
) -> str:
    """
    Find the LinkedIn URL for a user based on their name, title, location, and company.

    Args:
        user_name (str): The name of the user.
        user_title (str): The title of the user.
        user_location (str): The location of the user.
        user_company (str): The company of the user.

    Returns:
        str: The LinkedIn URL if found, otherwise an empty string.
    """
    queries = [
        f'site:linkedin.com/in "{user_name}" "{user_location}" "{user_title}" "{user_company}" intitle:"{user_name}"',
        f'site:linkedin.com/in "{user_name}" "{user_location}" "{user_company}" intitle:"{user_name}"',
        f'site:linkedin.com/in "{user_name}", {user_location} intitle:"{user_name}"',
        f'site:linkedin.com/in "{user_name}" intitle:"{user_name}"'
    ]

    for query in queries:
        if not query.strip():
            continue
        
        # Search for the keywords on Google with the query
        results = await search_google(query.strip(), 1)
        
        # Check if the result is empty or not a list
        if not isinstance(results, list) or len(results) == 0:
            continue

        try:
            # Parse the JSON string result
            result_json = json.loads(results[0])
        except (json.JSONDecodeError, IndexError):
            continue
        
        # Get the link from the first result
        link = result_json.get('link', '')

        # If the link is empty, continue to the next query
        if not link:
            continue

        # Parse the URL to get the domain part
        parsed_url = urlparse(link)
        
        # Check if the URL is in the linkedin.com/in format of a people profile
        if 'linkedin.com/in' in parsed_url.netloc + parsed_url.path:
            link = extract_user_linkedin_page(link)
            return link

    # Return an empty string if no valid link is found
    return ''

@assistant_tool
async def find_user_linkedin_url_by_title_google(
    user_title: str,
    user_location: str,
    user_company: str,
) -> str:
    """
    Find the LinkedIn URL for a user based on their name, title, location, and company.

    Args:
        user_title (str): The title of the user.
        user_location (str): The location of the user.
        user_company (str): The company of the user.

    Returns:
        str: The LinkedIn URL if found, otherwise an empty string.
    """
    queries = [
        f'site:linkedin.com/in "{user_company}" "{user_title}" "{user_location}"  intitle:"{user_company}"',
        f'site:linkedin.com/in  "{user_company}" {user_title} {user_location}',
    ]

    for query in queries:
        if not query.strip():
            continue
        
        # Search for the keywords on Google with the query
        results = await search_google(query.strip(), 1)
        
        # Check if the result is empty or not a list
        if not isinstance(results, list) or len(results) == 0:
            continue

        try:
            # Parse the JSON string result
            result_json = json.loads(results[0])
        except (json.JSONDecodeError, IndexError):
            continue
        
        # Get the link from the first result
        link = result_json.get('link', '')

        # If the link is empty, continue to the next query
        if not link:
            continue

        # Parse the URL to get the domain part
        parsed_url = urlparse(link)
        
        # Check if the URL is in the linkedin.com/in format of a people profile
        if 'linkedin.com/in' in parsed_url.netloc + parsed_url.path:
            link = extract_user_linkedin_page(link)
            return link

    # Return an empty string if no valid link is found
    return ''

def extract_company_page(url: str) -> str:
    """
    Extracts and returns the company page part of a LinkedIn URL.
    Ensures the domain is www.linkedin.com and removes any suffix path or query parameters.
    """
    # Normalize the domain to www.linkedin.com
    normalized_url = re.sub(r"(https?://)?([\w\-]+\.)?linkedin\.com", "https://www.linkedin.com", url)
    
    # Match and extract the company page segment
    match = re.match(r"https://www.linkedin.com/company/([\w\-]+)", normalized_url)
    if match:
        # Construct the cleaned URL
        company_page = f"https://www.linkedin.com/company/{match.group(1)}"
        return company_page
    
    # If no valid company page is found, return an empty string or appropriate error message
    return ""


@assistant_tool
async def find_company_linkedin_url_with_google_search(
    company_name: str,
    company_location: Optional[str] = None,
) -> str:
    """
    Find the LinkedIn URL for a company based on its name and optional location using Google search.

    Args:
        company_name (str): The name of the company.
        company_location (str, optional): The location of the company.

    Returns:
        str: The LinkedIn URL if found, otherwise an empty string.
    """
    if company_location:
        queries = [
            f'site:linkedin.com/company "{company_name}" {company_location}',
            f'site:linkedin.com/company "{company_name}"',
            f'site:linkedin.com/company {company_name} {company_location}',
        ]
    else:
        queries = [
                   f'site:linkedin.com/company "{company_name}"', 
                   f'site:linkedin.com/company {company_name}'
                 ]

    for query in queries:
        if not query.strip():
            continue

        # Search for the company on Google with the query
        results = await search_google(query.strip(), 1)

        # Check if the result is empty or not a list
        if not isinstance(results, list) or len(results) == 0:
            continue

        try:
            # Parse the JSON string result
            result_json = json.loads(results[0])
        except (json.JSONDecodeError, IndexError):
            continue

        # Get the link from the first result
        link = result_json.get('link', '')

        # If the link is empty, continue to the next query
        if not link:
            continue

        # Parse the URL to get the domain part
        parsed_url = urlparse(link)

        # Check if the URL is in the linkedin.com/company format
        if 'linkedin.com/company' in parsed_url.netloc + parsed_url.path:
            link = extract_company_page(link)
            return link

    # Return an empty string if no valid link is found
    return ''


async def get_external_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    soup = BeautifulSoup(content, "html.parser")
                    external_links = []
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        if href.startswith('http') and not href.startswith(url):
                            external_links.append(href)
                    return external_links
                else:
                    print(f"Error: HTTP {response.status}")
                    return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

@assistant_tool
async def get_company_website_from_linkedin_url(linkedin_url):
    if not linkedin_url:
        return ""
    links = await get_external_links(linkedin_url)
    for link in links:
        if 'trk=about_website' in link:
            parsed_link = urllib.parse.urlparse(link)
            query_params = urllib.parse.parse_qs(parsed_link.query)
            if 'url' in query_params:
                encoded_url = query_params['url'][0]
                company_website = urllib.parse.unquote(encoded_url)
                return company_website
    return ""


@assistant_tool
async def find_job_postings_google_search(
    company_name: str,
    keywords_check: List[str],
    company_linkedin_url: Optional[str] = None  
) -> List[str]:
    """
    Find job postings on LinkedIn for a given company using Google Custom Search.

    Args:
        company_name (str): The name of the company.
        company_linkedin_url (Optional[str]): The LinkedIn URL of the company.
        keywords_check (List[str]): A list of keywords to include in the search.

    Returns:
        List[str]: A list of job posting links.
    """
    keywords_list = [kw.strip().lower() for kw in keywords_check]
    
    # Combine all keywords into a single query
    keywords_str = ' '.join(f'"{kw}"' for kw in keywords_list)
    query = f'site:linkedin.com/jobs "{company_name}" {keywords_str}'
    queries = [query]
    
    job_posting_links = []

    for query in queries:
        if not query.strip():
            continue

        # Search for job postings on Google with the query
        results = await search_google_custom(query.strip(), 1)

        if not isinstance(results, list) or len(results) == 0:
            continue

        # For each result, fetch the page and process
        for result_item in results:
            try:
                result_json = json.loads(result_item)
            except json.JSONDecodeError:
                continue

            link = result_json.get('link', '')

            if not link:
                continue

            # Fetch the page content
            try:
                page_content = await get_html_content_from_url(link)
                # Parse the page content with BeautifulSoup
                soup = BeautifulSoup(page_content, 'html.parser')
            except Exception:
                continue

            # Extract all hrefs from the page
            page_links = [a.get('href') for a in soup.find_all('a', href=True)]

            # Check if company_linkedin_url and 'public_jobs_topcard-org-name' are in the page links
            company_match = False
            if company_linkedin_url:
                for page_link in page_links:
                    if (page_link and company_linkedin_url in page_link and
                        'public_jobs_topcard-org-name' in page_link):
                        company_match = True
                        break

            # Check if any of the keywords are in the page text
            keywords_found = False
            text = soup.get_text().lower()
            for kw in keywords_list:
                if kw in text:
                    keywords_found = True
                    break

            # If both conditions are true, add the job posting link
            if company_match and keywords_found:
                job_posting_links.append(link)

    return job_posting_links