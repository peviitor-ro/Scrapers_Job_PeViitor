#
#
#
# Scraper for Kenvue Company
# Link to company career page -> https://kenvue.taleo.net/careersection/2/jobsearch.ftl?_gl=1*z3fgw4*_ga*OTYzMDQ4NzY4LjE2ODg0OTgxMjQ.*_ga_C9CY922645*MTY4ODQ5ODEyNC4xLjEuMTY4ODQ5ODE0Ni4zOS4wLjA.
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid


def prepare_post_request() -> tuple:
    '''
    ... creating headers for post request
    ''' 
    url = 'https://kenvue.taleo.net/careersection/rest/jobboard/searchjobs?lang=en&portal=101430233'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,ro-RO;q=0.8,ro;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'locale=en; _ga=GA1.1.963048768.1688498124; _ga_C9CY922645=GS1.1.1688498124.1.1.1688498147.38.0.0; OptanonAlertBoxClosed=2023-07-04T19:15:47.305Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jul+04+2023+22%3A15%3A47+GMT%2B0300+(Eastern+European+Summer+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=6bda047b-e19c-429e-a5e6-ae72f79d82e3&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1&AwaitingReconsent=false',
        'Origin': 'https://kenvue.taleo.net',
        'Referer': 'https://kenvue.taleo.net/careersection/2/jobsearch.ftl?_gl=1*1w74hxb*_ga*OTYzMDQ4NzY4LjE2ODg0OTgxMjQ.*_ga_C9CY922645*MTY4ODQ5ODEyNC4xLjEuMTY4ODQ5ODEzMy41Mi4wLjA.',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': "?0'",
        'sec-ch-ua-platform': '"Windows"',
        'tz': 'GMT+03:00',
        'tzname': 'Europe/Bucharest'
    }

    data = {
        "multilineEnabled": True,
        "sortingSelection": {
            "sortBySelectionParam": "3",
            "ascendingSortingOrder": "false"
        },
        "fieldData": {
            "fields": {
                "KEYWORD": "",
                "LOCATION": "1493840260991",
                "CATEGORY": ""
            },
            "valid": True
        },
        "filterSelectionParam": {
            "searchFilterSelections": [
                {
                    "id": "POSTING_DATE",
                    "selectedValues": []
                },
                {
                    "id": "LOCATION",
                    "selectedValues": []
                },
                {
                    "id": "JOB_FIELD",
                    "selectedValues": []
                }
            ]
        },
        "advancedSearchFiltersSelectionParam": {
            "searchFilterSelections": [
                {
                    "id": "ORGANIZATION",
                    "selectedValues": []
                },
                {
                    "id": "LOCATION",
                    "selectedValues": []
                },
                {
                    "id": "JOB_FIELD",
                    "selectedValues": []
                },
                {
                    "id": "JOB_NUMBER",
                    "selectedValues": []
                },
                {
                    "id": "URGENT_JOB",
                    "selectedValues": []
                },
                {
                    "id": "STUDY_LEVEL",
                    "selectedValues": []
                },
                {
                    "id": "WILL_TRAVEL",
                    "selectedValues": []
                }
            ]
        },
        "pageNo": 1
    }

    return url, headers, data


def collect_data_from_kenvue():
    '''
    ... returns data with post request
    '''
    data = prepare_post_request()
    response = requests.post(url=data[0], headers=data[1], json=data[2]).json()
    
    lst_with_data = []
    for item in response['requisitionList']:
        title = item['column'][0]
        link = item['column'][2]
        location = item['column'][1].split('-')[-1].replace('"]', '')

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": f'https://kenvue.taleo.net/careersection/2/jobdetail.ftl?job={link}&tz=GMT%2B03%3A00&tzname=Europe%2FBucharest',
            "company": "Kenvue",
            "country": "Romania",
            "city": location
        })

    return lst_with_data
    

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Kenvue'
data_list = collect_data_from_kenvue()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Kenvue',
                  "https://kenvue.taleo.net/careersection/theme/1081641/1687871269000/en/theme/images/Kenvue_logo_black.png"
                  ))
