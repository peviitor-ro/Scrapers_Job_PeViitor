#
#
#
# Scraper for Vevohub Company
# Link to company career page -> https://vevohub.com/careers/
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid

def collect_data_from_vevohub():
    ''''
    ... this func will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://vevohub.com/careers/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='elementor-flip-box')

    lst_with_data = []
    for sd in soup_data:
        link = sd.find('a', class_='elementor-flip-box__button elementor-button elementor-size-md')['href']
        title = sd.find('h3', class_='elementor-flip-box__layer__title').text.strip()

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Vevohub",
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


company_name = 'Vevohub'
data_list = collect_data_from_vevohub()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Vevohub',
                  "https://vevohub.com/wp-content/uploads/2023/05/FullLogo_Transparent_NoBuffer-1-1.png"
                  ))
