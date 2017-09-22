from framework import *


class LoginLocators(object):
    username = (By.XPATH, "//input[@id='j_username']")
    password = (By.XPATH, "//input[@id='j_password']")
    submit = (By.XPATH, "//button[@name='submit']")


class MainLocators(object):
    # По умолчанию главной строницей является "Реестр форм"
    menu = (By.XPATH, "//i[@class='qa-header-icon-menu-left-sitebar']")
    search = (By.XPATH, "//input[@class='searchInput ng-pristine ng-valid']")
    second_search = (By.XPATH, "//input[@class='searchInput ng-valid ng-dirty']")
    link_form_0503121 = (By.XPATH, "(//tr[@class='ng-scope'])[1]")
    find_element_form_0503121 = (
        By.XPATH, "//div[@class='q-grid-state-read q-mask ng-binding ng-scope'][contains(.,'Расходы')]")
    exit_account = (By.XPATH, "//i[@class='qa-header-icon-exit']")


class MonitoringByStatusLocators(object):
    number_of_submitted_forms = (By.XPATH, "//tr[@class = 'pivotRow'][contains(., 'Бразилия')]//td[3]")


class ChessLocators(object):
    search_organization = (By.XPATH, "(//input)[2]")
    search_code_form = (By.XPATH, "(//input)[3]")
