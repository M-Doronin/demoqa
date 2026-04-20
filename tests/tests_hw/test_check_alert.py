import time
import pytest
from pages.alerts import Alerts
from components.components import WebElement

def test_timer_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    timer_alert_button = WebElement(browser, '#timerAlertButton')
    assert timer_alert_button.exist()

    timer_alert_button.click()

    time.sleep(6)

    alert = alert_page.alert()
    assert alert

    alert.accept()

    assert not alert_page.alert()