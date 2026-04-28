#
#
#
# Scraper for Tenaris Company
# Link to company career page -> https://careers.smartrecruiters.com/Tenaris1
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


def collect_data_from_tenaris():
    '''
    ... this function will collect all data and will return a list with jobs
    '''
    response = requests.get(url='https://careers.smartrecruiters.com/Tenaris1', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('section', class_='openings-section opening opening--grouped js-group')

    lst_with_data = []
    for sd in soup_data:
        city_text = sd.find('h3', class_='opening-title').text.split(',')[0].strip()
        cities = [city_text]
        counties = list(dict.fromkeys(
            county for county in (get_county(city) for city in cities) if county
        ))

        for job in sd.find_all('li', class_='opening-job job column wide-7of16 medium-1of2'):
            link = job.find('a', class_='link--block details js-job-ad-link')['href']
            title = job.find('h4', class_='details-title job-title link--block-target').text.strip()

            lst_with_data.append({
                "job_title": title,
                "job_link": link,
                "company": "tenaris",
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
    company_name = 'tenaris'
    data_list = collect_data_from_tenaris()
    scrape_and_update_peviitor(company_name, data_list)

    print(update_logo('tenaris',
                      "https://logowik.com/content/uploads/images/tenaris9552.logowik.com.webp"
                      ))
