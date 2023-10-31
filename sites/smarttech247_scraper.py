# # Scraper for Smarttech Company
# # Link to company career page -> https://www.smarttech247.com/careers/
# #
# #
# #
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
import requests
from bs4 import BeautifulSoup
#
import uuid
#
def collect_data_from_smarttech():
    '''
    ... this function will collect all data and will return a list with  jobs
    '''

    response = requests.get(url='https://www.smarttech247.com/careers/', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('div', class_='column hasnumbercard')

    lst_with_data = []
    for sd in soup_data:
        title = sd.find('p', class_='maintitle').text
        links = sd.find('div', class_='topcontent').find_all('a')

        # getting links by title
        new_title = title.split()[0].lower()
        new_link = ''
        for link in links:
            if new_title in link['href']:
                new_link = link['href']

        lst_with_data.append({
            "id": str(uuid.uuid4()),
            "job_title": title,
            "job_link": new_link,
            "company": "Smarttech247",
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


company_name = 'Smarttech247'
data_list = collect_data_from_smarttech()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Smarttech247',
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDdbElJVeQzKcdSRaPog3--QX26GdtMyI808b_egrYSw&s"
                  ))




