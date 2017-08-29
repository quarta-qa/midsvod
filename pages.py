from locators import *

import json
import os
import glob


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
        self.click(MainLocators.link_form, "Открытие формы")

    def exit_account(self):
        self.click(MainLocators.exit_account, "Выход из аккаунта")


class ChessPage(Browser):

    def search_organization(self, value):
        self.set_text(ChessLocators.search_organization, value, "Поле поиска по организации")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def search_code_form(self, value):
        self.set_text(ChessLocators.search_code_form, value, "Поле поиска по коду формы")
        self.click((By.XPATH, "//li[contains(., '%s')]" % value))

    def table_check(self, country, value):
        self.wait.element_appear((By.XPATH,
                                  "//tr[@ng-repeat='row in rows']//span[.='%s']" % country))
        table_country = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='row in rows']//td[2]").text
        table_value = self.driver.find_element(
            By.XPATH, "//tr[@ng-repeat='row in rows']//td[3]").text
        if (country == table_country) and (value == table_value):
            return True
        else:
            return False
