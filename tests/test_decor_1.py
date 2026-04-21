import pytest
from pages.radio import Radio


@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_1(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'Yes'

    radio.impressive.click_force()
    assert radio.text.get_text() == 'Impressive'

    assert 'disabled' in radio.no.get_dom_attribute('class')