import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    # Ожидаем, что в корзине нет товаров. Проверяю отсутствие картинки товара.
    def guest_the_go_to_checkout_button_is_not_showing_up(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ORDERING), \
            "Картинка товара отображается, но не должна"

    # Проверка наличия элемента с текстом о пустой корзине.
    def guest_there_is_a_text_that_the_cart_is_empty(self):
        text_basket_is_empty = self.browser.find_element(*BasketPageLocators.BASKET_TEXT_BASKET_IS_EMPTY)
        text_cart_is_empty = text_basket_is_empty.get_attribute('id')
        assert 'content_inner' in text_cart_is_empty, 'Нет наличия элемента с текстом о пустой корзине'


