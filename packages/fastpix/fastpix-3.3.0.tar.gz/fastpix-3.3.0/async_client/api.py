import aiohttp
import ssl
import certifi
from utilis.exceptions import APIError
from utilis.constants import BASE_URL


async def make_request(method, endpoint, headers=None, data=None, params=None):
    url = f"{BASE_URL}{endpoint}"
    headers = headers or {}

    # Create an SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                params=params,
                ssl=ssl_context  # Pass the SSL context here
            ) as response:
                try:
                    response_data = await response.json()
                except aiohttp.ContentTypeError:
                    response_data = await response.text()

                if response.ok:
                    return response_data
                else:
                    raise APIError(
                        message=f"Request failed with status {response.status}",
                        status_code=response.status,
                        details=response_data
                    )
    except aiohttp.ClientError as e:
        raise APIError(f"Request failed: {str(e)}")
