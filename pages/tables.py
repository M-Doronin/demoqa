import time
from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Локаторы элементов
        self.btn_delete_row = WebElement(driver, "button[title='Delete']")  # кнопка удаления строки
        self.no_data = WebElement(driver, "div.rt-noData")  # блок «No rows found»
        self.table_rows = WebElement(driver, ".rt-tr-group")  # все строки таблицы

    def visit(self):
        """Открывает страницу с веб‑таблицами"""
        self.driver.get(self.base_url)
        # Ожидание загрузки страницы
        time.sleep(2)

    def get_row_count(self):
        """Возвращает количество видимых строк в таблице"""
        return len(self.table_rows.find_elements())

    def exist(self):
        """
        Проверяет, существует ли элемент на странице.
        Используется для self.no_data.exist() в тесте.
        """
        try:
            return self.no_data.find_element().is_displayed()
        except:
            return False

    def is_table_empty(self):
        """Альтернативный метод проверки пустоты таблицы"""
        return self.get_row_count() == 0

    def delete_all_rows(self):
        """Удаляет все строки из таблицы (вспомогательный метод)"""
        while self.btn_delete_row.exist():
            self.btn_delete_row.click()
            time.sleep(0.5)  # небольшая пауза между кликами



