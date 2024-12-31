import asyncio
import hashlib
import json
import logging
import os
import aiohttp
import backoff
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from dhisana.utils.cache_output_tools import cache_output,retrieve_output
from dhisana.utils.assistant_tool_tag import assistant_tool
# Utility functions to work with Apollo API.

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=2,
    giveup=lambda e: e.status != 429,
    factor=10,
)
async def enrich_person_info_from_apollo(
    linkedin_url: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    """
    Fetch a person's details from Apollo using LinkedIn URL, email, or phone number.
    
    Parameters:
    - **linkedin_url** (*str*, optional): LinkedIn profile URL of the person.
    - **email** (*str*, optional): Email address of the person.
    - **phone** (*str*, optional): Phone number of the person.

    Returns:
    - **dict**: JSON response containing person information.
    """
    APOLLO_API_KEY = os.environ.get('APOLLO_API_KEY')
    if not APOLLO_API_KEY:
        return {'error': "Apollo API key not found in environment variables"}

    if not linkedin_url and not email and not phone:
        return {'error': "At least one of linkedin_url, email, or phone must be provided"}

    headers = {
        "X-Api-Key": f"{APOLLO_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {}
    if linkedin_url:
        data['linkedin_url'] = linkedin_url
        cached_response = retrieve_output("enrich_person_info_from_apollo", linkedin_url)
        if cached_response is not None:
            return cached_response
    if email:
        data['email'] = email
    if phone:
        data['phone_numbers'] = [phone]  # Apollo expects a list for phone numbers

    url = 'https://api.apollo.io/v1/people/match'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                if linkedin_url:
                    cache_output("enrich_person_info_from_apollo", linkedin_url, result)
                return result
            elif response.status == 429:
                logging.warning("enrich_person_info_from_apollo Rate limit hit")
                await asyncio.sleep(30)
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"enrich_person_info_from_apollo Failed to run assistant: ${result}")
                return {'error': result}


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=2,
    giveup=lambda e: e.status != 429,
    factor=30,
)
async def enrich_organization_info_from_apollo(
    organization_domain: Optional[str] = None,
):
    """
    Fetch a organization's details from Apollo using the organization domain.
    
    Parameters:
    - **organization_domain** (*str*, optional): Domain of the organization.

    Returns:
    - **dict**: JSON response containing organization information.
    """
    APOLLO_API_KEY = os.environ.get('APOLLO_API_KEY')
    if not APOLLO_API_KEY:
        return {'error': "Apollo API key not found in environment variables"}

    if not organization_domain:
        return {'error': "organization domain must be provided"}

    headers = {
        "X-Api-Key": f"{APOLLO_API_KEY}",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "accept": "application/json"
    }

    cached_response = retrieve_output("enrich_organization_info_from_apollo", organization_domain)
    if cached_response is not None:
        return cached_response

    url = f'https://api.apollo.io/api/v1/organizations/enrich?domain={organization_domain}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                cache_output("enrich_organization_info_from_apollo", organization_domain, result)
                return result
            elif response.status == 429:
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                return {'error': result}
            
@assistant_tool
async def get_enriched_customer_information(
    linkedin_url: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    required_fields: Optional[List[str]] = None,
    data_sources: Optional[List[str]] = None,
):
    """
    Fetch a person's details from specified data sources using LinkedIn URL, email, or phone number.

    Parameters:
    - **linkedin_url** (*str*, optional): LinkedIn profile URL of the person.
    - **email** (*str*, optional): Email address of the person.
    - **phone** (*str*, optional): Phone number of the person.
    - **required_fields** (*List[str]*, optional): Properties of the customer to fetch (e.g., 'job_history', 'education_history', 'skills', etc.).
    - **data_sources** (*List[str]*, optional): Data sources to fetch from (e.g., 'apollo', 'zoominfo', 'websearch', 'linkedin'). Defaults to all sources.

    Returns:
    - **dict**: JSON response containing person information.
    """
    # Set default values if not provided
    if required_fields is None:
        required_fields = [
            'job_history',
            'education_history',
            'skills',
            'headline',
            'summary',
            'experiences',
            'projects',
            'certifications',
            'publications',
            'languages',
            'volunteer_work',
        ]
    if data_sources is None:
        data_sources = ['apollo', 'zoominfo', 'websearch', 'linkedin']
        
    data = await enrich_person_info_from_apollo(
                linkedin_url=linkedin_url,
                email=email,
                phone=phone,
            )
    return data

@assistant_tool
async def get_enriched_organization_information(
    organization_domain: Optional[str] = None,
    required_fields: Optional[List[str]] = None,
    data_sources: Optional[List[str]] = None,
):
    """
    Fetch a organization's details from specified data sources using the organization domain.
    
    Parameters:
    - **organization_domain** (*str*, optional): Domain of the organization.
    - **required_fields** (*List[str]*, optional): Properties of the organization to fetch (e.g., 'technographics', 'firmographics', 'employee_count', etc.).
    - **data_sources** (*List[str]*, optional): Data sources to fetch from (e.g., 'apollo', 'zoominfo', 'builtwith', 'linkedin'). Defaults to all sources.

    Returns:
    - **dict**: JSON response containing organization information.
    """
    return await enrich_organization_info_from_apollo(organization_domain=organization_domain)



# Define the backoff strategy for handling rate limiting
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=5,
    giveup=lambda e: e.status != 429,
    factor=2,
)
async def fetch_apollo_data(session, url, headers, payload):
    key_data = f"{url}_{json.dumps(payload, sort_keys=True)}"
    key_hash = hashlib.sha256(key_data.encode()).hexdigest()
    cached_response = retrieve_output("fetch_apollo_data", key_hash)
    if cached_response is not None:
        return cached_response

    async with session.post(url, headers=headers, json=payload) as response:
        if response.status == 200:
            result = await response.json()
            cache_output("fetch_apollo_data", key_hash, result)
            return result
        elif response.status == 429:
            raise aiohttp.ClientResponseError(
                request_info=response.request_info,
                history=response.history,
                status=response.status,
                message="Rate limit exceeded",
                headers=response.headers
            )
        else:
            response.raise_for_status()



@assistant_tool
async def search_people_with_apollo(
    job_titles: List[str],
    locations: List[str],
    min_number_of_employees: int,
    max_number_of_employees: int,
    filter_by_signals: List[str],
    max_number_of_items_to_return: int,
    industries: List[str]
) -> List[Dict]:
    """
    Search for individuals on Apollo based on specified criteria.

    Parameters:
    - **job_titles** (*List[str]*): Job titles to include in the search.
    - **locations** (*List[str]*): Locations to filter the search.
    - **min_number_of_employees** (*int*): Minimum number of employees in the organization.
      Must be >= 1. Default is 1
    - **max_number_of_employees** (*int*): Maximum number of employees in the organization.
      Must be <= 100000 and greater than min_number_of_employees. Default 1000
    - **filter_by_signals** (*List[str]*): Signals to filter by. Valid options:
        - "RECENT_JOB_CHANGE"
        - "RAPID_EXPANSION"
    - **max_number_of_items_to_return** (*int*): Maximum number of results to return. Defaults to 100,
      with a maximum allowed value of 5000.
    - **industries** (*List[str]*): A list of industries to filter by. Defaults to [] for no filter. Default empty []

    Returns:
    - **List[Dict]**: A list of individual records (dictionaries) matching the specified criteria, 
      or a single-item list containing a JSON-encoded error dictionary if an error occurs.
    """

    # Validate min and max employees
    if min_number_of_employees < 1:
        raise ValueError("Minimum number of employees must be at least 1.")
    if max_number_of_employees > 100000:
        raise ValueError("Maximum number of employees must not exceed 100,000.")
    if min_number_of_employees >= max_number_of_employees:
        raise ValueError("Minimum number of employees must be less than the maximum number.")

    APOLLO_API_KEY = os.getenv('APOLLO_API_KEY')
    if not APOLLO_API_KEY:
        raise EnvironmentError("Apollo API key not found in environment variables.")

    # Log the search parameters for debugging
    logging.info(
        f"Initiating search with parameters: "
        f"Job titles: {job_titles}, Locations: {locations}, "
        f"Employee range: {min_number_of_employees}-{max_number_of_employees}, "
        f"Signals: {filter_by_signals}, "
        f"Industries: {industries}, "
        f"Max items: {max_number_of_items_to_return}"
    )

    # Ensure a positive number of items to return
    if max_number_of_items_to_return <= 0:
        max_number_of_items_to_return = 10

    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "X-Api-Key": APOLLO_API_KEY,
    }

    # Apollo endpoint for searching
    url = "https://api.apollo.io/v1/mixed_people/search"

    # Mapping of filter signals to their Apollo-specific IDs
    signal_mapping = {
        "RECENT_JOB_CHANGE": "643daa349293c1cdaa4d00f8",
        "RAPID_EXPANSION": "643daa3f9293c1cdaa4d00fa"
    }

    # Translate requested signals into Apollo signal IDs
    search_signal_ids = [signal_mapping[s] for s in filter_by_signals if s in signal_mapping]

    async with aiohttp.ClientSession() as session:
        results = []
        page = 1
        # Apollo API allows up to 100 items per page
        per_page = min(max_number_of_items_to_return, 100)

        while len(results) < max_number_of_items_to_return:
            payload = {
                "person_titles": job_titles,
                "person_locations": locations,
                "search_signal_ids": search_signal_ids,
                "organization_num_employees_ranges": [f"{min_number_of_employees},{max_number_of_employees}"],
                "page": page,
                "per_page": per_page
            }

            # Include industries filter if provided
            if industries:
                payload["organization_industries"] = industries

            try:
                data = await fetch_apollo_data(session, url, headers, payload)
                people = data.get('people', [])
                contacts = data.get('contacts', [])

                # If no results found, stop the loop
                if not people and not contacts:
                    break

                # Add the retrieved results
                results.extend(people + contacts)

                # Handle pagination
                pagination = data.get('pagination', {})
                current_page = pagination.get('page', 1)
                total_pages = pagination.get('total_pages', 1)

                if current_page >= total_pages:
                    # No more pages to fetch
                    break

                page += 1

            except aiohttp.ClientResponseError as e:
                # If rate-limited, wait and retry
                if e.status == 429:
                    await asyncio.sleep(30)
                else:
                    # Return error details as a JSON string in a list
                    error_details = {
                        'status': e.status,
                        'message': str(e),
                        'url': str(e.request_info.url),
                        'headers': dict(e.headers),
                    }
                    return [json.dumps(error_details)]

        # Return only up to the requested number of items
        return results[:max_number_of_items_to_return]

    
@assistant_tool
async def get_organization_domain_from_apollo(
    organization_id: str,
):
    """
    Fetch an organization's domain from Apollo using the organization ID.

    Parameters:
    - organization_id (str): ID of the organization.

    Returns:
    - dict: Contains the organization's ID and domain, or an error message.
    """
    result = await get_organization_details_from_apollo(organization_id)
    if 'error' in result:
        return result
    domain = result.get('primary_domain')
    if domain:
        return {'organization_id': organization_id, 'domain': domain}
    else:
        return {'error': 'Domain not found in the organization details'}

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    aiohttp.ClientResponseError,
    max_tries=3,
    giveup=lambda e: e.status != 429,
    factor=60,
)
async def get_organization_details_from_apollo(
    organization_id: str,
):
    """
    Fetch an organization's details from Apollo using the organization ID.

    Parameters:
    - organization_id (str): ID of the organization.

    Returns:
    - dict: Organization details or an error message.
    """
    APOLLO_API_KEY = os.environ.get('APOLLO_API_KEY')
    if not APOLLO_API_KEY:
        return {'error': "Apollo API key not found in environment variables"}

    if not organization_id:
        return {'error': "Organization ID must be provided"}

    headers = {
        "X-Api-Key": APOLLO_API_KEY,
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Accept": "application/json"
    }

    cached_response = retrieve_output("get_organization_details_from_apollo", organization_id)
    if cached_response is not None:
        return cached_response

    url = f'https://api.apollo.io/v1/organizations/{organization_id}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                org_details = result.get('organization', {})
                if org_details:
                    cache_output("get_organization_details_from_apollo", organization_id, org_details)
                    return org_details
                else:
                    return {'error': 'Organization details not found in the response'}
            elif response.status == 429:
                limit_minute = response.headers.get('x-rate-limit-minute')
                limit_hourly = response.headers.get('x-rate-limit-hourly')
                limit_daily = response.headers.get('x-rate-limit-daily')
                logging.info(f" get_organization_details_from_apollo x-rate-limit-minute: {limit_minute}")
                logging.info(f"get_organization_details_from_apollo x-rate-limit-hourly: {limit_hourly}")
                logging.info(f"get_organization_details_from_apollo x-rate-limit-daily: {limit_daily}")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                return {'error': result}