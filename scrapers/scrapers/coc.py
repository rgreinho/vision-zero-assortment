import asyncio
import dataclasses

import aiohttp

from scrapers.core import aiohelper
from scrapers.core import container


def main():
    """Define the main entrypoint."""
    asyncio.run(search_all())


def parse_entry(entry):
    org = container.Organization(entry["title"])
    org.address = (
        f'{entry.get("address", "").get("street1", "")}'
        " "
        f'{entry.get("address", "").get("street2", "")}'
    )
    org.city = entry.get("address", "").get("city", "")
    org.state = entry.get("address", "").get("state", "")
    org.zipcode = entry.get("address", "").get("zip", "")
    org.country = entry.get("address", "").get("country", "")
    org.latitude = entry.get("address", "").get("lat", 0.0)
    org.longitude = entry.get("address", "").get("lng", 0.0)
    org.phone = entry.get("phone", "")
    org.website = entry.get("webUrl", "")
    org.categories = ", ".join(
        [cause.get("title", "") for cause in entry.get("category", {})]
    )
    org.slug = entry.get("slug", "")
    return org


async def search_all():
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        url = "https://www.austinchamber.com/api/v1/directory"

        def params(page):
            return {
                "filter[categories]": "",
                "filter[show]": "all",
                "page": page,
                "limit": 24,
            }

        tasks = [
            aiohelper.fetch_json(session, url, params(page)) for page in range(0, 131)
        ]
        page_res = await asyncio.gather(*tasks)
        full_orgs = [org for orgs in page_res for org in orgs.get("data", {})]
        result = [parse_entry(org) for org in full_orgs if org.get("title")]
        container.orgs2csv("coc.csv", result)


if __name__ == "__main__":
    main()


# Austrin chamber of commerce
#
# {
#   "id": "51259",
#   "title": "TeamLogic IT of East Austin",
#   "slug": "teamlogic-it-of-east-austin",
#   "tier": {
#     "id": 3,
#     "handle": "build",
#     "name": "Build"
#   },
#   "directoryDescription": null,
#   "address": {
#     "street1": "9800 N Lamar Blvd",
#     "street2": "Ste 210",
#     "city": "Austin",
#     "state": "TX",
#     "zip": "78753",
#     "country": "United States",
#     "lat": "30.36798210",
#     "lng": "-97.69491910",
#     "mapApiKey": "AIzaSyDMI3DyyBwTwZRcbQsqv5JxcQp0ZzqqVGY"
#   },
#   "phone": "512.501.1077",
#   "webUrl": "https://www.teamlogicit.com/neAustinTX",
#   "organizationLogo": null,
#   "social": {
#     "facebook": "",
#     "twitter": "",
#     "instagram": "",
#     "linkedin": ""
#   },
#   "category": [
#     {
#       "id": "323",
#       "title": "Computers, IT & Technology",
#       "slug": "computers-it-technology",
#       "level": "1"
#     },
#     {
#       "id": "148",
#       "title": "IT Managed Services",
#       "slug": "it-managed-services",
#       "level": "2"
#     }
#   ]
# }
#
