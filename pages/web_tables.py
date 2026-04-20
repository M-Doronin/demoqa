from pages.base_page import BasePage
from components.components import WebElement
import time
from selenium.webdriver.common.by import By

class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/webtables")
        # Кнопки
        self.btn_add = WebElement(driver, locator="#addNewRecordButton", locator_type="css")
        self.btn_submit = WebElement(driver, locator="#submit", locator_type="css")
        self.btn_close_modal = WebElement(
            driver,
            locator="body > div.fade.modal.show > div > div > div.modal-header > button",
            locator_type="css"
        )

        # Поля формы добавления/редактирования
        self.input_first_name = WebElement(driver, locator="#firstName", locator_type="css")
        self.input_last_name = WebElement(driver, locator="#lastName", locator_type="css")
        self.input_email = WebElement(driver, locator="#userEmail", locator_type="css")
        self.input_age = WebElement(driver, locator="#age", locator_type="css")
        self.input_salary = WebElement(driver, locator="#salary", locator_type="css")
        self.input_department = WebElement(driver, locator="#department", locator_type="css")

        # Элементы таблицы
        self.table_rows = WebElement(driver, locator=".rt-tbody .rt-tr", locator_type="css")
        self.edit_buttons = WebElement(driver, locator="span[title='Edit']", locator_type="css")
        self.delete_buttons = WebElement(driver, locator="span[title='Delete']", locator_type="css")

    def safe_click(self, element):
        """Безопасный клик через JavaScript, если обычный клик не работает"""
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element.find_element())

    def is_modal_visible(self):
        """Проверяет, открыто ли модальное окно"""
        try:
            return self.input_first_name.visible()
        except:
            return False

    def add_new_record(self, first_name, last_name, email, age, salary, department):
        """Добавление новой записи через форму"""
        self.safe_click(self.btn_add)
        time.sleep(2)  # Ждём открытия модального окна

        self.input_first_name.send_keys(first_name)
        self.input_last_name.send_keys(last_name)
        self.input_email.send_keys(email)
        self.input_age.send_keys(age)
        self.input_salary.send_keys(salary)
        self.input_department.send_keys(department)

        self.safe_click(self.btn_submit)
        time.sleep(3)  # Увеличенное ожидание закрытия модального окна и обновления таблицы

    def get_table_data(self):
        """Получение всех данных из таблицы с проверкой наличия строк"""
        time.sleep(2)  # Даём время на обновление таблицы
        rows = self.table_rows.find_elements()
        data = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
            row_data = [cell.text for cell in cells if cell.text.strip()]  # Фильтруем пустые ячейки
            if row_data:  # Добавляем только непустые строки
                data.append(row_data)
        return data

    def wait_for_table_update(self, initial_row_count, timeout=10):
        """Ожидание обновления таблицы (добавления новой строки)"""
        for _ in range(timeout):
            current_data = self.get_table_data()
            if len(current_data) > initial_row_count:
                return current_data
            time.sleep(1)
        raise TimeoutError("Таблица не обновилась в течение таймаута")

    def edit_record(self, row_index, new_first_name=None):
        """Редактирование записи (изменение имени)"""
        # Перезапрашиваем кнопки редактирования — после обновления таблицы старые ссылки могут быть неактуальны
        edit_buttons = self.edit_buttons.find_elements()

        if row_index >= len(edit_buttons):
            raise IndexError(f"Индекс строки {row_index} выходит за пределы доступных кнопок редактирования ({len(edit_buttons)})")

        self.safe_click(edit_buttons[row_index])
        time.sleep(2)  # Ждём открытия модального окна редактирования

        if new_first_name:
            self.input_first_name.clear()
            self.input_first_name.send_keys(new_first_name)

        self.safe_click(self.btn_submit)
        time.sleep(2)  # Ждём закрытия окна после сохранения

    def delete_record(self, row_index):
        """Удаление записи"""
        delete_buttons = self.delete_buttons.find_elements()
        self.safe_click(delete_buttons[row_index])
        time.sleep(1)  # Ждём удаления строки из таблицы