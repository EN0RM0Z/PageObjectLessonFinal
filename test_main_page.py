import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

# Проверяем наличие ссылки на страницу логина.
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    # Комбинирование обращений к разным страницам.
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # Открываем Page Object - 'MainPage', передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем link
        page.go_to_login_page()          # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # Открываем Page Object - 'LoginPage', передаем в конструктор экземпляр драйвера и url адрес
        login_page.should_be_login_page() # Выполняем ряд тестов не уходя со страницы


def test_guest_should_be_login_link_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_be_password_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_password_form()


def test_guest_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


# Проверка пустой корзины с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket() # Клик по кнопке корзины
    page.guest_the_go_to_checkout_button_is_not_showing_up() # Проверяю отсутствие картинки товара.
    page.guest_there_is_a_text_that_the_cart_is_empty() # Проверка наличия элемента с текстом о пустой корзине.
