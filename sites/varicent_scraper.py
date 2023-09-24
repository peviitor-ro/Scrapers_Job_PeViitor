#
#
#
# Scraper for Varicent Company
# Link to company career page -> https://www.varicent.com/company/careers
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
#
import uuid


def get_headers() -> str:
    '''
    ... get headers from site and search for ID if none matches
    '''

    response = requests.head(url='https://www.varicent.com/company/careers', headers=DEFAULT_HEADERS).headers

    return response['ETag']


def get_prepare_post_request() -> tuple:
    '''
    ... prepare headers for get request with a special ETag
    '''
    url= 'https://api.lever.co/v0/postings/varicent?mode=json'

    headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ro-RO;q=0.8,ro;q=0.7',
            'Connection': 'keep-alive',
            'If-None-Match': f'{get_headers()}',
            'Origin': 'https://www.varicent.com',
            'Referer': 'https://www.varicent.com/company/careers',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
    }
    
    return url, headers


def get_data_from_varicent():
    '''
    ... will call the API using new headers
    '''
    data = get_prepare_post_request()
    response = requests.get(url=data[0], headers=data[1]).json()

    lst_with_data = []
    for sd in response:
        link_id = sd["id"]
        title = sd['text']
        location = sd['categories']['location']

        if 'Bucharest' in location:
            lst_with_data.append({
                            "id": str(uuid.uuid4()),
                            "job_title": title,
                            "job_link": f'https://jobs.lever.co/varicent/{link_id}',
                            "company": "Varicent",
                            "country": "Romania",
                            "city": "Bucuresti"
            })

    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Varicent'
data_list = get_data_from_varicent()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Varicent',
                  "https://www.varicent.com/hubfs/Varicent-Screen-FullColor.svg"
                  ))
