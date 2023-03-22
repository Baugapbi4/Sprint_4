from selenium.webdriver.common.by import By

class HeaderOfPages:
    yandex_logo = By.XPATH, '//img[contains(@alt,"Yandex")]'
    scooter_logo = By.XPATH, '//img[@alt="Scooter"]'
    small_order_button = By.CLASS_NAME, 'Button_Button__ra12g'
    status_button = By.XPATH, '//button[@class=''Header_Link__1TAG7''][contains(.,''Статус заказа'')]'
    input_number_of_order = By. XPATH, '//input[contains(@type,''text'')]'
    search_button = By.XPATH, '//button[@class=''Button_Button__ra12g Header_Button__28dPO''][contains(.,''Go!'')]'




