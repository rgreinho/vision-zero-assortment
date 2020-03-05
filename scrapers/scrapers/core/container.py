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
#
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
# amplify austin
#
# {
#   "id": 459892,
#   "cb_cover_photo": "https://www.givegab.com/images/fallback/cover-photo-3.jpg",
#   "claimed": true,
#   "collect_donor_address": false,
#   "dashboard_logo": "https://user-content.givegab.com/uploads/group/logo/459892/dashboard_7b8bf56d19a727d5c63b820456dc4cd302c6b13c.png",
#   "description": "Our vision is a world without Alzheimer's Disease",
#   "donatable": true,
#   "ein": "13-3039601",
#   "has_bank_account": true,
#   "logo": "https://user-content.givegab.com/uploads/group/logo/459892/7b8bf56d19a727d5c63b820456dc4cd302c6b13c.png",
#   "name": "Alzheimer's Association Capital of Texas Chapter",
#   "slug": "alzheimer-s-association-capital-of-texas-chapter",
#   "website": "http://www.alz.org/texascapital",
#   "who_we_are": "alzheimer's, alzheimers, dementia, geriatric, elderly care, caregivers, family, community, resources, support, support groups, education, alzheimer's association, memory, memories, families, educate, alz, alzheimer, alzhiemer's, alzhiemers, forgetting, memory loss, aging, care",
#   "group_dog": {
#     "id": 52111,
#     "approval_status": "approved",
#     "visible": true
#   },
#   "registered_for_dog": true,
#   "address": {
#     "id": 931175,
#     "address1": "5508 West Hwy 290 ",
#     "address2": "#206",
#     "city": "Austin",
#     "state": "Texas",
#     "postal_code": "78735",
#     "country": "United States",
#     "latitude": 30.2378217,
#     "longitude": -97.841602,
#     "venue": null
#   },
#   "campaign": {
#     "allow_p2p_campaigns": true,
#     "collect_donor_address": false,
#     "cover_photo_url": "https://user-content.givegab.com/uploads/campaign/cover_photo/60445/f66d2c582a1d4cdc5d6c3d35e72c9821be57d7c7.png",
#     "fundraise_link": "https://www.givegab.com/user_campaigns/new?campaign_id=60445",
#     "goal": 2000000,
#     "has_profile": true,
#     "percent_raised": 5,
#     "start_date": "2020-01-20T00:00:00.000-05:00",
#     "story": "\\u003cp\\u003e\\u003cfont color=\"#311873\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eOur organization's commitment to providing support to those individuals is sometimes hindered by the lack of resources to reach the sheer volume of those who need our help. We are especially committed to providing our services to the most rural and under-served communities at no cost.\\u0026nbsp; Thanks to a grant from St. David's Foundation we will now be able to hire a mobile Care Consultant who's role will be to help with care planning with families in the Central Texas community.\\u0026nbsp; \\u0026nbsp;This position will be mobile to achieve the goal of meeting of the needs of those who need us the most.\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003ch3\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eMission Statement\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/h3\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eOur mission is to eliminate Alzheimer's disease through the advancement of research; to provide and enhance care and support for all affected; and to reduce the risk of dementia through the promotion of brain health. Help us fund respite relief for caregivers through AmplifyATX!\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003ch3\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eNeeds Statement\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/h3\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eWe will use funds raised through Amplify Austin to offer RESPITE RELIEF to those caring for people with Alzheimer's Disease.\r\n\r\nBeing a full-time caregiver to someone with Alzheimer's can be one of the most difficult and stressful jobs imaginable. Respite provides relief to people who are caring for individuals with Alzheimer's disease or a related dementia. Time away from caregiving responsibilities is essential to the well-being of caregivers. Respite care helps to reduce stress and improve the quality of life and quality of care provided by caregivers.\\u0026nbsp; \\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eDETAILS:\r\nWe're aiming high -- Help us raise $20,000 to sponsor 80 individual caregivers for up to $250 worth of respite relief! We will prioritize our reach based on funding to focus on counties with a high senior population and a high percentage of individuals living below poverty lines: Bell; Hays; Travis; Robertson and Williamson Counties. However, should funding permit, we hope to be able to help as many of those who request the help. If we're successfully funded, each qualified participant could receive up to $250 towards respite care, paid directly to the service provider, facility of center of their choice. \r\n\r\nApplicant will be responsible for identifying and selecting the company they'd like to use. The scholarship can cover the following types of respite:   \r\n- In-home care services \r\n- Adult day centers \r\n- Residential facilities \r\n\r\n$250 = 1 stipend for 1 caregiver (if funds allow)\r\n$125 (and up) = 1 overnight stay at a respite facility*\r\n$60 (and up) = 1 day at a day care center*\r\n$20 (and up) = 1 hour of care at home*\r\n* prices vary depending on facility and service provider\r\n\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003e\r\nELIGIBILITY\\u0026nbsp;\\u003c/span\\u003e\\u003c/font\\u003e\\u003cspan style=\"color: rgb(49, 24, 115); font-family: Tahoma;\"\\u003eREQUIREMENTS:   \r\n- The person must have a diagnosis of dementia, and the caregiver must live in the same home as the person with dementia. \r\n- Service must be provided in the area in which the person with dementia resides. \r\n\r\nApplication and more information will be posted on alz.org/texascapital.\\u003c/span\\u003e\\u003c/p\\u003e\\u003ch3\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eTestimonials\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/h3\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003e\"We wanted to get involved with the Alzheimer's Association to help raise awareness for a disease that affects so many people. As a caregiver, and I wanted a place that provided information and resources for those affected by all Alzheimer's. The Alzheimer's Association has been a tremendous support to our family. We hope that our participation will in some way help to find the cure to end this disease.\" - Debbie, Georgetown\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003e\r\n\r\n\"I have early onset Alzheimer's disease and my diagnosis came as a total shock to me.  I was only 60 years young, enjoying life and looking forward to retirement after my wonderful 30 year career with the same company.  The fact is though that \"Alzheimer's has no boundaries\" and we must cure this disease. We are so grateful for the Alzheimer's Association support.\" - Sharon, Austin\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003e\r\n\r\n\"I support the Alzheimer's Association because my mother was a wonderful, loving soul whose life was torn apart by the ravages of Alzheimer's, and she remained a positive and happy person because of the love and understanding she received from excellent caregivers. I want to help find a way to eliminate Alzheimer's so others don't have to go through what she did!\" - Jill, Belton\r\n\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e\\u003ch3\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eVolunteer Details\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/h3\\u003e\\u003cp\\u003e\\u003cfont color=\"#311873\" face=\"Tahoma\"\\u003e\\u003cspan style=\"font-size: 14px;\"\\u003eOur volunteers are passionate, inspired and want to make a difference in the fight against Alzheimer's disease. Whether you can spare a few hours a week or can make a more significant time commitment, please consider becoming an Alzheimer's Association volunteer.\r\nIf you are an individual (teen, adult or senior) or part of a family, team, group of employees or company, please contact us at capitaloftexas@alz.org to see where your skills are needed. We can use your help in the following areas:\r\n\r\nSpecial events, such as galas and other fundraisers\r\nWalk to End Alzheimer's \r\nPublic education and awareness programs\r\nOffice help \r\nSpeaking engagements  \r\nHelpline support calls \r\nAdvocacy\r\n\r\nContact our office at 512-592-0990 if you are interested in being a volunteer for the Alzheimer's Association\\u003c/span\\u003e\\u003c/font\\u003e\\u003c/p\\u003e",
#     "story_image_url": "https://www.givegab.com/images/fallback/story-image-default.png",
#     "tagline": "Our vision is a world without Alzheimer's Disease",
#     "url": "https://www.givegab.com/campaigns/amplify-austin-day-61dbc1eb-17be-4f63-b349-e2504b51e265",
#     "video_embed_code": null,
#     "publication_status": "draft",
#     "id": 60445,
#     "dog_campaign": true,
#     "dog_id": 510,
#     "group": {
#       "donatable": true,
#       "id": 459892,
#       "logo_url": "https://user-content.givegab.com/uploads/group/logo/459892/7b8bf56d19a727d5c63b820456dc4cd302c6b13c.png",
#       "name": "Alzheimer's Association Capital of Texas Chapter",
#       "slug": "alzheimer-s-association-capital-of-texas-chapter"
#     },
#     "group_id": 459892,
#     "highlight": false,
#     "slug": "amplify-austin-day-61dbc1eb-17be-4f63-b349-e2504b51e265",
#     "title": "Amplify Austin Day"
#   },
#   "contact": {
#     "id": 349815,
#     "name": "",
#     "phone": "",
#     "email": "capitaloftexas@alz.org"
#   },
#   "causes": [
#     {
#       "id": 58,
#       "name": "Health and Wellness",
#       "image": "https://user-content.givegab.com/uploads/recommendation_attribute/picture/58/6d3bf649a6a60d4b7b79ba3812836e1b27fc8d6e.png",
#       "description": "You are not a hypochondriac or even a yoga fanatic, but you do have a deep interest in the eradication of illness and the promotion of nutrition and healthy living.",
#       "order": 10
#     },
#     {
#       "id": 4288,
#       "name": "Seniors",
#       "image": "https://user-content.givegab.com/uploads/recommendation_attribute/picture/4288/09a65c6dffdacc789c6354b969e0f3016c7fd6ea.png",
#       "description": "Whether it's having a conversation with an elderly person on a bench or volunteering in a senior living facility, you're eager to help seniors live and age with dignity and care. ",
#       "order": 3
#     },
#     {
#       "id": 70,
#       "name": "Education",
#       "image": "https://user-content.givegab.com/uploads/recommendation_attribute/picture/70/5a269b1dda104859e031f336d6465d456c1449c7.png",
#       "description": "There's no shortage of problems with our education system, and you're excited about diving in and making sure that students get the skills \\u0026 resources that they need to succeed.",
#       "order": 35
#     }
#   ]
# }
