# # Scraper for Voxility 
# # Link to company career page -> https://www.voxility.com/jobs
# #
# #
# #
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid
#
def collect_data_from_voxility():
    '''
    ... this function will collect all data and will return a list with available jobs
    '''

    response = requests.get(url='https://www.voxility.com/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='job-listing')

    lst_with_data = []
    for sd in soup_data:
        link = "https://www.voxility.com" + sd.find('a')['href'].replace('..', '')
        title = sd.find('a').text
        location = sd.find('span', class_='job-location').text.split()[-2].replace(',', '').replace('Bucharest', 'Bucuresti')
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Voxility",
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


company_name = 'Voxility'
data_list = collect_data_from_voxility()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Voxility',
                  "https://www.voxility.com/public/themes/mobile_VoxilityLogo.png"
                  ))