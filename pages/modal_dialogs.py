from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_submenu = WebElement(driver, '.btn btn-primary')

        self.icon_home = WebElement(driver, '.header:nth-child(1) > a:nth-child(1) > img:nth-child(1)')

    def visit(self):
        self.driver.get(self.base_url)