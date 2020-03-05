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
