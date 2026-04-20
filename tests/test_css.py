from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()

    assert text_box.submit.check_css('color', 'rgba(255, 255, 255, 1)')

    assert text_box.submit.check_css('backgroundColor', 'rgba(13, 110, 253, 1)')
    assert text_box.submit.check_css('borderColor', 'rgb(13, 110, 253)')
