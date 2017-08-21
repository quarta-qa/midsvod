from locators import *


class LoginPage(Browser):

    def username(self, value):
        self.set_text(LoginLocators.username, value, "Логин")

    def password(self, value):
        self.set_text(LoginLocators.password, value, "Пароль")

    def submit(self):
        self.click_by_text("Войти")


class MainPage(Browser):

    def menu(self):
        self.click(MainLocators.menu, "Главное меню")


class FormRegisterPage(Browser):

    pass
