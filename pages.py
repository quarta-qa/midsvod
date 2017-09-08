from locators import *


class LoginPage(Browser):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click(LoginLocators.submit, "Войти")


class MainPage(Browser):

    def menu(self):
        self.click(MainLocators.menu, "Меню")

    def search(self, value):
        self.set_text(MainLocators.search, value, "Поле поиска")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def second_search(self, value):
        self.set_text(MainLocators.second_search, value, "Поле поиска")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def open_form(self):
        self.click(MainLocators.link_form_0503121, "Открытие формы")

    def exit_account(self):
        self.click(MainLocators.exit_account, "Выход из аккаунта")

    def checking_form_registry_filter(self, country, value):
        self.wait.element_appear((By.XPATH, "//tr[@ng-repeat='item in plainGroupedItems'][1]//td[.='%s']" % country))
        n = 1
        table_country = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='item in plainGroupedItems']['%c']//td[2]" % n).text
        table_value = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='item in plainGroupedItems']['%c']//td[3]" % n).text
        while n < 3:
            if (country == table_country) and (value == table_value):
                print(table_country, table_value)
            elif (country != table_country) or (value != table_value):
                return False
            n = n + 1

    def checking_saving_another_mode_filter(self, country, values):
        self.wait.element_appear(
                    By.XPATH, "//tr[@ng-repeat='item in plainGroupedItems']//td[.='%s']" % country)
        table_values = self.driver.find_element(
                    By.XPATH, "//div[@class='search-tag-group ng-scope']").text
        if values == table_values:
            return True
        else:
            return False

class MonitoringByStatusPage(Browser):

    def click_on_the_element_of_forms(self):
        self.click(MonitoringByStatusLocators.number_of_submitted_forms, "Открытие режима Реестр форм")


class ChessPage(Browser):

    def search_organization(self, value):
        self.set_text(ChessLocators.search_organization, value, "Поле поиска по организации")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def search_code_form(self, value):
        self.set_text(ChessLocators.search_code_form, value, "Поле поиска по коду формы")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def table_check(self, country, value):
        self.wait.element_appear(
                By.XPATH, "//tr[@ng-repeat='row in rows']//span[.='%s']" % country)
        table_country = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='row in rows']//td[2]").text
        table_value = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='row in rows']//td[3]").text
        if (country == table_country) and (value == table_value):
            return True
        else:
            return False
