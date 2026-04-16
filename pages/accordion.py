from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_1_heading = WebElement(driver, '#section1Heading')
        self.section_2_heading = WebElement(driver, '#section2Heading')
        self.section_3_heading = WebElement(driver, '#section3Heading')

        self.section_1_content = WebElement(driver, '#section1Content > p')
        self.section_2_content_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_2_content_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_3_content = WebElement(driver, '#section3Content > p')

    def is_section_1_content_visible(self):
        return self.section_1_content.visible()

    def click_section_1_heading(self):
        self.section_1_heading.click()

    def is_section_2_content_1_hidden(self):
        return not self.section_2_content_1.visible()

    def is_section_2_content_2_hidden(self):
        return not self.section_2_content_2.visible()

    def is_section_3_content_hidden(self):
        return not self.section_3_content.visible()