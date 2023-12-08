import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

import platform

options = Options()
options.headless = True
options.accept_insecure_certs = True

# GitHub actions
if platform.system() == "Linux":
    print(platform.system())
    webdriver_service = Service("chromedriver")
    driver = webdriver.Chrome(service=webdriver_service, options=options)   

# Jenkins and local run
elif platform.system() == "Windows":
    print(platform.system())
    cwd = str(os.getcwd())
    chrome_driver_path = cwd + r'/chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path,options=options)            
else:
    print("Wrong Operating System")
    
url = "https://google.com/"

driver.get(url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
