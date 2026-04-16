import time
from pages.text_box import TextBox


def test_text_box_submission(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    full_name_text = "Test Testovich"
    current_address_text = "Russia, Saint-Petersburg, 1"

    text_box_page.name.send_keys(full_name_text)
    text_box_page.current_address.send_keys(current_address_text)


    text_box_page.btn_submit.click()


    time.sleep(3)

    result_name = text_box_page.result_full_name
    result_address = text_box_page.result_current_address

    assert full_name_text in result_name.get_text(), f"Текст '{full_name_text}' не найден в результате имени"
    assert current_address_text in result_address.get_text(), f"Текст '{current_address_text}' не найден в результате адреса"
