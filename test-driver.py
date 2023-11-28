import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

base_url = "http://www.google.com"
desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--allow-insecure-localhost')
driver = webdriver.Chrome(options=chrome_options)

# os.environ['WDM_LOG_LEVEL'] = '0'

driver.implicitly_wait(20)

driver.get(base_url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
time.sleep(3)
