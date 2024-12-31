import logging
import os
from typing import List
import aiohttp

from dhisana.utils.assistant_tool_tag import assistant_tool


@assistant_tool
async def send_email_with_mailgun(sender: str, recipients: List[str], subject: str, message: str):
    """
    Send an email using the Mailgun API.

    Parameters:
    - **sender** (*str*): The email address of the sender.
    - **recipients** (*List[str]*): A list of recipient email addresses.
    - **subject** (*str*): The subject of the email.
    - **message** (*str*): The HTML content of the email.
    """
    try:
        # Retrieve Mailgun API key and domain from environment variables
        api_key = os.environ["MAILGUN_NOTIFY_KEY"]
        domain = os.environ["MAILGUN_NOTIFY_DOMAIN"]

        # Prepare the data payload for the email
        data = {
            "from": sender,
            "to": recipients,
            "subject": subject,
            "html": message,
        }

        # Create an asynchronous HTTP session
        async with aiohttp.ClientSession() as session:
            # Send a POST request to the Mailgun API to send the email
            async with session.post(
                f"https://api.mailgun.net/v3/{domain}/messages",
                auth=aiohttp.BasicAuth("api", api_key),
                data=data,
            ) as response:
                # Return the response text
                return await response.text()
    except Exception as ex:
        # Log any exceptions that occur and return an error message
        logging.warning(f"Error sending email invite: {ex}")
        return {"error": str(ex)}