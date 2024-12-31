import asyncio
import json
import os
import aiohttp
import backoff
from typing import List, Optional

from bs4 import BeautifulSoup
from dhisana.utils.assistant_tool_tag import assistant_tool
from dhisana.utils.cache_output_tools import cache_output, retrieve_output
from dhisana.utils.serpapi_search_tools import search_google
from dhisana.utils.web_download_parse_tools import get_html_content_from_url
from urllib.parse import urlparse
from urllib.parse import urlparse, urlunparse


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=10,
)
async def enrich_person_info_from_proxycurl(
    linkedin_url: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    """
    Fetch a person's details from Proxycurl using LinkedIn URL, email, or phone number.

    Parameters:
    - linkedin_url (str, optional): LinkedIn profile URL of the person.
    - email (str, optional): Email address of the person.
    - phone (str, optional): Phone number of the person.

    Returns:
    - dict: JSON response containing person information.
    """
    API_KEY = os.getenv('PROXY_CURL_API_KEY')
    if not API_KEY:
        raise EnvironmentError("Proxycurl API key not found in environment variables")

    HEADERS = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    if not linkedin_url and not email and not phone:
        return {'error': "At least one of linkedin_url, email, or phone must be provided"}
    
    if linkedin_url:
        cached_response = retrieve_output("enrich_person_info_from_proxycurl", linkedin_url)
        if cached_response is not None:
            return cached_response


    params = {}
    if linkedin_url:
        params['url'] = linkedin_url
    if email:
        params['email'] = email
    if phone:
        params['phone'] = phone

    url = 'https://nubela.co/proxycurl/api/v2/linkedin'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as response:
            if response.status == 200:
                result = await response.json()
                if linkedin_url:
                    cache_output("enrich_person_info_from_proxycurl", linkedin_url, result)
                return result
            elif response.status == 429:
                await asyncio.sleep(30)
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                return {'error': await response.json()}




@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=10,
)
async def enrich_organization_info_from_proxycurl(
    organization_domain: Optional[str] = None,
    organization_linkedin_url: Optional[str] = None,
):
    """
    Fetch an organization's details from Proxycurl using either the organization domain or LinkedIn URL.

    Parameters:
    - organization_domain (str, optional): Domain of the organization.
    - organization_linkedin_url (str, optional): LinkedIn URL of the organization.

    Returns:
    - dict: JSON response containing organization information.
    """
    API_KEY = os.getenv('PROXY_CURL_API_KEY')
    if not API_KEY:
        raise EnvironmentError("Proxycurl API key not found in environment variables")

    HEADERS = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    if not organization_domain and not organization_linkedin_url:
        return {'error': "Either organization domain or LinkedIn URL must be provided"}

    if organization_linkedin_url:
        # Standardize LinkedIn URL to 'https://www.linkedin.com/company/<public_identifier>' format
        parsed_url = urlparse(organization_linkedin_url)
        if parsed_url.netloc != 'www.linkedin.com':
            standardized_netloc = 'www.linkedin.com'
            standardized_path = parsed_url.path
            if not standardized_path.startswith('/company/'):
                standardized_path = '/company' + standardized_path
            standardized_url = urlunparse(parsed_url._replace(netloc=standardized_netloc, path=standardized_path))
        else:
            standardized_url = organization_linkedin_url

        # Check if LinkedIn URL data is cached
        cached_response = retrieve_output("enrich_organization_info_from_proxycurl", standardized_url)
        if cached_response is not None:
            return cached_response

        # Fetch details using standardized LinkedIn URL
        url = 'https://nubela.co/proxycurl/api/v2/linkedin/company'
        params = {'url': standardized_url}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS, params=params) as response:
                if response.status == 200:
                    result = await response.json()
                    cache_output("enrich_organization_info_from_proxycurl", standardized_url, result)
                    return result
                else:
                    return {'error': await response.json()}

    if organization_domain:
        # Check if domain data is cached
        cached_response = retrieve_output("enrich_organization_info_from_proxycurl", organization_domain)
        if cached_response is not None:
            return cached_response

        # Resolve company URL from domain
        resolve_url = 'https://nubela.co/proxycurl/api/linkedin/company/resolve'
        params = {'domain': organization_domain}

        async with aiohttp.ClientSession() as session:
            async with session.get(resolve_url, headers=HEADERS, params=params) as response:
                if response.status == 200:
                    company_data = await response.json()
                    company_url = company_data.get('url')
                    if company_url:
                        # Standardize the resolved LinkedIn URL
                        parsed_url = urlparse(company_url)
                        if parsed_url.netloc != 'www.linkedin.com':
                            standardized_netloc = 'www.linkedin.com'
                            standardized_path = parsed_url.path
                            if not standardized_path.startswith('/company/'):
                                standardized_path = '/company' + standardized_path
                            standardized_url = urlunparse(parsed_url._replace(netloc=standardized_netloc, path=standardized_path))
                        else:
                            standardized_url = company_url

                        # Fetch company profile using standardized LinkedIn URL
                        profile_url = 'https://nubela.co/proxycurl/api/v2/linkedin/company'
                        async with session.get(profile_url, headers=HEADERS, params={'url': standardized_url}) as profile_response:
                            if profile_response.status == 200:
                                result = await profile_response.json()
                                cache_output("enrich_organization_info_from_proxycurl", organization_domain, result)
                                return result
                            else:
                                return {'error': await profile_response.json()}
                    else:
                        return {'error': 'Company URL not found for the provided domain'}
                elif response.status == 429:
                    await asyncio.sleep(30)
                    raise aiohttp.ClientResponseError(
                        request_info=response.request_info,
                        history=response.history,
                        status=response.status,
                        message="Rate limit exceeded",
                        headers=response.headers
                    )
                else:
                    return {'error': await response.json()}


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=10,
)
async def enrich_job_info_from_proxycurl(
    job_url: Optional[str] = None,
):
    """
    Fetch a job's details from Proxycurl using the job URL.

    Parameters:
    - job_url (str, optional): URL of the LinkedIn job posting.

    Returns:
    - dict: JSON response containing job information.
    """
    API_KEY = os.getenv('PROXY_CURL_API_KEY')
    if not API_KEY:
        raise EnvironmentError("Proxycurl API key not found in environment variables")

    HEADERS = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    if not job_url:
        return {'error': "Job URL must be provided"}
    
    if job_url:
        cached_response = retrieve_output("enrich_job_info_from_proxycurl", job_url)
        if cached_response is not None:
            return cached_response

    params = {'url': job_url}
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/job'

    async with aiohttp.ClientSession() as session:
        async with session.get(api_endpoint, headers=HEADERS, params=params) as response:
            if response.status == 200:
                result = await response.json()
                if job_url:
                    cache_output("enrich_job_info_from_proxycurl", job_url, result)
                return result
            elif response.status == 429:
                await asyncio.sleep(30)
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                return {'error': await response.json()}

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=10,
)
async def search_recent_job_changes(
    job_titles: List[str],
    locations: List[str],
    max_items_to_return: int = 100
) -> List[dict]:
    """
    Search for individuals with specified job titles and locations who have recently changed jobs.

    Parameters:
    - job_titles (List[str]): List of job titles to search for.
    - locations (List[str]): List of locations to search in.
    - max_items_to_return (int, optional): Maximum number of items to return. Defaults to 100.

    Returns:
    - List[dict]: List of individuals matching the criteria.
    """
    
    API_KEY = os.getenv('PROXY_CURL_API_KEY')
    if not API_KEY:
        raise EnvironmentError("Proxycurl API key not found in environment variables")

    HEADERS = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }


    url = 'https://nubela.co/proxycurl/api/search/person'
    results = []
    page = 1
    per_page = min(max_items_to_return, 100)

    async with aiohttp.ClientSession() as session:
        while len(results) < max_items_to_return:
            params = {
                'job_title': ','.join(job_titles),
                'location': ','.join(locations),
                'page': page,
                'num_records': per_page
            }
            async with session.get(url, headers=HEADERS, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    people = data.get('persons', [])
                    if not people:
                        break
                    results
 
@assistant_tool
async def find_matching_job_posting_proxy_curl(
    company_name: str,
    keywords_check: List[str],
    optional_keywords: List[str],
    company_linkedin_url: Optional[str] = None  
) -> List[str]:
    """
    Find job postings on LinkedIn for a given company using Google Custom Search.

    Args:
        company_name (str): The name of the company.
        keywords_check (List[str]): A list of keywords to include in the search.
        optinal_keywords (List[str]): A list of optional keywords to include in the search.
        company_linkedin_url (Optional[str]): The LinkedIn URL of the company.

    Returns:
        List[str]: A list of job posting links.
    """
    keywords_list = [kw.strip().lower() for kw in keywords_check]
    job_posting_links = []

    
    # Combine all keywords into a single query
    keywords_str = ' '.join(f'"{kw}"' for kw in keywords_check)
    optional_keywords_str = ' '.join(f'{kw}' for kw in optional_keywords)
    query = f'site:*linkedin.com/jobs/view/ "{company_name}" {keywords_str} {optional_keywords_str}'
    

    # Search for job postings on Google with the query
    results = await search_google(query.strip(), 1)
    if not isinstance(results, list) or len(results) == 0:
        query = f'site:*linkedin.com/jobs/view/ "{company_name}" {keywords_str}'
        # Search for job postings on Google with the query
        results = await search_google(query.strip(), 1)
        if not isinstance(results, list) or len(results) == 0:
            return job_posting_links
    
        

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
            json_result = await enrich_job_info_from_proxycurl(link)
        except Exception:
            continue

        if not json_result:
            continue

        text = json.dumps(json_result).lower()
        
        if company_linkedin_url and json_result.get('company', {}) and json_result.get('company', {}).get('url', ''):
            result_url = json_result.get('company', {}).get('url', '').lower()
            result_path = urlparse(result_url).path
            company_path = urlparse(company_linkedin_url.lower()).path
            company_match = result_path == company_path
        else:
            company_match = False

        
        keywords_found = any(kw in text for kw in keywords_list)

        # If both conditions are true, add the job posting link
        if company_match and keywords_found:
            job_posting_links.append(link)

    return job_posting_links