import strip as strip
from time import sleep
import allure
from selenium.webdriver import Keys
from locstors1.main_page import MainPageScooter
from locstors1.cookie import CookiePopUp
from locstors1.order_first_page import FirstOrderPage
from generation import name_of_user
from generation import lastname_of_user
from generation import adress
from generation import random_phone
from generation import commentary
from generation import random_date
from locstors1.order_second_page import SecondOrderPage
from locstors1.header import HeaderOfPages

class ScooterMainPage:
    def __init__(self, driver):
        self.driver = driver

    # клик по кнопке "Заказать"
    def click_order_button(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        # sleep(4)
        return self.driver.find_element(*MainPageScooter.order_button).click()

    def text_order_button(self):
        return self.driver.find_element(*MainPageScooter.order_button).text

    # получить заголовок
    def title_of_page(self):
        return self.driver.find_element(*MainPageScooter.title_on_main_page).text

    # клик по вопросу №1
    def click_first_question(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        return self.driver.find_element(*MainPageScooter.first_question).click()
    # текст из вопроса №1
    @allure.step('Проверка текста ответа на вопрос')
    def text_first_ansver(self):
        return self.driver.find_element(*MainPageScooter.first_answer).text == 'Сутки — 400 рублей. Оплата курьеру ' \
                                                                               '— наличными или картой.',\
            ('Текст не соотвествует ожидаемому')
    # текст вопроса №1
    @allure.step('Проверка текста вопроса')
    def text_first_que(self):
        return self.driver.find_element(*MainPageScooter.first_question).text == 'Сколько это стоит? И как оплатить?',\
            ('Текст не соотвествует ожидаемому')

    # клик по вопросу №2
    def click_second_question(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        return self.driver.find_element(*MainPageScooter.second_question).click()
    # текст из вопроса №2
    @allure.step('Проверка текста ответа на вопрос')
    def text_second_ansver(self):
        return self.driver.find_element(*MainPageScooter.second_answer).text == 'Пока что у нас так: один заказ —' \
          ' один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',\
            ('Текст не соотвествует ожидаемому')
    # текст вопроса №2
    @allure.step('Проверка текста вопроса')
    def text_second_que(self):
        return self.driver.find_element(*MainPageScooter.second_question).text == 'Хочу сразу несколько самокатов!' \
                                                                                  ' Так можно?',\
            ('Текст не соотвествует ожидаемому')

    # клик по вопросу №3
    def click_fird_question(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        return self.driver.find_element(*MainPageScooter.fird_question).click()
    # текст из вопроса №3
    @allure.step('Проверка текста ответа на вопрос')
    def text_fird_ansver(self):
        return self.driver.find_element(*MainPageScooter.fird_answer).text == 'Допустим, вы оформляете заказ на 8 мая.' \
        ' Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента,' \
        ' когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30,' \
        ' суточная аренда закончится 9 мая в 20:30.', ('Текст не соотвествует ожидаемому')
    # текст вопроса №3
    @allure.step('Проверка текста вопроса')
    def text_fird_que(self):
        # self.driver.find_element(self.click_fird_question())
        return self.driver.find_element(*MainPageScooter.fird_question).text == 'Как рассчитывается время аренды?'

    # клик по вопросу №4
    def click_fourth_question(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        return self.driver.find_element(*MainPageScooter.fourth_question).click()
    # текст из вопроса №4
    @allure.step('Проверка текста ответа на вопрос')
    def text_fourth_ansver(self):
        return self.driver.find_element(*MainPageScooter.fourth_answer).text
    # текст вопроса №4
    @allure.step('Проверка текста вопроса')
    def text_fourth_que(self):
        return self.driver.find_element(*MainPageScooter.fourth_question).text == 'Можно ли заказать самокат прямо на сегодня?'
    # клик по вопросу №5
    def click_fifth_question(self):
        self.driver.execute_script("window.scrollTo(0, 2300)")
        return self.driver.find_element(*MainPageScooter.fifth_question).click()
    # текст из вопроса №5
    @allure.step('Проверка текста ответа на вопрос')
    def text_fifth_ansver(self):
        return self.driver.find_element(*MainPageScooter.fifth_answer).text == 'Пока что нет!' \
        'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',\
            ('Текст не соотвествует ожидаемому')
    # текст вопроса №5
    @allure.step('Проверка текста вопроса')
    def text_fifth_que(self):
        return self.driver.find_element(*MainPageScooter.fifth_question).text == 'Можно ли продлить заказ ' \
                                                                                 'или вернуть самокат раньше?',\
            ('Текст не соотвествует ожидаемому')

    # клик по вопросу №6
    def click_sixth_question(self):
        self.driver.execute_script("window.scrollTo(0, 2300)")
        return self.driver.find_element(*MainPageScooter.sixth_question).click()
    # текст из вопроса №6
    @allure.step('Проверка текста ответа на вопрос')
    def text_six_ansver(self):
        return self.driver.find_element(*MainPageScooter.sixth_answer).text == 'Самокат приезжает к вам с полной' \
        'зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне.' \
                                                                               ' Зарядка не понадобится.', \
            ('Текст не соотвествует ожидаемому')
    # текст вопроса №6
    @allure.step('Проверка текста вопроса')
    def text_sixth_que(self):
        return self.driver.find_element(*MainPageScooter.sixth_question).text =='Вы привозите зарядку вместе' \
                                                                                ' с самокатом?',\
            ('Текст не соотвествует ожидаемому')

    # клик по вопросу №7
    def click_seventh_question(self):
        self.driver.execute_script("window.scrollTo(0, 2300)")
        return self.driver.find_element(*MainPageScooter.seventh_question).click()
    # текст из вопроса №7
    @allure.step('Проверка текста ответа на вопрос')
    def text_seventh_ansver(self):
        return self.driver.find_element(*MainPageScooter.seventh_answer).text == 'Да, пока самокат не привезли. ' \
        'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', \
            ('Текст не соотвествует ожидаемому')
    # текст вопроса №7
    @allure.step('Проверка текста вопроса')
    def text_seventh_que(self):
        return self.driver.find_element(*MainPageScooter.seventh_question).text == 'Можно ли отменить заказ?',\
            ('Текст не соотвествует ожидаемому')

    # клик по вопросу №8
    def click_eighth_question(self):
        self.driver.execute_script("window.scrollTo(0, 2300)")
        sleep(5)
        return self.driver.find_element(*MainPageScooter.eighth_question).click()

    # текст из вопроса №8
    @allure.step('Проверка текста ответа на вопрос')
    def text_eighth_ansver(self):
        return self.driver.find_element(*MainPageScooter.eighth_answer).text == 'Да, обязательно. ' \
            'Всем самокатов! И Москве, и Московской области.',\
            ('Текст не соотвествует ожидаемому')


    # текст вопроса №8
    @allure.step('Проверка текста вопроса')
    def text_eight_que(self):
        return self.driver.find_element(*MainPageScooter.eighth_question).text == 'Я жизу за МКАДом, привезёте?',\
            ('Текст не соотвествует ожидаемому')
    # def order_done(self):
    #     self.driver.find_element(*MainPageScooter.order_button).click()
    #     self.driver.find_element(*FirstOrderPage.name_input).send_keys(name_of_user())
    def check_cookie(self):
        assert self.driver.find_element(*CookiePopUp.text_of_pop_up).text == 'И здесь куки! В общем, мы их используем.'
        return self.driver.find_element(*CookiePopUp.cookie_button).click()

    def select_station(self):
        return self.driver.find_element(*FirstOrderPage.station).click()

    def next_step(self):
        return self.driver.find_element(*FirstOrderPage.next_button).click()
    def click_name_input(self):
        self.driver.find_element(*FirstOrderPage.name_input).click()

    def click_lastname_input(self):
        self.driver.find_element(*FirstOrderPage.lastname_input).click()

    def click_adress_input(self):
        self.driver.find_element(*FirstOrderPage.adress_input).click()
    def click_phone_input(self):
        self.driver.find_element(*FirstOrderPage.phone_input).click()

    def click_station_select(self):
        self.driver.find_element(*FirstOrderPage.placeholder_stantion).click()

    def fill_first_page(self):
        self.click_name_input()
        self.driver.find_element(*FirstOrderPage.name_input).send_keys(name_of_user())
        self.click_lastname_input()
        self.driver.find_element(*FirstOrderPage.lastname_input).send_keys(lastname_of_user())
        self.click_adress_input()
        self.driver.find_element(*FirstOrderPage.adress_input).send_keys(adress())
        self.click_station_select()
        self.select_station()
        self.click_phone_input()
        self.driver.find_element(*FirstOrderPage.phone_input).send_keys(random_phone()) #тут было *generation перед генератором
        return self.next_step()
    def click_finish(self):
        return self.driver.find_element(*SecondOrderPage.order_button).click()
    def click_privious(self):
        return self.driver.find_element(*SecondOrderPage.back_button).click()
    def click_date(self):
        return self.driver.find_element(*SecondOrderPage.date_input).send_keys(Keys.RETURN)
    def choose_calendar(self):
        return self.driver.find_element(*SecondOrderPage.calendar_select)
    def click_rent(self):
        return self.driver.find_element(*SecondOrderPage.time_for_rent).click()
    def click_color_1(self):
        return self.driver.find_element(*SecondOrderPage.first_checkbox).click()
    def click_color_2(self):
        return self.driver.find_element(*SecondOrderPage.second_checkbox).click()
    def click_commentary(self):
        return self.driver.find_element(*SecondOrderPage.commentary_input).click()
    def select_time_rent(self):
        self.driver.find_element(*SecondOrderPage.choose_time_for_rent).click()
    def check_modal_title(self):
        return self.driver.find_element(*SecondOrderPage.modal_title).text == 'Хотите оформить заказ?'
    def click_yes_order(self):
        return self.driver.find_element(*SecondOrderPage.yes_button).click()
    def click_no_order(self):
        return self.driver.find_element(*SecondOrderPage.no_button).click()

    def fill_second_page(self):
        self.click_date()
        self.driver.find_element(*SecondOrderPage.date_input).send_keys('23.03.2023')
        self.click_rent()
        self.select_time_rent()
        self.click_color_2()
        self.click_commentary()
        self.driver.find_element(*SecondOrderPage.commentary_input).send_keys(commentary())
        self.click_finish()
        self.click_yes_order()
        assert 'Заказ оформлен' in self.driver.find_element(*SecondOrderPage.finish_title).text

   # клик по кнопке "Заказать"
    def click_small_order_button(self):
        return self.driver.find_element(*HeaderOfPages.small_order_button).click()

    # клик по лого "Яндекс"
    def click_logo_yandex(self):
        self.driver.find_element(*HeaderOfPages.yandex_logo).click()
        return self.driver.current_url == ''
    # клик по лого "Самокат"
    def click_logo_scooter(self):
        self.driver.find_element(*HeaderOfPages.scooter_logo).click()
        assert 'Самокат' in self.title_of_page()

    # клик по кнопке "Статус"
    def click_status_button(self):
        return self.driver.find_element(*HeaderOfPages.status_button).click()

    # клик по кнопке "Поиск"
    def click_search_button(self):
        self.driver.find_element(*HeaderOfPages.search_button).click()