# Scraper for Zenitech Company
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

def collect_data_from_zenitech():
    '''
    ... this function will collect all data and will return a list with jobs
    '''

    response = requests.get(url='https://careers.zenitech.co.uk/jobs?location=Cluj-Napoca&query=', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('li', class_='transition-opacity duration-150 border rounded block-grid-item border-block-base-text border-opacity-15')

    lst_with_data= []
    for sd in soup_data:
        link = sd.find('a')['href']
        title = sd.find('span', class_='text-block-base-link company-link-style').text
        
        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": link,
            "company": "Zenitech",
            "country": "Romania",
            "city": 'Romania'
        })

    return lst_with_data



@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Zenitech'
data_list = collect_data_from_zenitech()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Zenitech',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTbilzbfZlTkelqz8CryI0bJ2c2KX0deihBw&usqp=CAU"
                  ))