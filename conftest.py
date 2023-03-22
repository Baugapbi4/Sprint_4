import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def browser():
    # service = Service(executable_path='E:\Program Files\geckodriver-v0.32.2-win32')
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()