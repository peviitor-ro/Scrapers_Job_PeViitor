#
#
#
# Scraper for Exiger Company
# Link to company career page -> https://www.exiger.com/careers/#Join-our-team-and-give-your-passion-purpose
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
import time

def collect_data_from_exiger() -> list[dict]:
    '''
    this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://boards.greenhouse.io/exiger', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='opening')

    lst_with_data = []
    for dt in soup_data:
        link = dt.find('a')['href'].split('/')[-1]
        title = dt.find('a').text
        location = dt.find('span', class_='location').text

        if 'Bucharest' in location:
            lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": f'https://www.exiger.com/careers/?gh_jid={link}',
                "company": "Exiger",
                "country": "Romania",
                "city": 'Bucharest'
            })
            
    return lst_with_data
 

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Exiger'
data_list = collect_data_from_exiger()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Exiger',
                  "https://www.exiger.com/wp-content/uploads/2020/08/Logo.png"
                  ))
