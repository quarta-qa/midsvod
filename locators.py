from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='j_username']")
    password = (By.XPATH, "//input[@id='j_password']")
    submit = (By.XPATH, "//button[@name='submit']")


class MainLocators(object):
    menu = (By.XPATH, "//i[@class='qa-header-icon-menu-left-sitebar']")

