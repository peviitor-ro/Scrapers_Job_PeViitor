# Scraper for Webasto Company
# Link to company career page -> https://jobs.webasto.com/search/?q=&q2=&alertId=&title=&location=RO&shifttype=&date=&department=
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

def collect_data_from_webasto():
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://jobs.webasto.com/search/?q=&q2=&alertId=&title=&location=RO&shifttype=&date=&department=', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('tr', class_='data-row')

    lst_with_data = []
    for job in jobs:
        link = 'https://jobs.webasto.com' + job.find('span', class_='jobTitle hidden-phone').find('a')['href']
        title = job.find('span', class_='jobTitle hidden-phone').find('a').text

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Webasto",
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


company_name = 'Webasto'
data_list = collect_data_from_webasto()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Webasto',
                  "https://logovtor.com/wp-content/uploads/2019/10/webasto-logo-vector.png"
                  ))