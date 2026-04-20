import pytest
import time
from pages.modal_dialogs import ModalDialogsPage
from components.components import WebElement

def test_modal_functionality(browser):
    """
    Тест-кейс для проверки функциональности модальных окон:
    1. Проверка наличия кнопок Small modal и Large modal
    2. Открытие и закрытие Small modal
    3. Открытие и закрытие Large modal
    """
    modal_dialogs_page = ModalDialogsPage(browser)

    # Попытка открыть страницу
    try:
        modal_dialogs_page.visit()
        time.sleep(3)  # Ожидание загрузки страницы

        # Проверка доступности страницы через наличие ключевого элемента
        if not modal_dialogs_page.btns_submenu.exist():
            pytest.skip("Страница недоступна — не найден ключевой элемент на странице")
    except Exception as e:
        pytest.skip(f"Страница недоступна: {str(e)}")

    # 1. Проверяем наличие кнопок Small modal и Large modal
    small_modal_btn = WebElement(browser, "button#showSmallModal")
    large_modal_btn = WebElement(browser, "button#showLargeModal")

    assert small_modal_btn.exist(), "Кнопка 'Small modal' не найдена на странице"
    assert large_modal_btn.exist(), "Кнопка 'Large modal' не найдена на странице"

    # 2. Проверяем Small modal
    small_modal_btn.click()
    time.sleep(2)  # Ожидание появления модального окна

    # Проверяем появление модального окна Small modal
    small_modal = WebElement(browser, "div#smallModal .modal-content")
    assert small_modal.exist(), "Small modal не появилось после клика"

    # Находим кнопку Close в Small modal
    close_btn_small = WebElement(browser, "div#smallModal button.btn-close")
    assert close_btn_small.exist(), "Кнопка 'Close' не найдена в Small modal"

    # Закрываем Small modal
    close_btn_small.click()
    time.sleep(1)  # Ожидание закрытия окна
    assert not small_modal.exist(), "Small modal не закрылось после клика по кнопке 'Close'"

    # 3. Проверяем Large modal
    large_modal_btn.click()
    time.sleep(2)  # Ожидание появления модального окна

    # Проверяем появление модального окна Large modal
    large_modal = WebElement(browser, "div#largeModal .modal-content")
    assert large_modal.exist(), "Large modal не появилось после клика"

    # Находим кнопку Close в Large modal
    close_btn_large = WebElement(browser, "div#largeModal button.btn-close")
    assert close_btn_large.exist(), "Кнопка 'Close' не найдена в Large modal"

    # Закрываем Large modal
    close_btn_large.click()
    time.sleep(1)  # Ожидание закрытия окна
    assert not large_modal.exist(), "Large modal не закрылось после клика по кнопке 'Close'"