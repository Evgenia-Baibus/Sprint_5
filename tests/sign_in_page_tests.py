from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import SignInPageLocators, SignUpPageLocators
from locators import MainPage
from locators import ForgotPasswordPage
from data import SignInData
from tests.conftest import driver
from urls import Urls

class TestSignInPage:

    def test_sign_in_success_via_login_to_account_button(self, driver):
        """Проверка входа по кнопке «Войти в аккаунт» на главной странице"""
        driver = driver
        driver.get(Urls.MAIN_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.sign_in_to_account))
        driver.find_element(*MainPage.sign_in_to_account).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
        driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
        driver.find_element(*SignInPageLocators.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))

        assert driver.current_url == Urls.MAIN_PAGE



    def test_sign_in_success_via_personal_account(self, driver):
        """Проверка через кнопку «Личный кабинет» на главной странице"""
        driver = driver
        driver.get(Urls.MAIN_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.sign_in_to_account))
        driver.find_element(*MainPage.personal_account_button).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
        driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
        driver.find_element(*SignInPageLocators.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))

        assert driver.current_url == Urls.MAIN_PAGE

    def test_sign_in_success_via_registration_form(self, driver):
        """Проверка входа через кнопку в форме регистрации"""
        driver = driver
        driver.get(Urls.SIGN_UP_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignUpPageLocators.sign_in_btn))
        driver.find_element(*SignUpPageLocators.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
        driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
        driver.find_element(*SignInPageLocators.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))

        assert driver.current_url == Urls.MAIN_PAGE


    def test_sign_in_success_via_recover_password_form(self, driver):
        """Проверка входа через кнопку в форме восстановления пароля"""
        driver = driver
        driver.get(Urls.FORGOT_PASSWORD)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(ForgotPasswordPage.sign_in_btn))
        driver.find_element(*ForgotPasswordPage.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
        driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
        driver.find_element(*SignInPageLocators.sign_in_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(*MainPage.place_order))

        assert driver.current_url == Urls.MAIN_PAGE





