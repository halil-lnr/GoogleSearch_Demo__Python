from selenium import webdriver

url = "https://google.com/"
driver = webdriver.Chrome()
driver.get(url)
print(" Google Page Loading... ")
driver.maximize_window()

page_title = driver.title
print("Page title is : " + page_title)
