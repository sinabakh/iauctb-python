__author__ = 'Sina Bakhtiari'

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from iauctb_py.exceptions import *


class IAUCTB:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        #self.driver.set_window_size(1120, 550)

    def login(self):
        self.driver.get("http://stu.iauctb.ac.ir/login.aspx")
        if "ثبت نام" not in self.driver.title:
            raise WebsiteNotAvailableException("Specified URL is wrong, or website is unreachable!")
        username_elem = self.driver.find_element_by_id("txtUserName")
        password_elem = self.driver.find_element_by_id("txtPassword")
        submit_elem = self.driver.find_element_by_id("LoginButton")

        username_elem.send_keys(self.username)
        password_elem.send_keys(self.password)
        submit_elem.click()
        try:
            dialog = self.driver.switch_to_alert()
            if "اشتباه است" in dialog.text:
                dialog.accept()
                raise WrongCredentialsException("Wrong Username or Password!")
        except NoAlertPresentException:
            if "سامانه آموزشی" not in self.driver.title:
                raise UnknownException("Login Encountered Unknown Page!")