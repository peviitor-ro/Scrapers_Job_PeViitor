# Scraper for Medihelp Company
# Link to company career page -> https://www.medihelp.ro/misiunea-medihelp/cariere
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


def collect_data_from_medihelp():
    '''
    this function will collect all data and will return a list with  jobs
    '''

    response = requests.get(url='https://www.medihelp.ro/misiunea-medihelp/cariere', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('div', class_='row mt-4 mt-md-5')

    lst_with_data = []
    for job in jobs:
        link ='https://www.medihelp.ro' + job.find('a', class_='buton-albastru')['href']
        title = job.find('div', class_='col-10').find('h5', class_='titlu-job').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Medihelp",
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


company_name = 'Medihelp'
data_list = collect_data_from_medihelp()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Medihelp',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnXhpivlxLppDoCJZSjTLwIoIrZAU9fybVjQkOWw_7_A&s"
                  ))