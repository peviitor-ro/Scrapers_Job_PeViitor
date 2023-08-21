# Scraper for Hennlich Company
# Link to company career page -> https://www.hennlich.ro/cariera/toate-locurile-de-munca.html
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

def collect_data_from_hennlich():
    '''
    ... this function will collect all data and will return a list with available jobs
    '''
    response = requests.get(url='https://www.hennlich.ro/cariera/toate-locurile-de-munca.html', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('li', class_='list_item list-group-item')

    lst_with_data = []
    for sd in soup_data:
        link = 'https://www.hennlich.ro' + sd.find('a')['href']
        title = sd.find('a').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Hennlich",
            "country": "Romania",
            "city": 'Romania'
        })
    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Hennlich'
data_list = collect_data_from_hennlich()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Hennlich',
                  "data:image/png;base64,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"
                  ))