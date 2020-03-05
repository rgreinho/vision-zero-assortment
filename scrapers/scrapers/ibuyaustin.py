import asyncio
import dataclasses

import aiohttp

from scrapers.core import aiohelper
from scrapers.core import container


def main():
    """Define the main entrypoint."""
    asyncio.run(search_all())


def parse_entry(entry):
    org = container.Organization(entry["organization"])
    org.address = entry.get("address", "")
    org.city = entry.get("city", "")
    org.state = entry.get("state", "")
    org.zipcode = entry.get("zip", "")
    org.country = entry.get("country", "")
    org.latitude = entry.get("glat", 0.0)
    org.longitude = entry.get("glong", 0.0)
    org.contact = f'{entry.get("first_name", "")} {entry.get("last_name", "")}'
    org.email = entry.get("email", "")
    org.phone = entry.get("phone", "")
    org.website = entry.get("website", "")
    org.categories = entry.get("custom_field_1", "")
    org.description = entry.get("summary", "")
    return org


async def search_all():
    async with aiohttp.ClientSession() as session:
        url = "https://widget.apricotmaps.com/p/NDgyMzY4MTQ=/scripts/genjson.php"
        params = dict(
            pln="p",
            acct="48236814",
            bCategory="all",
            bType="all",
            company_name="",
            bAll="Yes",
        )
        results = await aiohelper.fetch_json(session, url, params)
        orgs = [parse_entry(org) for org in results if org.get("organization")]
        container.orgs2csv("ibuyaustin.csv", orgs)


if __name__ == "__main__":
    main()

# ibuyaustin
# {
#     "memid": "50427540",
#     "first_name": "",
#     "last_name": "",
#     "organization": "Zucchini Kill Bakery",
#     "address": "701 E. 53rd St.",
#     "city": "Austin",
#     "state": "TX",
#     "zip": "78751",
#     "country": "",
#     "email": "jessica@zucchinikill.com",
#     "phone": "737-215-5936",
#     "website": "http://www.zucchinikill.com",
#     "summary": "Punk rock, female-led bakery serving vegan sweet & savory goods that are also soy & gluten-free.",
#     "photo": "",
#     "status": "Active",
#     "level": "962753",
#     "md5email": "0c83f57c786a0b4a39efab23731c7ebc",
#     "glat": "30.3152767",
#     "glong": "-97.7166469",
#     "custom_field_1": "ENTERTAINMENT & DINING: Coffeehouses & Bakeries",
#     "custom_field_2": "",
#     "custom_field_3": "Premiere IBIZ Merchant",
#     "custom_field_4": "North Loop",
#     "custom_field_5": "Suite C"
#   }
