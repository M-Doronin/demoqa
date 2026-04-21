import time

from pages.progress_bar import Progress


def test_progress_bar(browser):
    page = Progress(browser)

    page.visit()
    time.sleep(2)

    page.button.click()

    while True:
        if page.bar.get_dom_attribute('aria-valuenow') == '51':
            page.button.click()
            break

    time.sleep(2)