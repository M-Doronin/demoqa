import time
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
import pytest


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    pages = pages(browser)
    pages.visit()
    time.sleep(2)

    assert pages.viewport.exist()
    assert pages.viewport.get_dom_attribute('name') == 'viewport'
    assert pages.viewport.get_dom_attribute('content') == 'width=device-width, initial-scale=1.0'
