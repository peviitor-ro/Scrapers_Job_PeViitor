#
#
#
# Scraper for Siveco Company
# Link to company career page -> http://www.siveco.ro/en/about-siveco-romania/careers
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


def collect_data_from_siveco():
    '''
    ... this function will collect data and will return a list with available jobs
    '''

    response = requests.get(url='http://www.siveco.ro/en/about-siveco-romania/careers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    lst_with_data = []
    for sd in soup.find_all('span', class_='field-content'):
        link = "http://www.siveco.ro" + sd.find('a')['href']
        title = sd.find('a').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Siveco",
            "country": "Romania",
            "city": "Romania"
        })

    return lst_with_data[:-2]


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Siveco'
data_list = collect_data_from_siveco()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Siveco',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTseBFM6IikvyVvUG4SPYluW8G090IqQfhl3yMlzDBC&s"
                  ))

