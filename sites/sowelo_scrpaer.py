#
#
#
# Scraper for Sowelo Company
# Link to company career page -> https://sowelo.eu/job-offers/
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


def return_lst_dict(title: str, link: str, city: str) -> dict:
    '''
    ... this function will return a dict to append to a list and avoid DRY
    '''
    dct = {
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Sowelo",
                "country": "Romania",
                "city": city
            }
    
    return dct


def collect_data_from_sowelo():
    '''
    ... this function will collect data and will return a list with jobs
    '''

    response = requests.get(url='https://soweloconsulting.applytojob.com/apply/jobs', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    lst_with_data = []

    soup_data_1 = soup.find_all('tr', class_='resumator_odd_row')
    for sd_1 in soup_data_1:
        link_1 = 'https://soweloconsulting.applytojob.com' + sd_1.find('td').find('a', class_='job_title_link')['href']
        title_1 = sd_1.find('td').find('a', class_='job_title_link').text
        city_1 = sd_1.find_all('td')[-1].text.strip()

        if 'Romania' in city_1:
            lst_with_data.append(return_lst_dict(title=title_1, link=link_1, city=city_1.split()[0].replace(',','')))

    soup_data_2 = soup.find_all('tr', class_='resumator_even_row')
    for sd_2 in soup_data_2:
        link_2 = 'https://soweloconsulting.applytojob.com' + sd_2.find('td').find('a', class_='job_title_link')['href']
        title_2 = sd_2.find('td').find('a', class_='job_title_link').text
        city_2 = sd_2.find_all('td')[-1].text.strip()
        
        if 'Romania' in city_2:
            lst_with_data.append(return_lst_dict(title=title_2, link=link_2, city=city_2.split()[0].replace(',','')))

    return lst_with_data

    
@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Sowelo'
data_list = collect_data_from_sowelo()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Sowelo',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvjHLNHWH9V7VQ3qOP8EP-xqnvwSICQsjlsX7vfFswjQ&s"
                  ))
