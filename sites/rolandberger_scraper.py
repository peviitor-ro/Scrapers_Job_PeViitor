#
#
#
# Scraper for RolandBerger Company
# Link to company career page -> https://careers.smartrecruiters.com/RolandBerger
#
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
import requests
from bs4 import BeautifulSoup
import uuid


def return_lst_dict(title: str, link: str) -> dict:
    '''
    ... this function will return a dict to append to a list and avoid DRY
    '''
    dct = {
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "RolandBerger",
                "country": "Romania",
                "city": 'Romania'
            }
    
    return dct


def return_soup(page: str):

    response = requests.get(url=f'https://careers.smartrecruiters.com/RolandBerger/api/groups?page={page}',
                            headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def return_soup_show_more(page: str):

    response = requests.get(url=f'https://careers.smartrecruiters.com/RolandBerger/api/more?type=location&value=Bucharest%2C%20RO&page={page}',
                            headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def collect_data_from_rolandberger():
    
    lst_with_data = []

    page = 1
    page_show_more = 1
    while True:

        data = return_soup(str(page))
        soup_data = data.find_all('section', attrs={'class': 'openings-section opening opening--grouped js-group'})

        if len(soup_data) > 1:
            for sd in soup_data:
                title_country = sd.find('li').find('h3', attrs={'class': 'opening-title title display--inline-block text--default'}).text

                # check for job in Ro!
                if 'Bucharest' in title_country or 'Romania' in title_country:

                    # search all jobs:
                    for ro_job in sd.find_all('li', attrs={'class': 'opening-job job column wide-7of16 medium-1of2'}):
                        link = ro_job.find('a', attrs={'class': 'link--block details'})['href']
                        title = ro_job.find('h4', attrs={'class': 'details-title job-title link--block-target'}).text

                        lst_with_data.append(return_lst_dict(title=title, link=link))

                    if sd.find('ul', attrs={'class': 'list--dotted'}):
                        show_more_data = return_soup_show_more(str(page_show_more))

                        for n_job in show_more_data.find_all('li', attrs={'class': 'opening-job job column wide-7of16 medium-1of2'}):
                            link = n_job.find('a', attrs={'class': 'link--block details'})['href']
                            title = n_job.find('h4', attrs={'class': 'details-title job-title link--block-target'}).text

                            lst_with_data.append(return_lst_dict(title=title, link=link))

        else:
            break

        page += 1
    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'RolandBerger'
data_list = collect_data_from_rolandberger()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('RolandBerger',
                  'data:image/jpeg;base64,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'
        ))

