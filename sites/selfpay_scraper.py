#
#
#
# Scraper for Selfpay Company
# Link to company career page -> https://careers.smartrecruiters.com/SelfPay
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


def collect_data_from_selfpay():
    '''
    ... this function will collect all data and will return a list with available jobs
    '''
    response = requests.get(url='https://careers.smartrecruiters.com/SelfPay', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')

    soup_data = soup.find_all('section', class_='openings-section opening opening--grouped js-group')


    lst_with_data = []
    for sd in soup_data:
        for job in sd.find_all('li', class_='opening-job job column wide-7of16 medium-1of2'):
            link = job.find('a')['href']
            title = job.find('h4', class_='details-title job-title link--block-target').text

            lst_with_data.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "selfpay",
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


company_name = 'selfpay'
data_list = collect_data_from_selfpay()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('selfpay',
                  "data:image/png;base64,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"
                  ))
