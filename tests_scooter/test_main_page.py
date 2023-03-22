import allure

from locstors1.test_file_pom import ScooterMainPage


@allure.title('Проверка 1го вопроса')
def test_first_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    assert main_page.text_first_que()
    main_page.click_first_question()
    assert main_page.text_first_ansver()


@allure.title('Проверка 2го вопроса')
def test_second_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_second_question()
    assert main_page.text_second_que()
    assert main_page.text_second_ansver()


@allure.title('Проверка 3го вопроса')
def test_fird_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_fird_question()
    assert main_page.text_fird_que()
    assert main_page.text_fird_ansver()


@allure.title('Проверка 4го вопроса')
def test_fourth_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_fourth_question()
    assert main_page.text_fourth_que()
    assert main_page.text_fourth_ansver()


@allure.title('Проверка 5го вопроса')
def test_fifth_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_fifth_question()
    assert main_page.text_fifth_que()
    assert main_page.text_fifth_ansver()


@allure.title('Проверка 6го вопроса')
def test_sixth_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_sixth_question()
    assert main_page.text_sixth_que()
    assert main_page.text_six_ansver()


@allure.title('Проверка 7го вопроса')
def test_seventh_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_seventh_question()
    assert main_page.text_seventh_que()
    assert main_page.text_seventh_ansver()


@allure.title('Проверка 8го вопроса')
def test_eighth_question(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_eighth_question()
    assert main_page.text_eight_que()
    assert main_page.text_eighth_ansver()


@allure.title('Проверка оформления заказа из кнопки на странице')
def test_order_from_main(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_order_button()
    main_page.fill_first_page()
    main_page.fill_second_page()


@allure.title('Проверка оформления заказа из хедера с заполнением полей')
def test_order_from_header(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_small_order_button()
    main_page.fill_first_page()
    main_page.fill_second_page()


@allure.title('Проверка перехода со страницы заказа по лого "Яндекс"')
def test_back_to_ya_from_logo(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_order_button()
    main_page.click_logo_yandex()


@allure.title('Проверка перехода со страницы заказа по лого "Самокат"')
def test_back_to_main_from_logo(browser):
    main_page = ScooterMainPage(browser)
    main_page.check_cookie()
    main_page.click_order_button()
    main_page.click_logo_scooter()
