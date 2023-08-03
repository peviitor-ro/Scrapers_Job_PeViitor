from driver_config import chromedriver_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = chromedriver_config(headless=False)
try:
    driver.get('https://www.olx.ro/')
    time.sleep(3)
    accept_cookies = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
    input_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "headerSearch"))).send_keys('apartamente')
    time.sleep(1)
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "submit-searchmain"))).click()
except:
    pass
finally:
    time.sleep(5)
    driver.quit()

