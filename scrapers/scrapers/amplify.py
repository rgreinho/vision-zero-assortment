import asyncio
import csv
import dataclasses
import json

import aiohttp

from scrapers.core import aiohelper
from scrapers.core.container import Organization

SEARCH_URL = "https://api.givegab.com/v1/campaigns"
DETAILS_URL = "https://www.amplifyatx.org/organizations"


def main():
    """Define the main entrypoint."""
    asyncio.run(search_all())


async def parse_summary(session, page):
    """"""
    orgs = []
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
    response = await aiohelper.fetch_json(session, SEARCH_URL, params)
    for campaign in response["campaigns"]:
        name = campaign["group"]["name"]
        slug = campaign["group"]["slug"]
        o = Organization(name, slug=slug)
        orgs.append(o)
    return orgs


async def parse_details(session, org):
    response = await aiohelper.fetch_text(session, f"{DETAILS_URL}/{org.slug}")
    regex = re.compile(fr"var org = new app.Group\((.*)\);")
    term_match = regex.search(response)
    if term_match:
        content_dict = json.loads(term_match.groups()[0])
        org.address = (
            f'{content_dict.get("address", {}).get("address1", "")}'
            "  "
            f'{content_dict.get("address", {}).get("address2", "")}'
        )
        org.city = content_dict.get("address", {}).get("city", "")
        org.state = content_dict.get("address", {}).get("state", "")
        org.state = content_dict.get("address", {}).get("state", "")
        org.zipcode = content_dict.get("address", {}).get("postal_code", "")
        org.country = content_dict.get("address", {}).get("country", "")
        org.latitude = content_dict.get("address", {}).get("latitude", 0.0)
        org.longitude = content_dict.get("address", {}).get("longitude", 0.0)
        org.contact = content_dict.get("contact", {}).get("name", "")
        org.email = content_dict.get("contact", {}).get("email", "")
        org.phone = content_dict.get("contact", {}).get("phone", "")
        org.website = content_dict.get("website", "")
        org.categories = ", ".join(
            [cause.get("name", "") for cause in content_dict.get("causes", {})]
        )
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
