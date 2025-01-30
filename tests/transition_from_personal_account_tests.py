from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import MainPage
from locators import PersonalAccountPage


class TestTransitionFromPersonalAccount:

    def test_success_transition_from_personal_account_to_constructor(self, driver, authorized_driver):
        """Проверка перехода из личного кабинета в конструктор"""
        driver = authorized_driver

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))
        driver.find_element(*MainPage.personal_account_button).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PersonalAccountPage.order_history_btn))
        driver.find_element(*MainPage.constructor_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.buns_btn))

        assert driver.current_url == Urls.MAIN_PAGE

    def test_success_transition_from_personal_account_to_logo(self, driver, authorized_driver):
        """Проверка перехода по клику из личного кабинета на логотип"""
        driver = authorized_driver

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))
        driver.find_element(*MainPage.personal_account_button).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PersonalAccountPage.order_history_btn))
        driver.find_element(*MainPage.logo_img).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.buns_btn))

        assert driver.current_url == Urls.MAIN_PAGE