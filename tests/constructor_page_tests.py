from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urls import Urls
from locators import MainPage


class TestTransitionSectionsConstructorPage:

    def test_success_transition_on_sauces_section(self, driver):
        """Проверка перехода в раздел Соусы"""
        driver = driver
        driver.get(Urls.MAIN_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.buns_btn))
        driver.find_element(*MainPage.sauces_btn).click()

        section_text = driver.find_element(*MainPage.sauces_section).text

        assert section_text == 'Соусы'

    def test_success_transition_on_fillings_section(self, driver):
        """Проверка перехода в раздел Начинки"""
        driver = driver
        driver.get(Urls.MAIN_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.buns_btn))
        driver.find_element(*MainPage.fillings_btn).click()

        section_text = driver.find_element(*MainPage.fillings_section).text

        assert section_text == 'Начинки'

    def test_success_transition_on_buns_section(self, driver):
        """Проверка перехода в раздел Булки"""
        driver = driver
        driver.get(Urls.MAIN_PAGE)

        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.buns_btn))
        driver.find_element(*MainPage.fillings_btn).click()
        driver.find_element(*MainPage.buns_btn).click()

        section_text = driver.find_element(*MainPage.buns_section).text

        assert section_text == 'Булки'





