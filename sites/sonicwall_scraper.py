#
#
#
# Scraper for SonicWall Company
# Link to company career page -> https://www.sonicwall.com/about-sonicwall/careers/#open-positions
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


def return_lst_dict(title: str, link: str, location: str) -> dict:
    '''
    ... this function will return a dict to append to a list and avoid DRY
    '''
    dct = {
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "Sonicwall",
                "country": "Romania",
                "city": location
            }
    
    return dct


# let's get scrape the data!
def collect_data_from_sonicwall():
    '''
    ... this function will collect data and will return a list with available jobs
    '''

    response = requests.get(url='https://boards.greenhouse.io/sonicwall', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div',class_='opening')
    
    lst_with_data = []
    for sd in soup_data:
        link ='https://boards.greenhouse.io' + sd.find('a')['href']
        title = sd.find('a').text
        location = sd.find_all('span', class_='location')[-1].text.strip()

        if 'Romania' in location:
            lst_with_data.append(return_lst_dict(title=title, link=link, location=location.split()[0].replace(',','').replace('Bucharest', 'Bucuresti')))
    
    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Sonicwall'
data_list = collect_data_from_sonicwall()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Sonicwall',
                  "https://recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/000/010/059/resized/sonicwall_logo_2.jpg?1518814608"
                  ))
