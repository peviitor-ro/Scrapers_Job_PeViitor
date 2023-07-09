#
#
#
# Scraper for Seimaf Company
# Link to company career page -> https://www.seimaf.com/ro/ofertele-de-locuri-de-munca/
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


def collect_data_from_seimaf():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://www.seimaf.com/ro/ofertele-de-locuri-de-munca/?fwp_job_location=bucuresti-romania', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('article', class_='card-job')
    
    lst_with_data = []
    for sd in soup_data:
        title = sd.find('h1').text.strip()
        link = sd.find('a')['href']

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Seimaf",
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


company_name = 'Seimaf'
data_list = collect_data_from_seimaf()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Seimaf',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx-Ydt01GK5sYz8vgZVEzdjCHRmRI_JpqMaM2ThyOi8A&s"
                  ))



