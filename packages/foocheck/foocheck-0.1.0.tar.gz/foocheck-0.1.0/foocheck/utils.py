import httpx

async def check_username(username, url):
    """Check if a username is taken on a given platform.

    Args:
        username (str): The username to check.
        url (str): The URL format for the platform.

    Returns:
        str: A string indicating the status ("Taken", "Available", "Unknown", or "Error").
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    timeout = httpx.Timeout(10.0)  # 10 seconds timeout

    try:
        async with httpx.AsyncClient(http2=True, headers=headers, timeout=timeout, follow_redirects=True) as client:
            response = await client.get(url.format(username))
            if response.status_code == 200:
                return "Taken"
            elif response.status_code == 404:
                return "Available"
            else:
                return "Unknown"
    except httpx.RequestError:
        return "Error"
