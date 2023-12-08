# from selenium import webdriver

# url = "https://google.com/"
# driver = webdriver.Chrome()
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

options = Options()
options.headless = True
options.accept_insecure_certs = True

cwd = str(os.getcwd())
chrome_driver = cwd + r'/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver,options=options)
url = "https://google.com/"

driver.get(url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
