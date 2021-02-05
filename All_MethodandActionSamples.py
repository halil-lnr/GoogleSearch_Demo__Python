from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.locators.l001_login_page_locators import LoginPageLocators


class UtilMethods(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.email_textbox_xpath = LoginPageLocators.email_textbox_xpath
        self.password_textbox_xpath = LoginPageLocators.password_textbox_xpath
        self.login_button_xpath = LoginPageLocators.login_button_xpath
        self.login_button_xpath = LoginPageLocators.login_button_xpath
        self.wait = WebDriverWait(self.driver, 30)

    def dropdown_visible_text(self, locator, text):
        # common method to select a value from the dropdown menu
        # Explicit waits halt the execution until 30 seconds or till the dropdown is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        select = Select(self.driver.find_element_by_xpath(locator))
        sleep(0.5)
        select.select_by_visible_text(text)

    def is_displayed(self, locator):
        # common method to verify if the element is displayed
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element_by_xpath(locator)
        # if the element is visible boolen TRUE is returned
        return element.is_displayed()

    def click(self, locator):
        # common method to click an element
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        # element is clicked
        self.driver.find_element_by_xpath(locator).click()

    def click_execute_script(self, locator):
        # common method to execute a click operation
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        # click even is executed using script method
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(locator))

    def send_keys(self, locator, value):
        # common method to send the text value to a variable
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        self.clear_text_field(locator)
        # Text value is sent to the element
        self.driver.find_element_by_xpath(locator).send_keys(value)

    def clear_text_field(self, locator):
        # common method to clear already existing value in a text field
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)

        self.driver.find_element_by_xpath(locator).clear()

    def get_text(self, locator):
        # common method to get a value from a element
        # Explicit waits halt the execution until 30 seconds or till the text element is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)

        # text value is retrived from the element
        text = self.driver.find_element_by_xpath(locator).text
        return text

    def execution_time(self, end_time):
        # Method to find the time taken for an Test case to execute
        # if end time is converted into minitus from seconds
        if end_time > 60:
            mins = int(end_time / 60)
            secs = end_time % 60
            return "Execution Time: " + str(mins) + "mins %.2f" % secs + 's'
        else:
            return "Execution Time: %.2f" % end_time + 's'

    def dropdown_first_select_text(self, locator):
        # Explicit waits halt the execution until 30 seconds or till the text element is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        # loading the dropdown element using xpath
        dropdown_element = self.driver.find_element_by_xpath(locator)
        # Usig select funtion creating an object for the dropdown element
        dropdown_obj = Select(dropdown_element)
        # extracting text from the selected value in the dropdown object
        dropdown_text = dropdown_obj.first_selected_option.text
        # Returning the extracted text
        return dropdown_text

    def element_is_enabled(self, locator):
        # common method to verify if the element is enabled
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element_by_xpath(locator)
        # if the element is enabled boolen TRUE is returned
        return element.is_enabled()
