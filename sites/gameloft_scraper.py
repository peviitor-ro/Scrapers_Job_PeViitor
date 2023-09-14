#
#
#
# Scraper for Gameloft Company
# Link to company career page -> https://www.gameloft.ro/latest-jobs/
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


def construct_dict(title: str, link: str, city: str) -> dict:
    '''
    ... this function will return a dictionary to respect DRY
    '''

    dct = {
        "id": str(uuid.uuid4()),
        "job_title": title,
        "job_link": link,
        "company": "Gameloft",
        "country": "Romania",
        "city": city
    }

    return dct


def collect_data_from_gameloft():
    '''
    ... this function will collect and will return a list with jobs
    '''

    response = requests.get(url='https://careers.smartrecruiters.com/Gameloft', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('section', class_='openings-section opening opening--grouped js-group')

    lst_with_data =[]
    for sd in soup_data:
        if 'Bucharest' in sd.find('h3', class_='opening-title title display--inline-block text--default').text:
            for job in sd.find_all('li', class_='opening-job job column wide-7of16 medium-1of2'):
                link = job.find('a', class_='link--block details')['href']
                title = job.find('h4', class_='details-title job-title link--block-target').text

                lst_with_data.append(construct_dict(title=title, link=link, city='Bucuresti'))

        if 'Cluj' in sd.find('h3', class_='opening-title title display--inline-block text--default').text:
            for job in sd.find_all('li', class_='opening-job job column wide-7of16 medium-1of2'):
                link = job.find('a', class_='link--block details')['href']
                title = job.find('h4', class_='details-title job-title link--block-target').text

                lst_with_data.append(construct_dict(title=title, link=link, city='Cluj-Napoca'))

    return lst_with_data
                

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Gameloft'
data_list = collect_data_from_gameloft()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Gameloft',
                  "https://www.gameloft.ro/wp-content/uploads/2017/05/logo_gameloft_black.png"
                  ))
