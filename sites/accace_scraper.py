# Scraper for Accace Company
# Link to company career page -> https://accace.ro/cariere/#oportunitati
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


def collect_data_from_accace() -> list[dict]:
    '''
    this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://accace.ro/cariere/#oportunitati', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='col-md-4 col-sm-6 grid-item')

    lst_with_data = []
    for sd in soup_data:
        link = sd.find('a')['href']
        title = sd.find('span', class_='job-title').text

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Accace",
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


company_name = 'Accace'
data_list = collect_data_from_accace()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Accace',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLWhYB0zYG3AXTmVINv3O060D8nnNl2fIUB5FF9xVf&s"
                  ))
