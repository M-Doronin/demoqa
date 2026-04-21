from pages.base_page import BasePage
from components.components import WebElement

class Radio(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, 'input[type="radio"][id="yesRadio"]')
        self.impressive = WebElement(driver, 'input[type="radio"][id="impressiveRadio"]')
        self.no = WebElement(driver, 'input[type="radio"][id="noRadio"]')
        self.text = WebElement(driver, '.text-success')