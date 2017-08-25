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
        self.click(MainLocators.link_form, "Открытие формы")

    def exit_account(self):
        self.click(MainLocators.exit_account, "Выход из аккаунта")

