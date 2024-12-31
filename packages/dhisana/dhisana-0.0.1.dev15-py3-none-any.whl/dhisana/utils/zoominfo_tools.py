import asyncio
import hashlib
import json
import logging
import os
import aiohttp
import backoff
from typing import List, Optional
from datetime import datetime, timedelta
from dhisana.utils.cache_output_tools import cache_output, retrieve_output
from dhisana.utils.assistant_tool_tag import assistant_tool

# Utility functions to work with ZoomInfo API.

# Helper function to get ZoomInfo access token
async def get_zoominfo_access_token():
    ZOOMINFO_API_KEY = os.environ.get('ZOOMINFO_API_KEY')
    ZOOMINFO_API_SECRET = os.environ.get('ZOOMINFO_API_SECRET')
    if not ZOOMINFO_API_KEY or not ZOOMINFO_API_SECRET:
        raise EnvironmentError("ZoomInfo API key and secret not found in environment variables")

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": ZOOMINFO_API_KEY,
        "password": ZOOMINFO_API_SECRET
    }
    url = 'https://api.zoominfo.com/authenticate'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result.get('accessToken')
            else:
                result = await response.json()
                raise Exception(f"Failed to authenticate with ZoomInfo API: {result}")

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def enrich_person_info_from_zoominfo(
    linkedin_url: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    """
    Fetch a person's details from ZoomInfo using LinkedIn URL, email, or phone number.

    Parameters:
    - **linkedin_url** (*str*, optional): LinkedIn profile URL of the person.
    - **email** (*str*, optional): Email address of the person.
    - **phone** (*str*, optional): Phone number of the person.

    Returns:
    - **dict**: JSON response containing person information.
    """
    access_token = await get_zoominfo_access_token()
    if not access_token:
        return {'error': "Failed to obtain ZoomInfo access token"}

    if not linkedin_url and not email and not phone:
        return {'error': "At least one of linkedin_url, email, or phone must be provided"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {}
    if linkedin_url:
        data['personLinkedinUrls'] = [linkedin_url]
        cached_response = retrieve_output("enrich_person_info_from_zoominfo", linkedin_url)
        if cached_response is not None:
            return cached_response
    if email:
        data['personEmails'] = [email]
    if phone:
        data['personPhones'] = [phone]

    url = 'https://api.zoominfo.com/person/contact'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                if linkedin_url:
                    cache_output("enrich_person_info_from_zoominfo", linkedin_url, result)
                return result
            elif response.status == 429:
                logging.warning("enrich_person_info_from_zoominfo Rate limit hit")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"enrich_person_info_from_zoominfo Failed to run assistant: {result}")
                return {'error': result}


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def enrich_organization_info_from_zoominfo(
    organization_domain: Optional[str] = None,
):
    """
    Fetch an organization's details from ZoomInfo using the organization domain.

    Parameters:
    - **organization_domain** (*str*, optional): Domain of the organization.

    Returns:
    - **dict**: JSON response containing organization information.
    """
    access_token = await get_zoominfo_access_token()
    if not access_token:
        return {'error': "Failed to obtain ZoomInfo access token"}

    if not organization_domain:
        return {'error': "Organization domain must be provided"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    cached_response = retrieve_output("enrich_organization_info_from_zoominfo", organization_domain)
    if cached_response is not None:
        return cached_response

    data = {
        "companyDomains": [organization_domain]
    }

    url = 'https://api.zoominfo.com/company/enrich'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                cache_output("enrich_organization_info_from_zoominfo", organization_domain, result)
                return result
            elif response.status == 429:
                logging.warning("enrich_organization_info_from_zoominfo Rate limit hit")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"enrich_organization_info_from_zoominfo Failed to run assistant: {result}")
                return {'error': result}


@assistant_tool
async def get_enriched_customer_information_with_zoominfo(
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
    - **required_fields** (*List[str]*, optional): Properties of the customer to fetch.
    - **data_sources** (*List[str]*, optional): Data sources to fetch from (e.g., 'zoominfo', 'websearch', 'linkedin'). Defaults to all sources.

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
        data_sources = ['zoominfo', 'websearch', 'linkedin']

    data = await enrich_person_info_from_zoominfo(
        linkedin_url=linkedin_url,
        email=email,
        phone=phone,
    )
    return data


@assistant_tool
async def get_enriched_organization_information_with_zoominfo(
    organization_domain: Optional[str] = None,
    required_fields: Optional[List[str]] = None,
    data_sources: Optional[List[str]] = None,
):
    """
    Fetch an organization's details from specified data sources using the organization domain.

    Parameters:
    - **organization_domain** (*str*, optional): Domain of the organization.
    - **required_fields** (*List[str]*, optional): Properties of the organization to fetch.
    - **data_sources** (*List[str]*, optional): Data sources to fetch from (e.g., 'zoominfo', 'builtwith', 'linkedin'). Defaults to all sources.

    Returns:
    - **dict**: JSON response containing organization information.
    """
    data = await enrich_organization_info_from_zoominfo(organization_domain=organization_domain)
    return data


# Helper function to handle paginated ZoomInfo API calls
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=5,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def fetch_zoominfo_data(session, url, headers, payload):
    key_data = f"{url}_{json.dumps(payload, sort_keys=True)}"
    key_hash = hashlib.sha256(key_data.encode()).hexdigest()
    cached_response = retrieve_output("fetch_zoominfo_data", key_hash)
    if cached_response is not None:
        return cached_response

    async with session.post(url, headers=headers, json=payload) as response:
        if response.status == 200:
            result = await response.json()
            cache_output("fetch_zoominfo_data", key_hash, result)
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
async def search_recent_job_changes_with_zoominfo(
    job_titles: List[str],
    locations: List[str],
    organization_num_employees_ranges: Optional[List[str]],
    max_items_to_return: int
) -> List[dict]:
    """
    Search for individuals with specified job titles, locations, and optionally organization employee ranges who have recently changed jobs.

    Parameters:
    - **job_titles** (*List[str]*): List of job titles to search for.
    - **locations** (*List[str]*): List of locations to search in.
    - **organization_num_employees_ranges** (*Optional[List[str]]*, optional): List of employee ranges to filter organizations by.
    - **max_items_to_return** (*int*): Maximum number of items to return. Default is 100, max up to 5000.

    Returns:
    - **List[dict]**: List of individuals matching the criteria or error details.
    """
    access_token = await get_zoominfo_access_token()
    if not access_token:
        raise EnvironmentError("Failed to obtain ZoomInfo access token")

    if max_items_to_return <= 0:
        max_items_to_return = 10

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    url = 'https://api.zoominfo.com/person/search'

    # Define the search criteria
    criteria = {
        "personTitles": job_titles,
        "personLocationCities": locations,
        "pageSize": min(max_items_to_return, 100),
        "sortBy": "LastUpdatedDate",
        "sortOrder": "DESC"
    }

    if organization_num_employees_ranges and len(organization_num_employees_ranges) > 0:
        criteria["companyEmployeeCountRanges"] = organization_num_employees_ranges

    # Initialize the session
    async with aiohttp.ClientSession() as session:
        results = []
        page = 1
        page_size = min(max_items_to_return, 100)

        while len(results) < max_items_to_return:
            payload = {
                "criteria": criteria,
                "pagination": {
                    "page": page,
                    "pageSize": page_size
                }
            }

            try:
                data = await fetch_zoominfo_data(session, url, headers, payload)
                contacts = data.get('data', [])
                if not contacts:
                    break
                results.extend(contacts)

                total_records = data.get('total', 0)
                total_pages = (total_records // page_size) + (1 if total_records % page_size else 0)

                if page >= total_pages:
                    break

                page += 1
            except aiohttp.ClientResponseError as e:
                if e.status == 429:
                    await asyncio.sleep(30)  # Wait before retrying
                else:
                    # Return error details as JSON string in an array
                    error_details = {
                        'status': e.status,
                        'message': str(e),
                        'url': str(e.request_info.url),
                        'headers': dict(e.headers),
                    }
                    error_json = json.dumps(error_details)
                    return [error_json]

        return results[:max_items_to_return]


@assistant_tool
async def get_organization_domain_from_zoominfo(
    organization_id: str,
):
    """
    Fetch an organization's domain from ZoomInfo using the organization ID.

    Parameters:
    - organization_id (str): ID of the organization.

    Returns:
    - dict: Contains the organization's ID and domain, or an error message.
    """
    result = await get_organization_details_from_zoominfo(organization_id)
    if 'error' in result:
        return result
    domain = result.get('companyWebsite')
    if domain:
        return {'organization_id': organization_id, 'domain': domain}
    else:
        return {'error': 'Domain not found in the organization details'}


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def get_organization_details_from_zoominfo(
    organization_id: str,
):
    """
    Fetch an organization's details from ZoomInfo using the organization ID.

    Parameters:
    - organization_id (str): ID of the organization.

    Returns:
    - dict: Organization details or an error message.
    """
    access_token = await get_zoominfo_access_token()
    if not access_token:
        return {'error': "Failed to obtain ZoomInfo access token"}

    if not organization_id:
        return {'error': "Organization ID must be provided"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    cached_response = retrieve_output("get_organization_details_from_zoominfo", organization_id)
    if cached_response is not None:
        return cached_response

    url = f'https://api.zoominfo.com/company/detail'

    data = {
        "companyId": organization_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                org_details = result.get('data', {})
                if org_details:
                    cache_output("get_organization_details_from_zoominfo", organization_id, org_details)
                    return org_details
                else:
                    return {'error': 'Organization details not found in the response'}
            elif response.status == 429:
                logging.warning("get_organization_details_from_zoominfo Rate limit hit")
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

