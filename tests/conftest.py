import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import SignInPageLocators
from data import SignInData


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    driver.get(Urls.SIGN_IN_PAGE)

    WebDriverWait(driver, 3).until(ec.visibility_of_element_located(SignInPageLocators.sign_in_btn))
    driver.find_element(*SignInPageLocators.name_input).send_keys(SignInData.email)
    driver.find_element(*SignInPageLocators.password_input).send_keys(SignInData.password)
    driver.find_element(*SignInPageLocators.sign_in_btn).click()

    return driver