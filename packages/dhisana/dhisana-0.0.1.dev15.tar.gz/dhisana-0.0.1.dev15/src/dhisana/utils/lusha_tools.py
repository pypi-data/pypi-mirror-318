import logging
import os
import aiohttp
import backoff
from typing import Dict, Optional
from dhisana.utils.cache_output_tools import cache_output, retrieve_output
from dhisana.utils.assistant_tool_tag import assistant_tool

# Utility functions to work with Lusha API.

# Helper function to get Lusha access token
async def get_lusha_access_token():
    LUSHA_API_KEY = os.environ.get('LUSHA_API_KEY')
    if not LUSHA_API_KEY:
        raise EnvironmentError("Lusha API key not found in environment variables")

    return LUSHA_API_KEY

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def enrich_person_info_from_lusha(
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    """
    Fetch a person's details from Lusha using email or phone number.

    Parameters:
    - **email** (*str*, optional): Email address of the person.
    - **phone** (*str*, optional): Phone number of the person.

    Returns:
    - **dict**: JSON response containing person information.
    """
    access_token = await get_lusha_access_token()
    if not access_token:
        return {'error': "Failed to obtain Lusha access token"}

    if not email and not phone:
        return {'error': "At least one of email or phone must be provided"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {}
    if email:
        data['email'] = email
        cached_response = retrieve_output("enrich_person_info_from_lusha", email)
        if cached_response is not None:
            return cached_response
    if phone:
        data['phone'] = phone

    url = 'https://api.lusha.com/person'

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                if email:
                    cache_output("enrich_person_info_from_lusha", email, result)
                return result
            elif response.status == 429:
                logging.warning("enrich_person_info_from_lusha Rate limit hit")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"enrich_person_info_from_lusha Failed to run assistant: {result}")
                return {'error': result}

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def enrich_organization_info_from_lusha(
    domain: Optional[str] = None,
):
    """
    Fetch an organization's details from Lusha using the organization's domain.

    Parameters:
    - **domain** (*str*, optional): Domain of the organization.

    Returns:
    - **dict**: JSON response containing organization information.
    """
    access_token = await get_lusha_access_token()
    if not access_token:
        return {'error': "Failed to obtain Lusha access token"}

    if not domain:
        return {'error': "Organization domain must be provided"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    cached_response = retrieve_output("enrich_organization_info_from_lusha", domain)
    if cached_response is not None:
        return cached_response

    url = f'https://api.lusha.com/company?domain={domain}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                cache_output("enrich_organization_info_from_lusha", domain, result)
                return result
            elif response.status == 429:
                logging.warning("enrich_organization_info_from_lusha Rate limit hit")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"enrich_organization_info_from_lusha Failed to run assistant: {result}")
                return {'error': result}

@assistant_tool
async def search_person_with_lusha(
    first_name: str,
    last_name: str,
    domain: Optional[str] = None,
):
    """
    Search for a person's details using their first name, last name, and optionally organization domain.

    Parameters:
    - **first_name** (*str*): First name of the person.
    - **last_name** (*str*): Last name of the person.
    - **domain** (*Optional[str]*, optional): Organization domain to refine the search.

    Returns:
    - **dict**: JSON response containing person search results.
    """
    access_token = await get_lusha_access_token()
    if not access_token:
        return {'error': "Failed to obtain Lusha access token"}

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    url = 'https://api.lusha.com/search'
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "domain": domain if domain else None
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 429:
                logging.warning("search_person_with_lusha Rate limit hit")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.warning(f"search_person_with_lusha Failed to run assistant: {result}")
                return {'error': result}

@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def contact_search(
    page: int = 0,
    size: int = 10,
    contact_filters: Optional[Dict] = None,
    company_filters: Optional[Dict] = None
) -> Dict:
    """
    Search for contacts in Lusha with dynamic filters.

    Parameters:
    - **page** (*int*, optional): Page number (default: 0).
    - **size** (*int*, optional): Page size (default: 10).
    - **contact_filters** (*Dict*, optional): Dictionary of filters for contacts.
    - **company_filters** (*Dict*, optional): Dictionary of filters for companies.

    Returns:
    - **dict**: JSON response containing contact search results.
    """
    api_key = await get_lusha_access_token()
    headers = {
        "api_key": api_key,
        "Content-Type": "application/json"
    }
    url = "https://api.lusha.com/prospecting/contact/search"
    payload = {
        "pages": {"page": page, "size": size},
        "filters": {
            "contacts": {"include": contact_filters or {}},
            "companies": {"include": company_filters or {}}
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 429:
                logging.warning("Rate limit hit for contact_search")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.error(f"Contact search failed: {result}")
                return {"error": result}


@assistant_tool
@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientResponseError, Exception),
    max_tries=3,
    giveup=lambda e: not (isinstance(e, aiohttp.ClientResponseError) and e.status == 429),
    factor=2,
)
async def company_search(
    page: int = 0,
    size: int = 10,
    company_filters: Optional[Dict] = None
) -> Dict:
    """
    Search for companies in Lusha with dynamic filters.

    Parameters:
    - **page** (*int*, optional): Page number (default: 0).
    - **size** (*int*, optional): Page size (default: 10).
    - **company_filters** (*Dict*, optional): Dictionary of filters for companies.

    Returns:
    - **dict**: JSON response containing company search results.
    """
    api_key = await get_lusha_access_token()
    headers = {
        "api_key": api_key,
        "Content-Type": "application/json"
    }
    url = "https://api.lusha.com/prospecting/company/search"
    payload = {
        "pages": {"page": page, "size": size},
        "filters": {
            "companies": {"include": company_filters or {}}
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 429:
                logging.warning("Rate limit hit for company_search")
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message="Rate limit exceeded",
                    headers=response.headers
                )
            else:
                result = await response.json()
                logging.error(f"Company search failed: {result}")
                return {"error": result}
