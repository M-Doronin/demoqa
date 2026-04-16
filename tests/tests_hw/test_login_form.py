import time
from pages.form_page import FormPage

def test_fill_state_and_city(browser):
    form_page = FormPage(browser)
    form_page.visit()

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovoch')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('text')

    form_page.state.click_force()
    time.sleep(1)
    form_page.state_input.send_keys('NCR')
    time.sleep(1)
    form_page.state_option.click_force()

    form_page.city.click_force()
    time.sleep(1)
    form_page.city_input.send_keys('Delhi')
    time.sleep(1)
    form_page.city_option.click_force()

    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()