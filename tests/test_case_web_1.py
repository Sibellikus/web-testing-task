from pages.google_page import GooglePageHelper
from pages.base_app import BasePage
from selenium.webdriver import Chrome
from tests.test_base import BaseTest

QUERY = 'ivi'

RESULTS_URL_CLASS = 'yuRUbf'
XPATH_CLASS_CONTEXT = 'tF2Cxc'
PM_PAGE_RATING_CLASS = 'BHMmbe'

NAVIGATE_MENU_BAR = 'Картинки'
TOOLS = 'Инструменты'
SIZE_BAR = 'Размер'
BIG_SIZE = 'Большой'

MENU_BAR_CLASS = 'hdtb-mitem'
TOOLS_CLASS = 'PNyWAd ZXJQ7c'
SIZE_BTN_CLASS = 'xFo9P r9PaP'
BIG_SIZE_CLASS = 'Hm7Qac '

IVI_LINK_PIC_CLASS = 'fxgdke'


class TestScenario1(BaseTest):
    """1 Неавторизованный пользователь
            заходит в https://www.google.com/
            ищет ivi
            переходит в картинки
            выбирает большие
            убеждается, что не менее 3 картинок в выдаче ведут на сайт ivi.ru"""

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

    def test_step3_go_to_pics(self):
        self.search_page = GooglePageHelper(self.driver)
        # Получить кнопки под адресной строкой
        self.menu = self.search_page.get_panel(QUERY, MENU_BAR_CLASS)
        # Клик по картинкам
        self.menu[NAVIGATE_MENU_BAR].click()

    def test_step4_choose_big_pics(self):
        self.search_page = GooglePageHelper(self.driver)
        # Поиск кнопки "Инструменты" и клик по ней
        self.tools = self.search_page.set_btn_clicked(TOOLS, TOOLS_CLASS)
        # Клик по кнопке "Размер"
        self.size = self.search_page.set_manage_picture_size(SIZE_BAR, SIZE_BTN_CLASS)
        # Клик по кнопке "Большой"
        self.size_options = self.size.set_manage_picture_size(QUERY, BIG_SIZE_CLASS)

    def test_step5_prove_ivi_links(self):
        self.big_pic_results = GooglePageHelper(self.driver)
        # Сбор картинок по совпадению в адресе ссылки ivi.ru
        self.link_results = self.big_pic_results.set_validate_results(QUERY, IVI_LINK_PIC_CLASS)
        assert self.link_results > 2
