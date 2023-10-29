# Scraper for Expressoft Company
# Link to company career page -> https://expressoft.ro/cariere/
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

def collect_data_from_expressoft():
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://expressoft.ro/cariere/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    jobs = soup.find_all('div', class_='accordion-item job')

    # print(jobs)

    lst_with_data =[]
    for job in jobs:
        link = job.find('div', class_='accordion-more job__more').find('a')['href']
        title = job.find('div', class_='job__title accordion-title').text
        # print(title, link)

        lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Expressoft",
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


company_name = 'Expressoft'
data_list = collect_data_from_expressoft()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Expressoft',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCSaup6KyvWosB-umVxAjMtgoub9RC_UA89DfFxqkd&s"
                  ))