# Scraper for Neo Vision Company
# Link to company career page -> https://neovision.dev/careers/
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


def collect_data_from_neovision():
    '''
    this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://neovision.dev/careers/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='careers-openings-item')

    lst_with_data = []
    for sd in soup_data:
        link = sd.find('a')['href']
        title = sd.find('span', class_='button-casestudy-text text-h2').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "NeoVision",
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


company_name = 'NeoVision'
data_list = collect_data_from_neovision()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('NeoVision',
                  "https://www.highcontrast.ro/wp-content/uploads/2020/12/Neo-Vision-2.png"
                  ))

