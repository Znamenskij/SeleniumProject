import allure
from requests import get
import chromedriver_binary
import allure_pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_mos():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.mos.ru")

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    # тест для проверки наличия шапки подвала
    def test_find_footer(self):
        footer = self.driver.find_element(By.TAG_NAME, 'footer')
        assert 'Официальный портал Мэра и Правительства Москвы' in footer.text

    def test_find_header(self):
        header = self.driver.find_element(By.TAG_NAME, 'header')
        assert 'Официальный сайт Мэра Москвы' in header.text

    # тест для проверки количества ссылок
    def test_links_count(self):
        links_object_list = self.driver.find_elements(By.TAG_NAME, 'a')
        assert len(links_object_list) == 237

    def test_links_status_code(self):
        links_object_list = self.driver.find_elements(By.TAG_NAME, 'a')

        # проверяем ссылки на код 200 и не имеющих такого статуса записываем в список с кортежами
        false_links = list()
        for link in links_object_list:
            request = get(link.get_attribute('href'))
            if not request.status_code == 200:
                false_links.append((link.get_attribute('href'), request.status_code))

        # проверяем количество ссылок с кодом не 200 и если они есть, то выводим Exception
        if len(false_links) != 0:
            raise Exception(f'Ссылки имеющие код не 200: {len(false_links)} \n {false_links}')

    # тест для перехода по ссылкам и проверки адресной строки
    def test_go_to_links(self):
        links_object_list = self.driver.find_elements(By.TAG_NAME, 'a')

        false_links = list()
        for link in links_object_list:
            request = get(link.get_attribute('href'))
            if (link.get_attribute('href') != request.url) and ((link.get_attribute('href') + '/') != request.url):
                false_links.append((link.get_attribute('href'), request.url))

        if len(false_links) != 0:
            raise Exception(f'Ссылки, которые не совпадают после перехода: {len(false_links)} \n {false_links}')


