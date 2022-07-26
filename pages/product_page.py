import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # Добавить в карзину книгу
    def go_to_button_add_book(self):
        button_add_book = self.browser.find_element(*ProductPageLocators.ADD_BOOK_BUTTON)
        button_add_book.click()

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present()) # Явное ожидание алерта
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present()) # Явное ожидание алерта
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

        time.sleep(0)

    def checking_button_checkout(self):
        # Проверка появления кнопки Оформить
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, ProductPageLocators.CHECK_BUTTON_CLICKABILITY)))

    def checking_book_added_to_cart_price(self):
        price_in_the_cart = self.browser.find_element(By.XPATH, ProductPageLocators.PRICE_IN_THE_CART).text
        stock_price_book = self.browser.find_element(By.XPATH, ProductPageLocators.STOCK_PRICE_BOOK).text
        print(f'Price book, stock / added: - {stock_price_book} / {price_in_the_cart}')
        assert price_in_the_cart == stock_price_book, 'The PRICE of the book in stock is different from the price in the cart'

    @pytest.mark.xfail
    def checking_book_added_to_cart_name(self):
        name_in_the_cart = self.browser.find_element(By.XPATH, ProductPageLocators.NAME_IN_THE_CART).text
        stock_name_book = self.browser.find_element(By.XPATH, ProductPageLocators.STOCK_NAME_BOOK).text
        print(f'Name book, stock / added: - {stock_name_book} / {name_in_the_cart}')
        assert stock_name_book == name_in_the_cart, 'The NAME of the book in stock is different from the price in the cart'

    def output_current_link(self):
        name_current_link = self.browser.current_url
        print(f'Текущая страница: - {name_current_link}')

    # Проверяем, что нет сообщения об успехе, после добавления товара в корзину.
    # is_not_element_present - падет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be / Сообщение об успехе отображается, но не должно"

    # Проверяем, что нет сообщения об успехе,  добавления товара в корзину.
    # is_disappeared - будет ждать до тех пор, пока элемент не исчезнет.
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Есть сообщение об успехе, но оно не должно было появлятся"

