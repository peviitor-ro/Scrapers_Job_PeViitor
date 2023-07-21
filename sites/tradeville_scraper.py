#
#
# Scraper for Tradeville Company
# Link to company career page -> https://tradeville.ro/landing/jobs
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


def collect_data_from_tradeville():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://tradeville.ro/landing/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('a', class_='job-list row')

    lst_with_data =[]
    for sd in soup_data:
        link = 'https://tradeville.ro/landing/' + sd['href']
        title = sd.find('div', class_='content col').find('h6', class_='title').text.replace('â\x80\x93', '')
        location = sd.find('ul', class_='meta').text.split()[1].replace(',','')

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Tradeville",
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


company_name = 'Tradeville'
data_list = collect_data_from_tradeville()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Tradeville',
                  "https://tradeville.ro/landing/job-assets/images/logo/logo_tradeville.png"
                  ))

