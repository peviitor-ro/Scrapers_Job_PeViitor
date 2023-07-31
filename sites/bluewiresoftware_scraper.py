# Scraper for BlueWire Software Company
# Link to company career page -> https://careers.smartrecruiters.com/BlueWireSoftware
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

def collect_data_from_bluewire():
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://careers.smartrecruiters.com/BlueWireSoftware', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('section', class_='openings-section opening opening--grouped js-group')
    # print(soup_data)

    lst_with_data = []
    for sd in soup_data:
        for job in sd.find_all('li', class_='opening-job job column wide-7of16 medium-1of2'):
            link = job.find('a')['href']
            title = job.find('h4', class_='details-title job-title link--block-target').text

            lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Bluewiresoftware",
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


company_name = 'Bluewiresoftware'
data_list = collect_data_from_bluewire()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Bluewiresoftware',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwOHOLUCbckzh3fCqrWg8wT5wiojpV_fgg25BEodL9&s"
                  ))