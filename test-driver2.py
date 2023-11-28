# from selenium import webdriver

# url = "https://google.com/"
# driver = webdriver.Chrome()

import os

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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
