# from selenium import webdriver

# url = "https://google.com/"
# driver = webdriver.Chrome()
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

import platform
if platform.system() == "Linux":
# GitHub actions
    print(platform.system())
    # self.driver = webdriver.Chrome(service=webdriver_service, options=options)   

elif platform.system() == "Windows":
# Jenkins and local run
    print(platform.system())
    # self.driver = webdriver.Chrome(executable_path=chrome_driver,options=options)            
else:
    print("Wrong Operating System")

options = Options()
options.headless = True
options.accept_insecure_certs = True

cwd = str(os.getcwd())
chrome_driver = cwd + r'/chromedriver.exe'

driver = webdriver.Chrome(service=webdriver_service, options=options) 
# driver = webdriver.Chrome(executable_path='/chromedriver.exe',options=options)
url = "https://google.com/"

driver.get(url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
