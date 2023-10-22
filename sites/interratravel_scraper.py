# Scraper for Interra Company
# Link to company career page -> https://www.interra.ro/angajari/
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

def collect_data_from_interra():
    '''
    ... this function will collect all data and will return a list with available jobs
    '''
    response = requests.get(url='https://www.interra.ro/angajari/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('div', class_='box-offer mb-3')


    lst_with_data = []
    for job in jobs:
        link = job.find('div', class_='listing-description').find('a')['href']
        title = job.find('div', class_='listing-description').find('a').find('h2').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "InterraTravel",
                "country": "Romania",
                "city": "Romania"
            })
    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'InterraTravel'
data_list = collect_data_from_interra()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('InterraTravel',
                  "https://www.interra.ro/img/main-logo.svg"
                  ))
