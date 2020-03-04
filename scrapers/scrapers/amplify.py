import asyncio
import csv
import dataclasses
import re

import aiohttp

SEARCH_URL = "https://api.givegab.com/v1/campaigns"
DETAILS_URL = "https://www.amplifyatx.org/organizations"


@dataclasses.dataclass
class Organization:
    name: str
    slug: str
    website: str = ""
    email: str = ""


def main():
    """Define the main entrypoint."""
    asyncio.run(search_all())


async def fetch_data(session, url, params=None):
    """
    Fetch the data from a URL as text.
    :param aiohttp.ClientSession session: aiohttp session
    :param str url: request URL
    :param dict params: request paramemters, defaults to None
    :return: the data from a URL as text.
    :rtype: str
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


async def fetch_text(session, url, params=None):
    """
    Fetch the data from a URL as text.
    :param aiohttp.ClientSession session: aiohttp session
    :param str url: request URL
    :param dict params: request paramemters, defaults to None
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


async def parse_summary(session, page):
    """"""
    orgs = []
    # params = {"show_all": "true", "page": page}
    params = {
        "donatable": "true",
        "dog_campaign": "",
        "dog_id": "510",
        "use_new_search": "true",
        "visible_only": "true",
        "with": "address,dog_url,has_profile,stats,story_image_url",
        "sort_column": "alpha",
        "sort_order": "asc",
        "page": page,
    }
    response = await fetch_data(session, SEARCH_URL, params)
    for campaign in response["campaigns"]:
        name = campaign["group"]["name"]
        slug = campaign["group"]["slug"]
        o = Organization(name, slug)
        orgs.append(o)
    return orgs


async def parse_details(session, org):
    website_regex = re.compile(r",\"website\":\"(.*?)\"")
    email_regex = re.compile(r",\"email\":\"(.*?)\"")
    response = await fetch_text(session, f"{DETAILS_URL}/{org.slug}")
    website_match = website_regex.search(response)
    org.website = website_match.groups()[0] if website_match else ""
    email_match = email_regex.search(response)
    org.email = email_match.groups()[0] if email_match else ""
    return org


async def search_all():
    async with aiohttp.ClientSession() as session:
        tasks = [parse_summary(session, page) for page in range(0, 35)]
        page_res = await asyncio.gather(*tasks)
        orgs = [org for orgs in page_res for org in orgs]
        tasks = [parse_details(session, org) for org in orgs]
        full_orgs = await asyncio.gather(*tasks)
        fieldnames = dataclasses.asdict(full_orgs[0]).keys()
        with open("amplify.csv", "w") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, extrasaction="ignore"
            )
            writer.writeheader()
            for org in full_orgs:
                writer.writerow(dataclasses.asdict(org))


if __name__ == "__main__":
    main()
