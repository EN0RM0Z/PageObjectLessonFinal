import pytest
import time
from .pages.main_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

bugged_link = ['7']

# Перечисляем номера. Маркируем пропуск плохого теста.
@pytest.mark.need_review
@pytest.mark.parametrize('number_url', ['0', '1', '2', '3', '4', '5', '6',
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  '8', '9'])
# Переходим на страницу с товаром
def test_guest_can_add_product_to_basket(browser, number_url):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(number_url)}'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.solve_quiz_and_get_code()
    page.checking_button_checkout() # Проверка появления кнопки Оформить
    page.checking_book_added_to_cart_price() # Проверка соответствия цены на складе и в корзине
    page.checking_book_added_to_cart_name() # Проверка соответствия имени товара на складе и в корзине
    page.output_current_link()

# отрицательные проверки
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.solve_quiz_and_get_code()
    # Негативный сценарий: - Проверяем, что нет сообщения об успехе
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket() # Проверка что нет 'сообщения об успехе' добавления в корзину.


@pytest.mark.xfail
def test_message_add_in_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.solve_quiz_and_get_code()
    # Негативный сценарий: - Проверяем, что нет сообщения об успехе
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# Проверка пустой корзины со страницы товара
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    page.guest_the_go_to_checkout_button_is_not_showing_up()
    page.guest_there_is_a_text_that_the_cart_is_empty()

@pytest.mark.reg
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_button_add_book()
        page.test_guest_cant_see_success_message_after_adding_product_to_basket()  # Проверка что нет 'сообщения об успехе' добавления в корзину.


    # Переходим на страницу с товаром
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_button_add_book()
        page.solve_quiz_and_get_code()
        page.checking_button_checkout()  # Проверка появления кнопки Оформить
        page.checking_book_added_to_cart_price()  # Проверка соответствия цены на складе и в корзине
        page.checking_book_added_to_cart_name()  # Проверка соответствия имени товара на складе и в корзине
        page.output_current_link()
