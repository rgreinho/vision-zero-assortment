import csv
import dataclasses


@dataclasses.dataclass
class Organization:
    name: str
    website: str = ""
    email: str = ""
    address: str = ""
    city: str = ""
    state: str = ""
    zipcode: str = ""
    country: str = ""
    phone: str = ""
    contact: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    description: str = ""
    categories: str = ""
    slug: str = ""


def orgs2csv(filename, orgs):
    fieldnames = dataclasses.asdict(Organization("name")).keys()
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for org in orgs:
            writer.writerow(dataclasses.asdict(org))
