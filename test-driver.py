import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

base_url = "http://www.google.com"


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
# options.add_argument("--headless")
# options.add_argument("--window-size=1920x1080")
coptions.add_argument('--allow-insecure-localhost')
options.add_argument("--start-maximized")
service = webdriver.ChromeService(executable_path="chromedriver.exe")        
driver = webdriver.Chrome(service=service, options=options)

# os.environ['WDM_LOG_LEVEL'] = '0'

driver.implicitly_wait(20)

driver.get(base_url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
time.sleep(3)


