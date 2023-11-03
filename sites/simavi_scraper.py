#
#
#
# Scraper for Simavi Company
# Link to company career page -> https://www.simavi.ro/ro/cariere
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

def collect_data_from_simavi():
    '''
    ... this function will collect data and will retrieve a list with jobs
    '''

    response = requests.get(url='https://www.simavi.ro/ro/cariere', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='views-row col-md-4')

    lst_with_data = []
    for sd in soup_data:
        link = 'https://www.simavi.ro' + sd.find('a')['href']
        title = sd.find('span', class_='field field--name-title field--type-string field--label-hidden').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Simavi",
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


company_name = 'Simavi'
data_list = collect_data_from_simavi()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Simavi',
                  "https://www.simavi.ro/sites/default/files/2018-07/logo-construction_0.png"
                  ))
