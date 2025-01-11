from selenium.webdriver.common.by import By

class SignUpPageLocators:
    sign_up_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    name_input = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    email_input = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    incorrect_password = (By.XPATH, ".//p[text()= 'Некорректный пароль']")
    sign_in_btn = (By.XPATH, ".//a[text() = 'Войти']")

class SignInPageLocators:
    sign_in_btn = (By.XPATH, ".//button[text() = 'Войти']")
    name_input = (By.XPATH, ".//input[@name = 'name']")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")

class MainPage:
    sign_in_to_account = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    place_order = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    buns_btn = (By.XPATH, ".//span[text() = 'Булки']")
    buns_section = (By.XPATH, ".//h2[text() = 'Булки']")
    sauces_btn = (By.XPATH, ".//span[text() = 'Соусы']")
    sauces_section = (By.XPATH, ".//h2[text() = 'Соусы']")
    fillings_btn = (By.XPATH, ".//span[text() = 'Начинки']")
    fillings_section = (By.XPATH, ".//h2[text() = 'Начинки']")
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")
    logo_img = (By.TAG_NAME, "svg")

class ForgotPasswordPage:
    sign_in_btn = (By.XPATH, ".//a[text() = 'Войти']")

class PersonalAccountPage:
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")






