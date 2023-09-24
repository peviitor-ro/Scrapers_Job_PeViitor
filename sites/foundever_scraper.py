# Scraper for Foundever Company
# Link to company career page -> https://jobs.foundever.com/go/Jobs-in-Romania/9236600/
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

def collect_data_from_foundever():
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://jobs.foundever.com/go/Jobs-in-Romania/9236600/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('tr', class_='data-row')
    

    lst_with_data = []
    for sd in soup_data:
        link = 'https://jobs.foundever.com' + sd.find('span', class_='jobTitle hidden-phone').find('a')['href']
        title = sd.find('span', class_='jobTitle hidden-phone').find('a').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Foundever",
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


company_name = 'Foundever'
data_list = collect_data_from_foundever()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Foundever',
                  "data:image/png;base64,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"
                  ))