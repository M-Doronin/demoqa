import time
import pytest
from pages.web_tables import WebTablesPage

@pytest.fixture
def web_tables_page(browser):
    """Фикстура для инициализации страницы"""
    page = WebTablesPage(browser)
    page.visit()
    return page

def test_web_tables_full_functionality(web_tables_page):
    # a. Проверка наличия кнопки Add
    assert web_tables_page.btn_add.exist(), "Кнопка Add не найдена на странице"

    # b. Открытие диалогового окна по клику на Add
    web_tables_page.safe_click(web_tables_page.btn_add)
    time.sleep(2)  # Ждём открытия модального окна

    assert web_tables_page.input_first_name.exist(), "Поле First Name не отображается в диалоге"
    assert web_tables_page.input_last_name.exist(), "Поле Last Name не отображается в диалоге"
    assert web_tables_page.input_email.exist(), "Поле Email не отображается в диалоге"
    assert web_tables_page.input_age.exist(), "Поле Age не отображается в диалоге"
    assert web_tables_page.input_salary.exist(), "Поле Salary не отображается в диалоге"
    assert web_tables_page.input_department.exist(), "Поле Department не отображается в диалоге"

    # c. Проверка невозможности сохранения пустой формы
    initial_modal_state = web_tables_page.is_modal_visible()
    web_tables_page.safe_click(web_tables_page.btn_submit)
    time.sleep(1)
    final_modal_state = web_tables_page.is_modal_visible()

    assert initial_modal_state == final_modal_state, \
        "Модальное окно должно оставаться открытым при попытке сохранения пустой формы"

    # Закрываем диалог для дальнейших тестов
    assert web_tables_page.is_modal_visible(), "Модальное окно уже закрыто — кнопка закрытия недоступна"
    web_tables_page.safe_click(web_tables_page.btn_close_modal)
    time.sleep(0.5)  # Ждём закрытия

    # d. Заполнение всех полей и нажатие Submit
    test_data = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "age": "30",
        "salary": "50000",
        "department": "IT"
    }

    initial_table_data = web_tables_page.get_table_data()
    initial_row_count = len(initial_table_data)

    web_tables_page.add_new_record(**test_data)

    # Ждём обновления таблицы и получаем новые данные
    updated_table_data = web_tables_page.wait_for_table_update(initial_row_count)
    added_record = updated_table_data[-1]  # Последняя запись в таблице

    # Проверяем, что данные совпадают с введёнными
    assert test_data["first_name"] in added_record, "Имя не соответствует введённому"
    assert test_data["last_name"] in added_record, "Фамилия не соответствует введённой"
    assert test_data["email"] in added_record, "Email не соответствует введённому"
    assert test_data["age"] in added_record, "Возраст не соответствует введённому"
    assert test_data["salary"] in added_record, "Зарплата не соответствует введённой"
    assert test_data["department"] in added_record, "Отдел не соответствует введённому"

    # e. Клик на карандаш (редактирование)
    # Получаем актуальный список кнопок редактирования после добавления записи
    edit_buttons = web_tables_page.edit_buttons.find_elements()
    assert len(edit_buttons) > 0, "Кнопки редактирования не найдены после добавления записи"

    # Редактируем последнюю запись (новую)
    last_row_index = len(updated_table_data) - 1
    web_tables_page.edit_record(last_row_index, new_first_name="UpdatedTest")


    # f. Проверка обновления данных
    time.sleep(2)
    final_table_data = web_tables_page.get_table_data()
    updated_record = final_table_data[last_row_index]

    assert "UpdatedTest" in updated_record, "Имя не было обновлено после редактирования"
    print("Редактирование прошло успешно — запись обновлена")

    # g. Удаление записи (опционально)
    web_tables_page.delete_record(last_row_index)
    time.sleep(1)

    # Проверка удаления
    table_after_deletion = web_tables_page.get_table_data()
    assert len(table_after_deletion) == initial_row_count, "Запись не была удалена из таблицы"
    print("Удаление прошло успешно — запись удалена")