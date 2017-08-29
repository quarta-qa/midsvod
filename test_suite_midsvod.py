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
        data = Data.load("data")
        print(data["test"]["directory"])

    def test_selection_of_the_reporting_period(self):
        """
        Выбор отчетного периода (год и месяц)
        """
        page = MainPage(self.driver)
        page.select_month(2017, 6)

    def test_menu_monitoring_chess(self):
        """
        Переход в режим Мониторинг - Шахматка.
        (Меню - Маниторинг - Шахматка)
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Шахматка")
        assert "Организация" in self.driver.page_source

    def test_monitoring_chess_search_fields_by_name_organization_and_by_code_form(self):
        """
        Мониторинг - Шахматка. Тестирование полей поиска по названию организации и по коду формы (ОКУД)
        """
        page = ChessPage(self.driver)
        page.search_organization("Бразилия")
        page.search_code_form("0503126 МЭР ЗУ – Справка об остатках денежных средств")
        assert page.table_check("Бразилия", "4")

    # def_test_example(self):
    #     """
    #     заготовка на проверку перехода в подрежимы Справочники черех Меню
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Справочники")
    #     page.click_by_text("КБК (финансирования)")
    #     # page.wait.text_appear("Год  актуальности")
    #     assert "Год  актуальности" in self.driver.page_source
    #
    # def test_menu_monitoring_chess(self):
    #     """
    #     Меню - Мониторинг - Шахматка
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Мониторинг")
    #     page.click_by_text("Шахматка")
    #     assert "Организация" in self.driver.page_source
    #
    # def test_menu_monitoring_schedule_monitoring(self):
    #     """
    #     Меню - Мониторинг - Списочный мониторинг
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Мониторинг")
    #     page.click_by_text("Списочный мониторинг")
    #     page.wait.text_appear("Наименование организации")
    #     assert "Наименование организации" in self.driver.page_source
    #
    # def test_menu_monitoring_monitoring_by_status(self):
    #     """
    #     Меню - Мониторинг - Мониторинг по статусам
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Мониторинг")
    #     page.click_by_text("Мониторинг по статусам")
    #     assert "Количество форм" in self.driver.page_source
    #
    # def test_menu_monitoring_deleted_documents(self):
    #     """
    #     Меню - Мониторинг - Удаленные документы
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Мониторинг")
    #     page.click_by_text("Удалённые документы")
    #     page.wait.text_appear("ВОССТАНОВИТЬ")
    #     assert "ВОССТАНОВИТЬ" in self.driver.page_source
    #
    # def test_menu_monitoring_planning(self):
    #     """
    #     Меню - Мониторинг - Планирование
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Мониторинг")
    #     page.click_by_text("Планирование")
    #     assert "Установить срок" in self.driver.page_source
    #
    # def test_menu_directives(self):
    #     """
    #     Меню - Директивы
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Директивы")
    #     assert "От кого" in self.driver.page_source
    #
    # def test_menu_settings(self):
    #     """
    #     Меню - Настройки
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Настройки")
    #     assert "ФИО" in self.driver.page_source
    #
    # def test_menu_administrator_logs_update_function_for_the_admin(self):
    #     """
    #     Меню - Журналы администратора - Функция обновления для админа
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Журналы администратора")
    #     page.click_by_text("Функции обновления для админа")
    #
    # def test_menu_administrator_logs_log_visit_to_users(self):
    #     """
    #     Меню - Журналы администратора - Журнал входа/выхода пользователей
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Журналы администратора")
    #     page.click_by_text("Журнал входа/выхода пользователей")
    #     assert "Тип события" in self.driver.page_source
    #
    # def test_menu_administrator_logs_user_activity_log(self):
    #     """
    #     Меню - Журналы администратора -  Журнал действий пользователей
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Журналы администратора")
    #     page.click_by_text("Журнал действий пользователей")
    #     assert "Ссылка доступа" in self.driver.page_source
    #
    # def test_menu_administrator_logs_import_results(self):
    #     """
    #     Меню - Журналы администратора - Результаты иморта
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Журналы администратора")
    #     page.click_by_text("Результаты импорта")
    #     assert "Время импорта (сек)" in self.driver.page_source
    #
    # def test_menu_system_buttons(self):
    #     """
    #     Меню - Системные кнопки
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные кнопки")
    #     page.wait.text_appear("Сортировать документы")
    #     assert "Сортировать документы" in self.driver.page_source
    #
    # def test_menu_synchronization_settings_ftp(self):
    #     """
    #     Меню - Синхронизация - Настройки FTP
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Синхронизация")
    #     page.click_by_text("Настройки FTP")
    #     assert "Интервал синхронизации" in self.driver.page_source
    #
    # def test_menu_synchronization_sync_settings(self):
    #     """
    #     Меню - Синхронизация - Настройка синхронизации:
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Синхронизация")
    #     page.click_by_text("Настройки синхронизации")
    #     assert "Список синхронизируемых учетных объектов" in self.driver.page_source
    #
    # def test_menu_synchronization_versioning(self):
    #     """
    #     Меню - Синхронизация - Управление версиями
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Синхронизация")
    #     page.click_by_text("Управление версиями")
    #     assert "Создать версию" in self.driver.page_source
    #
    # def test_menu_organization_settings(self):
    #     """
    #
    #     Меню - Настройки организации
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Настройки организации")
    #     assert "Буквенное обозначение" in self.driver.page_source
    #
    # def test_menu_system_settings_account_management(self):
    #     """
    #     Меню - Системные настройки - Управление аккаунтами
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Управление аккаунтами")
    #     assert "Пользователь" in self.driver.page_source
    #
    # def test_menu_system_settings_role_management(self):
    #     """
    #     Меню - Системные настройки - Управление ролями
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Управление ролями")
    #     assert "Идентификатор (лат.)" in self.driver.page_source
    #
    # def test_menu_system_settings_history_of_changes(self):
    #     """
    #     Меню - Системные настройки - История изменений
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("История изменений")
    #     assert "Значение до" in self.driver.page_source
    #
    # def test_menu_system_settings_report_input_forms(self):
    #     """
    #     Меню - Системные настройки - Формы ввода отчетов
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Формы ввода отчетов")
    #     assert "Группа сбора" in self.driver.page_source
    #
    # def test_menu_system_settings_description_of_input_forms(self):
    #     """
    #     Меню - Системные настройки - Описание форм ввода
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Описание форм ввода")
    #     assert "Форма ввода" in self.driver.page_source
    #
    # def test_menu_system_settings_collection_group(self):
    #     """
    #     Меню - Системные настройки - Группа сбора
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Группы сбора")
    #     assert "Родительская группа" in self.driver.page_source
    #
    # def test_menu_system_settings_menu(self):
    #     """
    #     Меню - Системные настройки - Меню
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Меню")
    #     assert "Наименование" in self.driver.page_source
    #
    # def test_menu_system_settings_accounting_object(self):
    #     """
    #     Меню - Системные настройки - Учетные объекты
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Учетные объекты")
    #     assert "Имя таблицы в БД (лат.)" in self.driver.page_source
    #
    # def test_menu_system_settings_representation(self):
    #     """
    #     Меню - Системные настройки - Представления
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Представления")
    #     assert "Идентификатор представления (лат.)" in self.driver.page_source
    #
    # def test_menu_system_scripts(self):
    #     """
    #     Меню - Системные настройки - Скрипты
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Скрипты")
    #     assert "Пользователь" in self.driver.page_source
    #
    # def test_menu_system_starting_object_for_the_role(self):
    #     """
    #     Меню - Системные настройки - Стартовый объект для роли
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Стартовый объект для роли")
    #     assert "Объект для стартовой страницы" in self.driver.page_source
    #
    # def test_menu_system_starting_source(self):
    #     """
    #     Меню - Системные настройки - Исходные коды
    #     """
    #     page = MainPage(self.driver)
    #     page.menu()
    #     page.click_by_text("Системные настройки")
    #     page.click_by_text("Исходные коды")
    #     assert "Исходники" in self.driver.page_source

    def test_menu_form_registry(self):
        """
        Меню - Реестр форм
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Реестр форм")
        page.wait.text_appear("Организация")
        assert "Организация" in self.driver.page_source

    def test_page_form_registry_search_field(self):
        """
        Тест поля поиска
        """
        page = MainPage(self.driver)
        page.search("Бразилия")
        sleep(1)
        page.second_search("0503121")
        sleep(1)

    def test_page_form_registry_open_form(self):
        """
        Открытие формы
        """
        page = MainPage(self.driver)
        page.open_form()
        page.wait.text_appear("Принять к рассмотрению")
        assert "Принять к рассмотрению" in self.driver.page_source

    def test_menu_monitoring_monitoring_by_status(self):
        """
        Меню - Мониторинг - Мониторинг по статусам
        """
        page = MainPage(self.driver)
        page.menu()
        page.click_by_text("Мониторинг")
        page.click_by_text("Мониторинг по статусам")
        assert "Количество форм" in self.driver.page_source

    def test_print_on_the_page__monitoring_by_status(self):
        """
        Тестирование кнопки печать
        """
        page = MainPage(self.driver)
        page.click_by_text("Печать")



