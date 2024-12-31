import asyncio
import os
import logging
from typing import List, Optional
import playwright
from pydantic import BaseModel, Field
from playwright.async_api import async_playwright, Page
import pandas as pd

from dhisana.utils.assistant_tool_tag import assistant_tool
from dhisana.utils.dataframe_tools import get_structured_output
from dhisana.utils.web_download_parse_tools import parse_html_content_as_text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SalesNavLeadInformation(BaseModel):
    full_name: str = Field(..., description="Full name of the lead")
    job_title: str = Field(..., description="Job title of the lead")
    organization_name: str = Field(..., description="Name of the organization the lead works for")
    location: str = Field(..., description="Location of the lead")
    months_in_role: int = Field(..., description="Number of months in the current role. Convert from years and months to this.")
    months_in_organization: int = Field(..., description="Number of months in the organization. Convert from years and months to this value")
    summary: str = Field(..., description="Short summary or description about the lead's expertise or role")
    number_of_mutual_connections: int = Field(..., description="Number of mutual LinkedIn connections with the lead. Default 0")
    tags: List[str] = Field(..., description="List of tags such as 'Viewed', 'Past Colleague', 'Recently In News', 'Posted Recently' etc.")
    lead_salesnavigator_url: str = Field(..., description="Sales Navigator URL of lead is in format /sales/lead/{lead_salesnavigator_id},Name")

class SalesNavLeadsList(BaseModel):
    data: List[SalesNavLeadInformation]
    
class SalesNavigatorUserProfile(BaseModel):
    full_name: str = Field(..., description="Full name of the lead")
    job_title: str = Field(..., description="Job title of the lead")
    organization_name: str = Field(..., description="Name of the organization the lead works for")
    location: str = Field(..., description="Location of the lead")
    months_in_role: int = Field(..., description="Number of months in the current role. Convert from years and months to this.")
    months_in_organization: int = Field(..., description="Number of months in the organization. Convert from years and months to this value")
    summary: str = Field(..., description="Short summary or description about the lead's expertise or role")
    number_of_mutual_connections: int = Field(..., description="Number of mutual LinkedIn connections with the lead")
    tags: List[str] = Field(..., description="List of tags such as 'Viewed', 'Past Colleague', 'Recently In News', 'Posted Recently' etc.")
    lead_salesnavigator_id: str = Field(..., description="Sales Navigator URL of the lead. format is like https://www.linkedin.com/sales/lead/{id}")
    linkedin_url: str = Field(..., description="LinkedIn URL of the lead. Keep it empty if not available")
    num_of_followers: int = Field(..., description="Number of followers of the lead")
    education: List[str] = Field(..., description="List of educational qualifications of the lead")
    skills: List[str] = Field(..., description="List of skills of the lead")
    recommendations: List[str] = Field(..., description="List of recommendations for the lead")
    accomplishments: List[str] = Field(..., description="List of accomplishments of the lead")
    interests: List[str] = Field(..., description="List of interests of the lead")
    sales_navigator_insight: str = Field(..., description="Sales Navigator insights about the lead")
    key_signals: str = Field(..., description="Key signals about the lead")
    common_connection_paths: List[str] = Field(..., description="List of common connection paths with the lead")
    

class SalesNavUserProfilesList(BaseModel):
    data: List[SalesNavigatorUserProfile]


class SalesNavAccountInformation(BaseModel):
    company_sales_navigator_url: str = Field(..., description="Sales Navigator URL of the company. format is like https://www.linkedin.com/sales/company/{company_id}")
    company_sales_navigator_id: str = Field(..., description="Sales Navigator ID of the company")
    company_name: str = Field(..., description="Name of the account")
    about_company: str = Field(..., description="Description of the company")
    number_of_employees_in_linked_in: int = Field(..., description="Number of employees in the account")
    revenue: str = Field(..., description="Revenue of the account")
    company_website: str = Field(..., description="Website of the account")
    company_primary_domain: str = Field(..., description="Primary domain of the account")
    company_linkedin_url: str = Field(..., description="LinkedIn URL of the account")
    tags: List[str] = Field(..., description="List of tags such as Industry, Revenue, HeadCountGorwth etc.")

class SalesNavAccountInformationList(BaseModel):
    data: List[SalesNavAccountInformation]
     
async def scroll_to_bottom(page: Page):
    """
    Scrolls to the bottom of the page by:
    - If '#search-results-container' is present, scrolls within it up to 4 times.
    - Else, moves the mouse to the right half center of the page and simulates mouse wheel events.
    Performs a maximum of 4 scrolls. If any issues occur during scrolling, it stops further actions.
    """
    try:
        # Check if the container exists
        container = await page.query_selector("#search-results-container")
        if container:
            logger.info("Found '#search-results-container'. Scrolling within the container.")
            previous_scroll_height = -1
            max_scrolls = 4  # Maximum number of scrolls

            for scroll_count in range(1, max_scrolls + 1):
                try:
                    # Scroll down by 500px within the container
                    await container.evaluate("el => el.scrollBy(0, 500)")
                    logger.debug(f"Scrolled down by 500px within container on scroll {scroll_count}.")

                    # Wait for content to load
                    await page.wait_for_timeout(1000)  # Wait for 1 second
                    logger.debug(f"Waited for 1 second after scroll {scroll_count} within container.")

                    # Get the current scroll height of the container
                    scroll_height = await container.evaluate("el => el.scrollHeight")
                    logger.debug(f"Current scroll height within container: {scroll_height}.")

                    if scroll_height == previous_scroll_height:
                        # Reached the bottom; no further scrolling needed
                        logger.info(f"No change in scroll height after scroll {scroll_count}. Reached the bottom of the container.")
                        break

                    previous_scroll_height = scroll_height
                    logger.info(f"Completed scroll {scroll_count} within container.")

                except Exception as e:
                    logger.error(f"Error during scrolling within container on scroll {scroll_count}: {e}")
                    break
            else:
                logger.info(f"Reached maximum scroll limit of {max_scrolls} scrolls within container.")

        else:
            logger.info("'#search-results-container' not found. Scrolling the page directly.")

            # Retrieve the viewport size
            viewport = page.viewport_size
            if viewport is None:
                logger.error("Could not retrieve viewport size.")
                return

            width, height = viewport['width'], viewport['height']
            logger.debug(f"Viewport size: width={width}, height={height}.")

            # Calculate the coordinates for the right half center of the page
            x = (width * 3) / 4
            y = height / 2
            logger.debug(f"Calculated mouse position: ({x}, {y}).")

            previous_scroll_height = -1
            max_scrolls = 15  # Maximum number of scrolls

            for scroll_count in range(1, max_scrolls + 1):
                try:
                    # Move mouse to the right half center
                    await page.mouse.move(x, y)
                    logger.debug(f"Moved mouse to ({x}, {y}) on scroll {scroll_count}.")

                    # Scroll the mouse wheel down by 500 pixels
                    await page.mouse.wheel(0, 500)
                    logger.debug(f"Scrolled down by 500px on scroll {scroll_count}.")

                    # Wait for content to load
                    await page.wait_for_timeout(2000)  # Wait for 1 second
                    logger.debug(f"Waited for 1 second after scroll {scroll_count}.")
                except Exception as e:
                    logger.error(f"Error during scrolling on scroll {scroll_count}: {e}")
                    break
            else:
                logger.info(f"Reached maximum scroll limit of {max_scrolls} scrolls.")

        logger.info("Completed scrolling to the bottom of the page.")

    except Exception as e:
        logger.error(f"Failed to execute scroll_to_bottom function: {e}")


async def extract_leads_from_current_page(page: Page) -> List[SalesNavLeadInformation]:
    """
    Extracts leads data from the current page.
    """
    leads = []

    # Get page HTML content
    html_content = await page.content()
    content_text = parse_html_content_as_text(html_content)
    if not content_text:
        return [], 'FAIL'

    # Get structured content using OpenAI's API
    extract_content, status = await get_structured_output(content_text, SalesNavLeadsList, model="gpt-4o-mini")
    if status == 'FAIL':
        return [], 'FAIL'
    leads = extract_content.data
    return leads, 'SUCCESS'

async def extract_accounts_from_current_page(page: Page) -> List[SalesNavAccountInformation]:
    """
    Extracts leads data from the current page.
    """
    leads = []

    # Get page HTML content
    html_content = await page.content()
    content_text = parse_html_content_as_text(html_content)
    if not content_text:
        return [], 'FAIL'

    # Get structured content using OpenAI's API
    extract_content, status = await get_structured_output(content_text, SalesNavAccountInformationList, model="gpt-4o-mini")
    if status == 'FAIL':
        return [], 'FAIL'
    leads = extract_content.data
    return leads, 'SUCCESS'

async def extract_lead_from_current_page(page: Page) -> List[SalesNavigatorUserProfile]:
    """
    Extracts leads data from the current page.
    """
    leads = []

    # Get page HTML content
    html_content = await page.content()
    content_text = parse_html_content_as_text(html_content)
    if not content_text:
        return [], 'FAIL'

    # Get structured content using OpenAI's API
    extract_content, status = await get_structured_output(content_text, SalesNavigatorUserProfile, model="gpt-4o-mini")
    if status == 'FAIL':
        return [], 'FAIL'
    leads = [extract_content]
    return leads, 'SUCCESS'

async def extract_account_from_current_page(page: Page) -> List[SalesNavAccountInformation]:
    """
    Extracts leads data from the current page.
    """
    leads = []

    # Get page HTML content
    html_content = await page.content()
    content_text = parse_html_content_as_text(html_content)
    if not content_text:
        return [], 'FAIL'

    # Get structured content using OpenAI's API
    extract_content, status = await get_structured_output(content_text, SalesNavAccountInformation, model="gpt-4o-mini")
    if status == 'FAIL':
        return [], 'FAIL'
    leads = [extract_content]
    return leads, 'SUCCESS'

async def extract_from_page_with_pagination(page: Page, url: str, max_pages: int = 95) -> List[SalesNavLeadInformation]:
    """
    Extracts leads data from Sales Navigator with pagination.
    """
    leads_data = []
    current_page = 1

    await page.goto(url)
    await page.wait_for_load_state('load')

    while current_page <= max_pages:
        logger.info(f"Processing page {current_page}")

        # Scroll to the bottom to load all leads
        await scroll_to_bottom(page)

        # Wait for dynamic content to load
        await asyncio.sleep(2)

        # Extract leads from the current page
        if '/sales/search/people' in url:
            page_items, status = await extract_leads_from_current_page(page)
        elif '/sales/search/company' in url:
            page_items, status = await extract_accounts_from_current_page(page)
        elif '/sales/lead/' in url:
            page_items, status = await extract_lead_from_current_page(page)
        elif '/sales/company/' in url:
            page_items, status = await extract_account_from_current_page(page)
        else:
            logger.warn("Invalid URL. Exiting.")
            break
        if (status == 'FAIL') or (not page_items):
            logger.info("Extraction failed or no leads found. Ending pagination.")
            break
        leads_data.extend(page_items)

        # Attempt to click the "Next" button
        try:
            next_buttons = page.locator("button[aria-label='Next']")
            await next_buttons.wait_for(state='attached', timeout=5000)  # Wait up to 5 seconds for the button to appear

            if await next_buttons.count() == 0:
                logger.info("Next button not found. Possibly less than 10 entries. End of pagination.")
                break

            next_button = next_buttons.first  # Corrected: Removed parentheses

            # Ensure the "Next" button is visible and enabled
            await next_button.wait_for(state='visible', timeout=5000)

            if await next_button.is_disabled():
                logger.info("Next button is disabled. End of pagination.")
                break

            await next_button.click()
            await page.wait_for_load_state('load')
            current_page += 1

        except asyncio.TimeoutError:
            logger.error("Timeout while waiting for the Next button. Ending pagination.")
            break
        except Exception as e:
            logger.error(f"Failed to navigate to next page: {e}")
            break

    return leads_data

async def login_to_linkedin(page: Page, email: str, password: str, headless: bool):
    """
    Logs into LinkedIn using the provided email and password.
    If credentials are not provided, waits for user to log in manually.
    """
    await page.goto("https://www.linkedin.com/uas/login?session_redirect=%2Fsales")
    await page.wait_for_load_state('load')    
    if email and password:
        await page.get_by_label("Email or Phone").click()
        await page.get_by_label("Email or Phone").fill(email)
        await page.get_by_label("Password").click()
        await page.get_by_label("Password").fill(password)
        await page.locator("#organic-div form").get_by_role("button", name="Sign in", exact=True).click()
        await page.wait_for_load_state('load')
    else:
        logger.info("Waiting for user to log in manually...")
        try:
            await page.wait_for_url(lambda url: url == "https://www.linkedin.com/sales/home", timeout=300000)  # 5 minutes
            logger.info("User logged in successfully.")
        except:
            logger.error("Timeout waiting for user to log in.")
            return 'FAIL'
    
    if "checkpoint/challenge" in page.url:
        if not headless:
            logger.warning("Captcha page encountered! Human intervention is needed.")
            max_iterations = 25
            for attempt in range(max_iterations):
                await asyncio.sleep(5)
                await page.wait_for_load_state('load')
                if "checkpoint/challenge" not in page.url:
                    logger.info("Captcha solved. Continuing with the process.")
                    break
            else:
                logger.error(f"Captcha not solved after {max_iterations} attempts. Exiting.")
                return 'FAIL'
            await asyncio.sleep(3)
        else:
            logger.error("Captcha page encountered! Aborting due to headless mode.")
            return 'FAIL'
    return 'SUCCESS'

@assistant_tool
async def extract_leads_from_sales_navigator(urls_to_track: List[str], output_file_path: str):
    """
    Main function to orchestrate scraping and data extraction.
    """
    email = os.environ.get("LINKEDIN_EMAIL", "")
    password = os.environ.get("LINKEDIN_PASSWORD", "")
    
    
    # Start the browser using Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Login to LinkedIn
        login_status = await login_to_linkedin(page, email, password, False)
        if login_status == 'FAIL':
            return {"status": "FAIL", "message": "Login failed due to captcha or incorrect credentials."}

        all_leads = []
        for track_url in urls_to_track:
            leads = await extract_from_page_with_pagination(page, track_url)
            all_leads.extend(leads)

        # Close the browser
        await browser.close()

        # Convert to DataFrame and save to CSV or desired format
        df = pd.DataFrame([lead.model_dump() for lead in all_leads])
        df.to_csv(output_file_path, index=False)

        return {"status": "SUCCESS", "message": f"Data extraction completed successfully to {output_file_path}."}
    