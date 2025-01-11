from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import SignUpPageLocators
from locators import SignInPageLocators
from data import RandomData

from selenium.webdriver.common.by import By

class TestSignUpPage:

    def test_sign_up_success_with_valid_data(self, driver):
        """Проверка успешной регистрации"""
        driver = driver
        driver.get(Urls.SIGN_UP_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignUpPageLocators.sign_up_btn))

        driver.find_element(*SignUpPageLocators.name_input).send_keys(RandomData.name)
        driver.find_element(*SignUpPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*SignUpPageLocators.password_input).send_keys(RandomData.password)
        driver.find_element(*SignUpPageLocators.sign_up_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))

        assert driver.current_url == Urls.SIGN_IN_PAGE


    def test_sign_up_error_with_invalid_password(self, driver):
        """Проверка ошибки для некорректного пароля (менее шести символов)"""
        driver = driver
        driver.get(Urls.SIGN_UP_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignUpPageLocators.sign_up_btn))

        driver.find_element(*SignUpPageLocators.name_input).send_keys(RandomData.name)
        driver.find_element(*SignUpPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*SignUpPageLocators.password_input).send_keys("1")
        driver.find_element(*SignUpPageLocators.sign_up_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignUpPageLocators.incorrect_password))

        assert driver.current_url == Urls.SIGN_UP_PAGE