from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, ".header:nth-child(1) > a:nth-child(1) > img:nth-child(1)")

    def exist_icon(self):

        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True