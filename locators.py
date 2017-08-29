from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='j_username']")
    password = (By.XPATH, "//input[@id='j_password']")
    submit = (By.XPATH, "//button[@name='submit']")


class MainLocators(object):
    menu = (By.XPATH, "//i[@class='qa-header-icon-menu-left-sitebar']")
    search = (By.XPATH, "//input[@class='searchInput ng-pristine ng-valid']")
    second_search = (By.XPATH, "//input[@class='searchInput ng-valid ng-dirty']")
    link_form = (By.XPATH, "(//tr)[1]")
    exit_account = (By.XPATH, "//i[@class='qa-header-icon-exit']")

class ChessLocators(object):
    search_organization = (By.XPATH, "(//input)[2]")
    search_code_form = (By.XPATH, "(//input)[3]")
