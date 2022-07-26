import math
from selenium import webdriver
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url
    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.get(self.url)

    # Проверяем наличие ссылки на страницу логина.
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    # Если элемент найден возвращаем True, иначе -
    # - перехватываем ошибку 'NoSuchElementException' и присваиваем False
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Кликаем по ссылке логин / регистрация
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Кликаем по кнопке 'посмотреть корзину'
    def guest_clik_button_see_basket(self):
        button_basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        text_atribut_button_basket = button_basket.get_attribute('href')
        assert 'basket' in text_atribut_button_basket, 'No view cart button /  Нет кнопки - посмотреть корзину'
        button_basket.click()


    # Метод проверки проверяет, что элемент не появляется на странице в течение времени.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Метод ПРОВЕРКИ что какой-то элемент исчезает.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Проверка того, что пользователь залогинен.
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



