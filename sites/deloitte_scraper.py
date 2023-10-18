#
#
#
# Scraper for Deloitte Company
# Link to company career page -> https://apply.deloittece.com/en_US/careers/SearchJobs/?523=%5B5509%5D&523_format=1482&listFilterMode=1&jobRecordsPerPage=10&jobOffset=0
#
#
#
from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
#
from requests_html import HTMLSession
from bs4 import BeautifulSoup
#
import uuid
import time


def make_bs4_object(requests_html_object) -> BeautifulSoup:
    '''
    Convert requests-html to bs4 object.
    '''

    return BeautifulSoup(requests_html_object, 'lxml')


def config_requests_html() -> HTMLSession:
    '''
    Config requests_html with headers and make new requests
    and parse js data.
    '''

    session = HTMLSession()
    session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    session.headers['Accept-Language'] = 'en-US,en;q=0.5'
    session.headers['Refer'] = 'https://google.com/'
    session.headers['DNT'] = '1'

    return session


def collect_data_from_delloite():
    '''
    ... this function will collect all data and will return a list with available jobs
    '''

    session = config_requests_html()
    page_jobs = 0
    flag = True
    lst_with_data = []

    while flag != False:
        response = session.get(url=f'https://apply.deloittece.com/en_US/careers/SearchJobs/?523=%5B5509%5D&523_format=1482&listFilterMode=1&jobRecordsPerPage=10&jobOffset={page_jobs}')
        time.sleep(1)
        
        job_elements = response.html.find('article.article.article--result')
        if len(job_elements) > 1:
            for job in job_elements:
                soup_bs4 = make_bs4_object(job.html)

                link = soup_bs4.find('a')['href']
                title = soup_bs4.find('a').text.strip()
            

                lst_with_data.append({
                    "id": str(uuid.uuid4()),
                    "job_title": title,
                    "job_link": link,
                    "company": "Deloitte",
                    "country": "Romania",
                    "city": "Romania"
                })

        else:
            flag = False
            break
        print(f'Suntem pe pagina {page_jobs}')
        page_jobs += 10
        
    return lst_with_data


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'Deloitte'
data_list = collect_data_from_delloite()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('Deloitte',
                  "https://www2.deloitte.com/content/dam/Deloitte/us/Images/promo_images/deloitte/us-deloitte-logo.jpg"
                  ))