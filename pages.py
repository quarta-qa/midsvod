from locators import *
from framework import *


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

    def checking_form_registry_filter(self, country, value, order=1):
        self.wait.element_appear((By.XPATH, "(//tr[@ng-repeat='item in plainGroupedItems']//td[2])[%s]" % order))
        while order < 3:
            table_country = self.driver.find_element(
                By.XPATH, "(//tr[@ng-repeat='item in plainGroupedItems']//td[2])[%s]" % order).text
            table_value = self.driver.find_element(
                By.XPATH, "(//tr[@ng-repeat='item in plainGroupedItems']//td[3])[%s]" % order).text
            print(table_country, country, table_value, value)
            if country == table_country and value == table_value:
                order += 1
            else:
                return False
        return True

    def checking_saving_another_mode_filter(self, country, values):# Необходимо дописать проверку по country
        self.wait.element_appear((
                    By.XPATH, "//th[@ng-repeat='desc in columns'][.='Организация']"))
        table_values = self.driver.find_element(
                    By.XPATH, "//div[@class='search-tag-group ng-scope']//div[@class='ticker-message ng-binding']").text
        if values == table_values:
            return True
        else:
            return False


class MonitoringByStatusPage(Browser):

    def click_on_the_element_of_forms(self):
        self.click(MonitoringByStatusLocators.number_of_submitted_forms, "Открытие режима Реестр форм")


class ScheduledMonitoringPage(Browser):

    def click_on_the_checkboxes(self):
        self.click(ScheduledMonitoringLocators.all_checkboxes_on_one_page,
                   "Проставление галок напротив всех форм на странице")


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

# Сравнение Excel файла с эталоном


def get_max_rows_and_cols(file):

    rows_max = 0
    cols_max = 0

    for name in file.sheet_names():
        sheet = file.sheet_by_name(name)
        if rows_max < sheet.nrows:
            rows_max = sheet.nrows
        if cols_max < sheet.ncols:
            cols_max = sheet.ncols

    return [rows_max, cols_max]


# Сравнение excel файлов 1
def analyze_two_files(filename):

    data = Data.load("data")
    file = data["way"]
    reference_file = file["directory"] + filename
    output_file = file["directoryCompare"] + filename

    output_hash = md5(output_file)
    reference_hash = md5(reference_file)
    if output_hash == reference_hash:
        print('Печатные формы одинаковы')
    else:
        # открываем исходный файл
        output = xlrd.open_workbook(output_file, on_demand=True, formatting_info=True)
        reference = xlrd.open_workbook(reference_file, on_demand=True, formatting_info=True)
        if output.nsheets != reference.nsheets:
            print('Количество книг не совпадает')
        else:
            print('Найдены ОШИБКИ в печатной форме: "%s"' % filename)

            output_max = get_max_rows_and_cols(output)
            reference_max = get_max_rows_and_cols(reference)
            max_rows = max(reference_max[0], output_max[0])
            max_cols = max(reference_max[1], output_max[1])

            reference_new = xlcopy(reference)
            for i in range(reference.nsheets):
                sheet = reference_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            reference_new.save(file["directory"]+"example.xls")

            output_new = xlcopy(output)
            for i in range(output.nsheets):
                sheet = output_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            output_new.save(file["directory"]+"example_new.xls")

    return [file["directory"]+"example.xls", file["directory"]+"example_new.xls"]


def compare_files(filename):

    files = analyze_two_files(filename)

    reference = xlrd.open_workbook(files[0], on_demand=True,  formatting_info=True)
    output = xlrd.open_workbook(files[1], on_demand=True, formatting_info=True)

    for index in range(reference.nsheets):
        reference_sheet = reference.sheet_by_index(index)
        output_sheet = output.sheet_by_index(index)
        reference_sheet_name = reference_sheet.name
        output_sheet_name = output_sheet.name
        if reference_sheet_name != output_sheet_name:
            print("Название книги[%s] не совпадает с эталонным [%s]!" % (output_sheet_name, reference_sheet_name))
        print("Книга [%s]:" % reference_sheet_name)
        for i in range(reference_sheet.nrows):
            for j in range(reference_sheet.ncols):
                reference_cell = reference_sheet.cell(i, j).value
                output_cell = output_sheet.cell(i, j).value
                if reference_cell != output_cell:
                    print("\tЯчейка [%s, %s]. Значение [%s] не совпадает с эталонным [%s]!"
                          % (i, j, output_cell, reference_cell))


# Получение хеша
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


#
def delete_spaces(value):
    return value.strip()

