# Scraper for Napa Company
# Link to company career page -> https://jobs.napa.fi/jobs
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


def collect_data_from_napa():
    '''
    this function will collect all data and will return a list with available jobs
    '''

    response = requests.get(url='https://jobs.napa.fi/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('li', class_='w-full')

    lst_with_data = []
    for job in jobs:
        if 'Romania' in job.find('a').find('div', class_='mt-1 text-md').text.strip():
            link = job.find('a', class_='flex flex-col py-6 text-center sm:px-6 hover:bg-gradient-block-base-bg focus-visible-company focus-visible:rounded')['href']
            title = job.find('a').find('span', class_='text-block-base-link sm:min-w-[25%] sm:truncate company-link-style').text


            lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Napa",
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


company_name = 'Napa'
data_list = collect_data_from_napa()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Napa',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2yNohzwIV2oeULkKuy854uOcUVgcxOKFCiGg2hpH5qw&s"
                  ))
