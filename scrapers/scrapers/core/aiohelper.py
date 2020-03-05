import aiohttp
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=3), reraise=True)
async def fetch_json(session, url, params=None):
    """
    Fetch the data from a URL as json.
    :param aiohttp.ClientSession session: aiohttp session
    :param str url: request URL
    :param dict params: request parameters, defaults to None
    :return: the data from a URL as dict.
    :rtype: dict
    """
    if not params:
        params = {}
    try:
        async with session.get(url, params=params) as response:
            return await response.json()
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
        aiohttp.client_exceptions.ContentTypeError,
    ) as e:
        err = await response.text()
        print(f"aiohttp exception for {url} -> {e} => {err}")
        raise e


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=3), reraise=True)
async def fetch_text(session, url, params=None):
    """
    Fetch the data from a URL as text.
    :param aiohttp.ClientSession session: aiohttp session
    :param str url: request URL
    :param dict params: request parameters, defaults to None
    :return: the data from a URL as text.
    :rtype: str
    """
    if not params:
        params = {}
    try:
        async with session.get(url, params=params) as response:
            return await response.text()
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
        aiohttp.client_exceptions.ContentTypeError,
    ) as e:
        err = await response.text()
        print(f"aiohttp exception for {url} -> {e} => {err}")
        raise e
