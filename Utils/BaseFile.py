from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller
import unittest

class BasicClass(unittest.TestCase):
    @classmethod
    def get_classname(cls):
        return cls.__name__

    @classmethod
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()

        try:
            self.driver.get('https://www.niio.com/signin')
            self.driver.implicitly_wait(10)
        except TimeoutException as ex:
            isrunning = 0
            print("Exception has been throw: " + str(ex))


    @classmethod
    def tearDown(self):
        self.driver.quit()



