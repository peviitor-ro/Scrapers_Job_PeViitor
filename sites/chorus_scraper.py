#
#
#
# Scraper for Chorus Electric Company
# Link to company career page -> https://www.chorus.ro/job_list
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#

from _county import get_county


def collect_data_from_chorus():
    '''
    ... this function will collect data and will retrieve a list with available jobs
    '''
    response = requests.get(
        url='https://www.chorus.ro/Careers/Careers', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='card-body')

    lst_with_data =[]
    for sd in soup_data:
        job_title = sd.find('h5', class_='card-title').text.strip()
        job_link = f"https://www.chorus.ro{sd.find_all('a', class_='card-link')[-1]['href'].strip()}"
        cities = [city.strip() for city in sd.find('h6', class_='card-subtitle').text.split(',') if city.strip()]
        counties = list(dict.fromkeys(
            county for county in (get_county(city) for city in cities) if county
        ))


        lst_with_data.append({
            "job_title": job_title,
            "job_link": job_link,
            "company": "Chorus",
            "country": "Romania",
            "city": cities,
            "county": counties
        })

    return lst_with_data

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """
    return data_list


if __name__ == '__main__':
    company_name = 'Chorus'
    data_list = collect_data_from_chorus()
    scrape_and_update_peviitor(company_name, data_list)

    print(update_logo('Chorus',
                      "https://www.chorus.ro/images/design/logo.png"
                      ))
