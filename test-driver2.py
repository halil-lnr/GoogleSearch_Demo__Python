# from selenium import webdriver

# url = "https://google.com/"
# driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

webdriver_service = Service("chromedriver")
options = Options()
options.headless = False
options.accept_insecure_certs = True

driver = webdriver.Chrome(service=webdriver_service, options=options)

driver.get(url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
