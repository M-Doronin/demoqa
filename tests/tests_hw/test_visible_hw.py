import time
import pytest
from pages.accordion import Accordion

@pytest.mark.usefixtures("browser")
class TestVisibleAccordion:

    def test_visible_accordion(self, browser):
        accordion_page = Accordion(browser)

        accordion_page.visit()

        assert accordion_page.is_section_1_content_visible(), \
            "Элемент #section1Content > p должен быть виден при загрузке страницы"

        accordion_page.click_section_1_heading()

        time.sleep(2)

        assert not accordion_page.is_section_1_content_visible(), \
            "Элемент #section1Content > p должен стать невидимым после клика на заголовок"

    def test_visible_accordion_default(self, browser):
        accordion_page = Accordion(browser)

        accordion_page.visit()

        assert accordion_page.is_section_2_content_1_hidden(), \
            "Первый параграф второй секции (#section2Content > p:nth-child(1)) должен быть скрыт по умолчанию"

        assert accordion_page.is_section_2_content_2_hidden(), \
            "Второй параграф второй секции (#section2Content > p:nth-child(2)) должен быть скрыт по умолчанию"

        assert accordion_page.is_section_3_content_hidden(), \
            "Контент третьей секции (#section3Content > p) должен быть скрыт по умолчанию"