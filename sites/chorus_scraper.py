#
#
#
# Scraper for Chorus Electric Company
# Link to company career page -> https://www.chorus.ro/job_list
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

def collect_data_from_chorus():
    '''
    ... this function will collect data and will retrieve a list with jobs
    '''
    response = requests.get(url='https://www.chorus.ro/job_list', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('ul', class_='descr')

    lst_with_data =[]
    for sd in soup_data:
        for job in sd.find_all('li'):
            link = job.find('a')['href'].strip()
            title = job.find('a').text.strip()

            lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Chorus",
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


company_name = 'Chorus'
data_list = collect_data_from_chorus()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Chorus',
                  "https://www.chorus.ro/images/design/logo.png"
                  ))
