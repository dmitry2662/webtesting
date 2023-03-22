from Utils.BaseFile import BasicClass
from Elements.Elements_Login import ElementLoginScreen
from Elements.Elements_Login import ElementPasswScreen


class LoginFlow(BasicClass):
    def test_correctly(self):
        elements = ElementLoginScreen(self.driver)
        element_username = elements.get_element_login()
        if element_username:
            element_username.send_keys("test25@niio.com")

        element_password = ElementPasswScreen(self.driver)
        input_password = element_password.get_element_passwd()
        if element_username is not None:
            input_password.send_keys("N1io11!!")
            print("SSSSSSS")
