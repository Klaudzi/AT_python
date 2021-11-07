import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск браузера при начале каждого теста
        self.driver = webdriver.Firefox()
    def test_mySearch1_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://bugs.python.org
        driver.get("https://bugs.python.org/")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # получение элемента страницы
        elem = driver.find_element_by_xpath("//form/input[2]")
        # ждем 5 секунд
        time.sleep(5)
        # набор значения для поиска
        elem.send_keys("45243")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия строки на странице с результатами поиска
        self.assertIn("Python Software Foundation", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)

    def test_mySearch2_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://bugs.python.org
        driver.get("https://bugs.python.org/")
        elem = driver.find_element_by_link_text("Список пользователей")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_id("realname")
        elem.send_keys("Jim")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Python Software Foundation", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)

    def test_my3_breadcrumbs(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # получаем список ссылок в меню top
        elems = driver.find_elements_by_css_selector('#top .menu li a')

        # выписываем названия и ссылки в отдельные списки
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки
        for i in range(len(href_list)):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # проверка наличия в пунктах меню
            # наличия названия  пункта
            self.assertIn('Community',name_list)

            time.sleep(1)


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
