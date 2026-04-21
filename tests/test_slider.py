from pages.slider import SliderPage
from components.components import WebElement
from selenium.webdriver.common.keys import Keys


def test_slider_v3(browser):
    slider = SliderPage(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.inp.get_dom_attribute('value') == '50'