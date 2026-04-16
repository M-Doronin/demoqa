import time
from pages.modal_dialogs import ModalDialogsPage
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btns_submenu.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    browser.refresh()

    modal_dialogs_page.icon_home.click()

    browser.back()

    browser.set_window_size(900, 400)

    browser.forward()

    demo_qa_page = DemoQa(browser)
    assert demo_qa_page.equal_url(), "URL не соответствует главной странице"

    assert browser.title == 'demosite', "Заголовок не соответствует ожидаемому 'demosite'"

    browser.set_window_size(1000, 1000)