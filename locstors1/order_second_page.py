from selenium.webdriver.common.by import By

class SecondOrderPage:
    date_input = By.XPATH, '//input[contains(@placeholder,"* Когда привезти самокат")]'
    calendar_select = By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--014"][contains(.,"14")]'
    time_for_rent = By.XPATH, '//div[@class="Dropdown-placeholder"][contains(.,"* Срок аренды")]'
    first_checkbox = By.XPATH, '//label[@for="black"][contains(.,"чёрный жемчуг")]'
    second_checkbox = By.XPATH, '//label[contains(.,"серая безысходность")]'
    commentary_input = By.XPATH, '//input[contains(@placeholder,"Комментарий для курьера")]'
    back_button = By.XPATH, '//button[contains(.,"Назад")]'
    order_button = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][contains(.,"Заказать")]'
    choose_time_for_rent = By.XPATH, '//div[@class="Dropdown-option"][contains(.,"двое суток")]'
    yes_button = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"][contains(.,"Да")]'
    no_button = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"][contains(.,"Нет")]'
    modal_title = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"][contains(.,"Хотите оформить заказ?")]'
    finish_title = By.XPATH, '//div[contains(@class,"Order_ModalHeader__3FDaJ")]'
    check_button = By.XPATH, '//button[contains(.,"Посмотреть статус")]'