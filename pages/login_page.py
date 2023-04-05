from utils.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BasePage):
    USERNAME = (MobileBy.ID, "com.example.app:id/username")
    PASSWORD = (MobileBy.ID, "com.example.app:id/password")
    LOGIN_BUTTON = (MobileBy.ID, "com.example.app:id/login")

    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
