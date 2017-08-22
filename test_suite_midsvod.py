from pages import *
from links import Links


class TestSuite:

    driver = webdriver.Chrome("driver\\chromedriver.exe")

    @classmethod
    def setup_class(cls):
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_login(self):
        """
        Авторизация на портале
        """
        page = LoginPage(self.driver)
        page.username("svodzu")
        page.password("123")
        page.submit()

    def test_example(self):
        """
        Проверка меню
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Справочники")
        page.click_by_text("КБК (финансирования)")
        # page.wait.text_appear("Год  актуальности")
        assert "Год  актуальности" in self.driver.page_source

    def test_menu_monitoring_chess(self):
        """
        Меню - Мониторинг - Шахматка
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Шахматка")
        assert "Организация" in self.driver.page_source

    def test_menu_monitoring_schedule_monitoring(self):
        """
        Меню - Мониторинг - Списочный мониторинг
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Списочный мониторинг")
        assert "Наименование организации" in self.driver.page_source

    def test_menu_monitoring_monitoring_by_status(self):
        """
        Меню - Мониторинг - Мониторинг по статусам
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Мониторинг по статусам")
        assert "Количество форм" in self.driver.page_source


    def test_menu_monitoring_deleted_documents(self):
        """
        Меню - Мониторинг - Удаленные документы
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Удалённые документы")
        page.wait.text_appear("ВОССТАНОВИТЬ")
        assert "ВОССТАНОВИТЬ" in self.driver.page_source

    def test_menu_monitoring_planning(self):
        """
        Меню - Мониторинг - Планирование
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Планирование")
        assert "Установить срок" in self.driver.page_source

    def test_menu_monitoring_directives(self):
        """
        Меню - Директивы
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Директивы")
        assert "От кого" in self.driver.page_source

    def test_menu_monitoring_settings(self):
        """
        Меню - Настройки
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Настройки")
        assert "ФИО" in self.driver.page_source

    def test_menu_monitoring_аdministrator_logs(self):
        """
        Меню - Журналы администратора - Функция обновления для админа
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Настройки")
        assert "ФИО" in self.driver.page_source

