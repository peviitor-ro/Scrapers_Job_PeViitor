#
#
#
# Scraper for FNT  
# Link to company career page -> https://www.fntsoftware.com/en/careers/career-opportunities
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


def collect_data_from_fnt() -> dict:
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://www.fntsoftware.com/en/careers/career-opportunities', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='link-liste')

    lst_with_data = []
    for sd in soup_data:
        link = 'https://www.fntsoftware.com/' + sd.find('a', class_='link-liste__item')['href']
        title = sd.find('a').find('span', class_='link-liste__text').text

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "FntSoftware",
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


company_name = 'FntSoftware'
data_list = collect_data_from_fnt()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('FntSoftware',
                  "https://webapps-cdn.esri.com/CDN/business-partners/00P5x00001KntphEAB"
                  ))