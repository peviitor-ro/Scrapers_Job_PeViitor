#
#
# Scraper for Tradeville Company
# Link to company career page -> https://tradeville.ro/cariere
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import re
import requests

from _county import get_county


CAREERS_URL = 'https://tradeville.ro/cariere'
PROXY_URL = 'https://r.jina.ai/http://tradeville.ro/cariere'


def collect_data_from_tradeville():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(PROXY_URL, headers=DEFAULT_HEADERS)
    soup_data = re.findall(r'^##\s+(.+)$', response.text, re.MULTILINE)

    lst_with_data =[]
    for title in soup_data:
        title = title.strip().strip('*')

        if title in {'Cine este TradeVille?', 'De ce sa deveniti colegul nostru?'}:
            break

        if ',' not in title:
            continue

        city_text = title.split(',')[-1].strip().strip('*').replace('București', 'Bucuresti')
        cities = [city_text]
        counties = list(dict.fromkeys(
            county for county in (get_county(city) for city in cities) if county
        ))

        lst_with_data.append({
            "job_title": title,
            "job_link": CAREERS_URL,
            "company": "Tradeville",
            "country": "Romania",
            "city": cities,
            "county": counties
        })

    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


if __name__ == '__main__':
    company_name = 'Tradeville'
    data_list = collect_data_from_tradeville()
    scrape_and_update_peviitor(company_name, data_list)

    print(update_logo('Tradeville',
                      "https://tradeville.ro/landing/job-assets/images/logo/logo_tradeville.png"
                      ))
