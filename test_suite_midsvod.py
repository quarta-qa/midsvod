from pages import *
from links import Links


class TestSuite:

    driver = webdriver.Chrome("driver\\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)
        cls.main = MainPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_login(self):
        """
        Авторизация на портале
        """
        page = LoginPage(self.driver)
        page.username("admin")
        page.password("quarta")
        page.submit()
        assert "Реестр отчетных форм" in self.driver.page_source

    def test_register_form(self):
        """
        Создание отчетой формы
        """
        page = FormRegisterPage(self.driver)
        self.main.menu()
        page.click_by_text("Реестр форм")
        page.click_by_text("Добавить")
        sleep(10)
