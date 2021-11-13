import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestMainPage1():

    def test_mySearch1(self, browser):
        print("start test1")
        elem = browser.find_element_by_xpath("//form/input[2]")
        elem.send_keys("45243")
        # ждем 5 секунд
        time.sleep(1)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        elem1 = browser.find_element(By.ID, 'breadcrumb')
        # проверка наличия строки на странице с результатами поиска
        assert elem1.text == 'Задача 45243', "К сожалению - не так"
        print("finish test1")
        # ждем 5 секунд
        time.sleep(5)

    def test_mySearch2(self, browser):
        print("start test2")
        elem = browser.find_element(By.LINK_TEXT,"Список пользователей")
        elem.click()
        time.sleep(2)
        elem = browser.find_element_by_id("realname")
        elem.send_keys("Jim")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        elem1 = browser.find_element(By.ID, 'breadcrumb')
        # проверка наличия строки на странице с результатами поиска
        assert 'Список пользователей' == elem1.text, "К сожалению - не так"
        print("finish test2")
        # ждем 5 секунд
        time.sleep(2)

    def test_breadcrumbs(self, browser1):
        print("start test3")
        elems = browser1.find_elements_by_css_selector('#top .menu li a')

        # выписываем названия и ссылки в отдельные списки
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки
        for i in range(len(href_list)):
            # переходим по ссылке
            browser1.get(
                href_list[i]
            )
            # проверка наличия в пунктах меню
            # наличия названия  пункта
            assert 'Community' in name_list, "К сожалению - не так"
        print("finish test3")
        # ждем 5 секунд
        time.sleep(2)