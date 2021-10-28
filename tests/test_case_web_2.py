from pages.element_obj import WebElementObj
from pages.google_page import GooglePageHelper
from pages.base_app import BasePage
from pages.playmarket_page import PlayMarketPageHelper
from selenium.webdriver import Chrome
from tests.test_base import BaseTest
import time

# Настройка данных тест-кейса

QUERY = 'ivi'
RESULTS_URL_CLASS = 'yuRUbf'

PLAY_MARKET_QUERY = 'play.google.com'
PAGE_NUMBER = 5
XPATH_CLASS_CLICKABLE = 'yuRUbf'
XPATH_CLASS_CONTEXT = 'tF2Cxc'
PM_PAGE_RATING_CLASS = 'BHMmbe'


class TestScenario2(BaseTest):
    """1 неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            на первых 5 страницах находит ссылки на приложение ivi в play.google.com
            убеждается, что рейтинг приложения на кратком контенте страницы совпадает с рейтингом при переходе"""

    def test_step1_goto_google_site(self):
        self.search_page = GooglePageHelper(self.driver)
        self.search_page.go_to_site()

    def test_step2_query_ivi(self):
        # Поиск по заданному значению QUERY
        self.search_page = GooglePageHelper(self.driver)
        self.search_page.search(QUERY)
        # Смена семантики
        self.result_page = self.search_page
        # Подсчет длины списка результатов для валидации наличия результата
        assert self.result_page.query_count(RESULTS_URL_CLASS) > 0

    def test_step3_inspect_result_for_pm_site(self):
        self.results = GooglePageHelper(self.driver)
        # Получить кликабельный элемент с совпадением в адресе ссылки play.google.com
        self.play_market_link = self.results.set_browse_result_pages(QUERY, PLAY_MARKET_QUERY, PAGE_NUMBER)

        # Получить родительский элемент с текстом содержащим рейтинг, получить рейтинг
        self.play_market_context = GooglePageHelper(self.play_market_link)
        # Единственный случай передачи состояния от тестовой функции к тестовой функции
        # Значение рейтинга из текста элемента фиксируется в классе
        self.__class__.play_market_context_rate = self.play_market_context.get_play_market_context_rating()

        # Клик по ранее найденному элементу для перехода на play.google.com
        self.play_market_link.click()



    def test_step4_prove_rating(self):
        self.play_market_rate = PlayMarketPageHelper(self.driver)
        # Получение рейтинга на странице play.google.com
        self.play_market_rate = self.play_market_rate.get_play_market_page_rating()
        # Сравнение
        assert self.play_market_context_rate == self.play_market_rate
