from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPageScooter:
    # Заголовок
    title_on_main_page = By.XPATH, "//div[@class='Home_Header__iJKdX'][contains(.,'Самокат на пару днейПривезём его прямо к вашей двери, а когда накатаетесь — заберёмОн лёгкий и с мощными колёсами— самое то, чтобы ехать по набережной и нежно барабанить пальцами по рулю')]"
    # текст под заголовком
    text_under_title = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']
    # описание самоката
    about_of_scooter = [By.CLASS_NAME, 'Home_Row__jdQW2']
    # Изображение на главной
    picture_on_main_page = [By.CLASS_NAME, 'Home_Scooter__3YdJy']
    #заголовок "как это рабоатет"
    title_about_order = [By.XPATH, '//div[@class=''Home_SubHeader__zwi_E''][contains(.,''Как это работает'')']
    # шаг 1
    step_first = [By.XPATH, '//div[@class=''Home_Status__YkfmH''][contains(.,''Заказываете самокат'')]']
    # шаг 2
    step_second = [By.XPATH, '//div[@class=''Home_Status__YkfmH''][contains(.,''Курьер привозит самокат'')]']
    # шаг 3
    step_fird = [By.XPATH, '//div[@class=''Home_Status__YkfmH''][contains(.,''Катаетесь'')]']
    # шаг 4
    step_fourth = [By.XPATH, '//div[@class=''Home_Status__YkfmH''][contains(.,''Курьер забирает самокат'')]']
    # кнопка "заказать"
    order_button = By.XPATH, '//button[contains(@class,"1CSJM")]'

    # заголовок вопросов
    title_of_questions = By. XPATH, '//div[@class=''Home_SubHeader__zwi_E''][contains(.,''Вопросы о важном'')]'
    # вопрос 1
    first_question = By. XPATH, '//div[@id="accordion__heading-0"]'
    # вопрос 2
    second_question = By.XPATH, '//div[contains(@aria-controls,"accordion__panel-1")]'
    # вопрос 3
    fird_question = By.XPATH, '//div[@id="accordion__heading-2"]'
    # вопрос 4
    fourth_question = By.XPATH, '//div[@id="accordion__heading-3"]'
    # вопрос 5
    fifth_question = By.XPATH, '//div[@id="accordion__heading-4"]'
    # вопрос 6
    sixth_question = By.XPATH, '//div[@id="accordion__heading-5"]'
    # вопрос 7
    seventh_question = By.XPATH, '//div[@id="accordion__heading-6"]'
    # вопрос 8
    eighth_question = By.XPATH, '//div[@id="accordion__heading-7"]'
    # вопрос 1 раскрыт
    first_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-0"]'
    # вопрос 2 раскрыт
    second_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-1"]'
    # вопрос 3 раскрыт
    fird_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-2"]'
    # вопрос 4 раскрыт
    fourth_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-3"]'
    # вопрос 5 раскрыт
    fifth_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-4"]'
    # вопрос 6 раскрыт
    sixth_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-5"]'
    # вопрос 7 раскрыт
    seventh_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-6"]'
    # вопрос 8 раскрыт
    eighth_question_is_open = By.XPATH, '//div[@aria-controls,"accordion__panel-7"]'
    # ответ 1
    first_answer = By.XPATH, '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или")]'
    # ответ 2
    second_answer = By.XPATH, '//p[contains(text(),"Пока что у нас так: один заказ — один самокат.'\
                               ' Если хотите покататься с друзьями,'\
                               ' можете просто сделать несколько заказов — один за другим.")]'
    # ответ 3
    fird_answer = By.XPATH, '//p[contains(.,"Допустим")]'
    # ответ 4
    fourth_answer = By.XPATH, '//p[contains(.,"Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]'
    # ответ 5
    fifth_answer =By.XPATH, '//p[contains(.,"Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]'
    # ответ 6
    sixth_answer = By.XPATH, '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. ")]'
    # ответ 7
    seventh_answer = By.XPATH, '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, '\
                                'объяснительной записки тоже не попросим. Все же свои.")]'
    # ответ 8
    eighth_answer = By.XPATH, '//p[contains(.,"Да, обязательно. Всем самокатов! И Москве, и Московской области.")]'