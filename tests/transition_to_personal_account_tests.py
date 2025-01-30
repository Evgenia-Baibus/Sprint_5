from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import MainPage
from locators import PersonalAccountPage

class TestTransitionToPersonalAccount:

    def test_success_transition_to_personal_account(self, driver, authorized_driver):
        """Проверка перехода в личный кабинет"""
        driver = authorized_driver

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.place_order))
        driver.find_element(*MainPage.personal_account_button).click()

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PersonalAccountPage.order_history_btn))

        assert driver.current_url == Urls.PROFILE

