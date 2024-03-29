import time
from selenium import webdriver
from customLogger import LogGen
from selenium.webdriver.chrome.service import Service
import os


class OpenGoogle:
    base_url = "http://www.google.com"

    logger = LogGen.loggen()
    service = Service()
    options = webdriver.ChromeOptions()
    options.headless = False
    options.accept_insecure_certs = True

    driver = webdriver.Chrome(service=service, options=options)
  
    os.environ['WDM_LOG_LEVEL'] = '0'

    driver.implicitly_wait(20)

    print("Launching Headless browser.........")
    logger.info("Launching Headless browser.........")
    driver.get(base_url)
    print(" Google Page Loading... ")
    logger.info("Login Page Loading............")
    driver.maximize_window()

    page_title = driver.title
    print("Page title is : " + page_title)
    logger.info("Page title is : " + page_title)
    time.sleep(3)
    
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('Laptop')
    search_box.submit()
    time.sleep(5)
    
    page_title = driver.title
    print("New page title is : " + page_title)
    logger.info("New page title is : " + page_title)
    time.sleep(3)
    
    userName_xpath = "//input[@formcontrolname='username']"
    passWord_xpath = "//input[@formcontrolname='password']"
    arrowGroupID_xpath = "//div[contains(@class,'arrow')]"
    btnLogin_xpath = "//span[text()='Login']"

    time.sleep(1)
    current_url = driver.current_url
    print(f"Page Opened = {current_url}")
    
#     driver.find_element_by_xpath(userName_xpath).send_keys("infosys_user")
#     time.sleep(1)
#     print("Username Entered")
#     driver.find_element_by_xpath(passWord_xpath).send_keys("Automation03")
#     print("Password Entered")
#     time.sleep(1)
#     driver.find_element_by_xpath(arrowGroupID_xpath).click()
#     time.sleep(1)
#     element = driver.find_element_by_xpath("//*[contains(text(),'External')]")
#     element.click()
#     print("Type Selected as External")
#     time.sleep(2)
#     driver.find_element_by_xpath(btnLogin_xpath).click()
#     print("Login Button Clicked")

    time.sleep(5)
    driver.close()

    print(" Page CLOSED successfully.")
    logger.info(" Page CLOSED successfully. ")

    # if header_text == "Home":
    # if "Home" in header_text:
    #     assert True
    #     print(" Logged in successfully. ")
    #     time.sleep(3)
    #     driver.close()
    # else:
    #     print("Log in was NOT successfully. ")
    #     driver.close()
