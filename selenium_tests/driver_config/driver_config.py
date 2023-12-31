from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def chromedriver_config(headless=True):
    """
    Config webdriver for future commands.
    """
    chrome_options = Options()

    # for chrome options
    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # antibot
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # set user_agent
    chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0")

    service = Service('C:\Scraper_Jobs_Peviitor\selenium_tests\selenium_driver\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver
