import time
from pages.form_page import FormPage

def test_form_validation(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'

    email_pattern = form_page.user_email.get_dom_attribute('pattern')
    expected_pattern = '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'
    assert email_pattern == expected_pattern, f"Неверный pattern: {email_pattern}"

    form_page.btn_submit.click_force()
    time.sleep(2)

    form_element = form_page.form.find_element()
    class_attribute = form_element.get_attribute('class')
    assert 'was-validated' in class_attribute, "Класс 'was-validated' не найден у формы"