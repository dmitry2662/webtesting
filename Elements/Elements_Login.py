from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging


class ElementLoginScreen:
    def __init__(self, driver):
        self._driver = driver

    def get_element_login(self):
        try:
            element_input_username = WebDriverWait(self._driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@id='email']")))
            return element_input_username
        except NoSuchElementException as ex:
            logging.info(str(ex))


class ElementPasswScreen:
    def __init__(self, driver):
        self._driver = driver

    def get_element_passwd(self):
        try:
            element_input_passwd = WebDriverWait(self._driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@id='password']")))
            return element_input_passwd
        except NoSuchElementException as ex:
            logging.info(str(ex))
