#
#
#
# Scraper for EEU Software Company
# Link to company career page -> https://www.eeusoft.ro/ro/category/cariere
# https://careers.smartrecruiters.com/EEUSoftware
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

def collect_data_from_eeusoftware():
    '''
    ... this function collects all data and returns a list with available jobs
    '''

    response = requests.get(url='https://careers.smartrecruiters.com/EEUSoftware', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('li', class_='opening-job job column wide-7of16 medium-1of2')

    lst_with_data = []
    for sd in soup_data:
        title = sd.find('h4', class_='details-title job-title link--block-target').text
        link = sd.find('a', class_='link--block details')['href']

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "EEUSoftware",
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


company_name = 'EEUSoftware'
data_list = collect_data_from_eeusoftware()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('EEUSoftware',
                  "https://www.eeusoft.ro/ro/wp-content/themes/eeutheme/images/logoEEU.svg"
                  ))



