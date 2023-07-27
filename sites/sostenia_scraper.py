# Scraper for Sostenia Company
# Link to company career page -> https://www.sostenia.ro/en/jobs
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

def collect_data_from_sostenia():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://www.sostenia.ro/en/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('a', class_='text-decoration-none')

    lst_with_data = []
    for sd in soup_data:
        link = "https://www.sostenia.ro" + sd['href']
        title = sd.find('h3', class_='text-secondary mt0 mb4').text.strip()
        location = sd.find('div', class_='d-flex align-items-baseline').find('span', class_='w-100 o_force_ltr d-block').text.split()[-3].replace('2', '')

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Sostenia",
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


company_name = 'Sostenia'
data_list = collect_data_from_sostenia()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Sostenia',
                  "https://www.sostenia.ro/web/image/website/1/logo/Sostenia?unique=70ec873"
                  ))



