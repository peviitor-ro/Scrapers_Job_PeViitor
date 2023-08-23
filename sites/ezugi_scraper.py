#
#
#
# Scraper for Ezugi Company
# Link to company career page -> https://careers.ezugi.com/jobs
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


def collect_data_from_ezugi():
    '''
    ... this function will collect all data and will return a list with  jobs
    '''
    response = requests.get(url='https://careers.ezugi.com/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('li', class_='w-full')
    
    lst_with_data = []
    for sd in soup_data:
        link = sd.find('a', class_='flex flex-col py-6 text-center sm:px-6 hover:bg-gradient-block-base-bg focus-visible-company focus-visible:rounded')['href']
        title = sd.find('span', class_='text-block-base-link sm:min-w-[25%] sm:truncate company-link-style').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Ezugi",
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


company_name = 'Ezugi'
data_list = collect_data_from_ezugi()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Ezugi',
                  "https://images.teamtailor-cdn.com/images/s3/teamtailor-production/logotype-v3/image_uploads/34b2d2c3-89da-4697-a57c-78cabbc1d793/original.png"
                  ))