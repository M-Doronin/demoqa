import time
from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()
    time.sleep(2)

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    time.sleep(3)

    current_url = koup_add.get_url()
    assert koup_add.equal_url(), f"Ожидаемый URL: {koup_add.base_url}, текущий: {current_url}"

    assert koup_add.btn_add.get_text() == 'Add Element'
    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        koup_add.btn_add.click()
        time.sleep(1)

    all_buttons = koup_add.btns_delete.find_elements()
    delete_buttons = [btn for btn in all_buttons if btn.text.strip() == 'Delete']
    actual_count = len(delete_buttons)

    assert actual_count == 4, f"Ожидали 4 кнопки Delete, найдено: {actual_count}"

    for element in delete_buttons:
        assert element.text.strip() == 'Delete', f"Неверный текст на кнопке: '{element.text}'"

    while delete_buttons:
        delete_buttons[0].click()
        time.sleep(0.5)
        all_buttons = koup_add.btns_delete.find_elements()
        delete_buttons = [btn for btn in all_buttons if btn.text.strip() == 'Delete']

    all_buttons = koup_add.btns_delete.find_elements()
    remaining_delete_buttons = [btn for btn in all_buttons if btn.text.strip() == 'Delete']
    assert len(remaining_delete_buttons) == 0, "Кнопки Delete не исчезли после клика"