from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import MainPage
from locators import SignInPageLocators
from locators import PersonalAccountPage

class TestLogoutFromAccount:

    def test_success_log_out(self, driver, authorized_driver):
        """Проверка выхода по кнопке "Выйти" в личном кабинете"""
        driver = authorized_driver

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))
        driver.find_element(*MainPage.personal_account_button).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PersonalAccountPage.order_history_btn))
        driver.find_element(*PersonalAccountPage.exit_btn).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))

        assert driver.current_url == Urls.SIGN_IN_PAGE
