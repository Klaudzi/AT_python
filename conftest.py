import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'https://bugs.python.org/'
link1 = "http://www.python.org"

@pytest.fixture()
def browser():
    # запуск Firefox при начале каждого теста (до yield)
    print("\nstart firefox browser for test..")
    driver = webdriver.Firefox()
    # открытие страницы при начале каждого теста
    page = driver.get(link)
    # передача драйвера для использования в тесте
    yield driver
    print("\nquit browser..")
    # закрытие браузера после теста (после yield)
    driver.close()

@pytest.fixture()
def browser1():
    # запуск Firefox при начале каждого теста (до yield)
    print("\nstart firefox browser for test..")
    driver = webdriver.Firefox()
    # открытие страницы при начале каждого теста
    page = driver.get(link1)
    # передача драйвера для использования в тесте
    yield driver
    print("\nquit browser..")
    # закрытие браузера после теста (после yield)
    driver.close()

