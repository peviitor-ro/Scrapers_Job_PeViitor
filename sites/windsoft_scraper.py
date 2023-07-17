# Scraper for Windsoft Company
# Link to company career page -> https://www.windsoft.ro/ro/cariere
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

def collect_data_from_windsoft():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://www.windsoft.ro/ro/cariere', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-4 col-lg-4 mv-20')

    lst_with_data= []
    for sd in soup_data:
        link = 'https://www.windsoft.ro' + sd.find('a')['href']
        title = sd.find('a').text
        location = sd.find('div', class_='career_location').text

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Windsoft",
            "country": "Romania",
            "city": location.capitalize()
        })

    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Windsoft'
data_list = collect_data_from_windsoft()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Windsoft',
                  "https://www.windsoft.ro/images/logo.png"
                  ))