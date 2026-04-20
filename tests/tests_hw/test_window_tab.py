import pytest
import time
from pages.links import LinksPage
from components.components import WebElement

def test_home_link_new_tab(browser):
    links_page = LinksPage(browser)
    links_page.visit()

    home_link = WebElement(browser, 'a#simpleLink')

    assert home_link.exist()

    link_text = home_link.get_text()
    assert link_text == 'Home'

    expected_href = 'https://demoqa.com'
    actual_href = home_link.get_dom_attribute('href')

    normalized_actual_href = actual_href.rstrip('/')
    assert normalized_actual_href == expected_href

    original_windows = browser.window_handles
    original_window_count = len(original_windows)

    home_link.click()

    time.sleep(2)

    current_windows = browser.window_handles
    current_window_count = len(current_windows)

    assert current_window_count == original_window_count + 1

    new_window_handle = current_windows[-1]
    browser.switch_to.window(new_window_handle)

    time.sleep(2)

    current_url = browser.current_url

    normalized_current_url = current_url.rstrip('/')

    assert normalized_current_url == expected_href

    browser.close()

    browser.switch_to.window(original_windows[0])