import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver



class FirstOrderPage:
    # заголовок 1й страницы
    title_of_first_page = By.CLASS_NAME, "Order_Header__BZXOb"
    name_input = By.XPATH, '//input[contains(@placeholder,"* Имя")]'
    name_error = By.XPATH,\
                   '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6"]'\
                   '[contains(.,"Введите корректное имя")]'
    lastname_input = By.XPATH, '//input[contains(@placeholder,"* Фамилия")]'
    lastname_error = By.XPATH, '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6"]'\
                                '[contains(.,"Введите корректную фамилию")]'
    adress_input = By.XPATH, '//input[contains(@placeholder,"* Адрес: куда привезти заказ")]'
    adress_error = By.XPATH, '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6"]'\
                              '[contains(.,""Введите корректный адрес")]'
    phone_input = By.XPATH, '//input[contains(@placeholder,"* Телефон: на него позвонит курьер")]'
    phone_error = By.XPATH, '//div[@class="Input_ErrorMessage__3HvIb Input_Visible___syz6"]'\
                             '[contains(.,"Введите корректный номер")]'
    placeholder_stantion = By.XPATH, '//input[contains(@placeholder,"* Станция метро")]'

    station_error = By.XPATH, '//div[@class=''Order_MetroError__1BtZb''][contains(.,"Выберите станцию")]'
    first_station = By.XPATH, '//input[contains(@value,"Бульвар Рокоссовского")]'
    station = By.XPATH, '//button[@value="5"]'
    next_button = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][contains(.,"Далее")]'

