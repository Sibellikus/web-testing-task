from pages.wiki_page import WikiPageHelper
from pages.google_page import GooglePageHelper
from tests.test_base import BaseTest


# Настройка данных тест-кейса
PAGE_NUMBER = 5
QUERY = 'ivi'
WIKI_QUERY = 'wikipedia.org'
IS_EXIST_QUERY = 'ivi.ru'

RESULTS_URL_CLASS = 'yuRUbf'
XPATH_CLASS_CONTEXT = 'tF2Cxc'


class TestScenario3(BaseTest):
    """неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            на первых 5 страницах находит ссылку на статью в wikipedia об ivi
            убеждается, что в статье есть ссылка на официальный сайт ivi.ru"""


    def test_step1_goto_google_site(self):

        self.search_page = GooglePageHelper(self.driver)
        #search_page = GooglePageHelper(self)
        self.search_page.go_to_site()



    def test_step2_query_ivi(self):
        # Поиск по заданному значению QUERY
        self.search_page = GooglePageHelper(self.driver)
        self.search_page.search(QUERY)
        # Смена семантики
        self.result_page = self.search_page
        # Подсчет длины списка результатов для валидации наличия результата
        assert self.result_page.query_count(RESULTS_URL_CLASS) > 0

    def test_step3_inspect_result_for_wiki_site(self):
        self.results = GooglePageHelper(self.driver)
        # Получить кликабельный элемент с совпадением в адресе ссылки play.google.com
        self.wiki_link = self.results.set_browse_result_pages(QUERY, WIKI_QUERY, PAGE_NUMBER)
        self.wiki_link.click()




    def test_step4_is_exist_ivi_url(self):
        # Присвоение
        self.wiki_page = WikiPageHelper(self.driver)

        # Проверка на наличие ссылок ivi.ru
        self.wiki_results = self.wiki_page.get_all_links(IS_EXIST_QUERY)
        assert self.wiki_page.get_links_are_existed(self.wiki_results)

        # Клик по ссылке
        self.wiki_page.get_link_clicked(IS_EXIST_QUERY)
        # Проверка верности текущего адреса ivi.ru
        assert self.wiki_page.get_url(IS_EXIST_QUERY)


