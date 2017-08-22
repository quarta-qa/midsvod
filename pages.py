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

    def search(self):
        self.set_text(MainLocators.search, "Поле поиска")