from pages.base_page import BasePage
from components.components import WebElement
import time

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_submenu = WebElement(driver, '.btn btn-primary')

        self.icon_home = WebElement(driver, '#root > header > a > img')

    def visit(self):
        self.driver.get(self.base_url)

    @classmethod
    def is_page_available(cls, driver):
        try:
            temp_page = cls(driver)
            temp_page.visit()
            time.sleep(3)
            return temp_page.btns_submenu.exist()
        except Exception:
            return False