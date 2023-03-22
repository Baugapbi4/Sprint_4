from selenium.webdriver.common.by import By


class CookiePopUp:
    text_of_pop_up = By.XPATH, '//div[contains(@class,"1sbqp")]'
    cookie_button = By.XPATH, '//button[contains(.,"да все привыкли")]'