from pages.base_app import BasePage
from urllib.parse import quote_plus
from selenium.webdriver.common.by import By

'''Класс наследует от BasePage и является POM для веб-страницы google.com'''
'''Содержит атрибуты (локаторы) и методы для поиска и взаимодействия с результатами поиска'''


class GooglePageHelper(BasePage):

    SEARCH_INPUT = (By.NAME, 'q')

    XPATH_CLASS_CLICKABLE = 'yuRUbf'
    XPATH_CLASS_CONTEXT = 'tF2Cxc'
    MENU_BAR_CLASS = 'hdtb-mitem'
    TOOLS_CLASS = 'PNyWAd ZXJQ7c'
    SIZE_CLASS = 'xFo9P r9PaP'
    BIG_SIZE_CLASS = 'Hm7Qac '

    # Инициализация класса и наследование
    def __init__(self, driver):
        super().__init__(driver)

    # Загрузчик страницы по адресу
    def load_result_page(self, url):
        self.driver.get(url)

    '''Главный метод навигации по Google'''
    # Quote_plus формирует адресный запрос, закладывая номмер стсраницы результата.
    # TODO заменить quote_plus или настроить его. Занимает больше времени, чем кнопки пагинации
    def search(self, QUERY, page_num=0, per_page=10, lang='en'):
        query = quote_plus(QUERY)
        url = 'https://www.google.hr/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num * per_page, lang)
        self.load_result_page(url)

    # Подсчет длины списка результатов для валидации их наличия
    def results_count(self):
        link_divs = self.driver.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    # Подсчет длины списка искомого по классу элемммента class_value в результатах для валидации наличия искомого
    def query_count(self, class_value):
        query_results = self.get_elements(self.xpath_class_locator(class_value))
        return len(query_results)

    # Определение значения запроса для валидации поиска
    def validate_input(self):
        search_input = self.get_element(self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    # Цикл поиска элемента по страницам результатов
    def set_browse_result_pages(self, query, subquery, page_num):
        for page_num in range(page_num - 1):
            if self.get_link_is_visible(self.xpath_query_locator(subquery)):
                return self.get_element(self.xpath_query_locator(subquery))
            else:
                self.search(query, page_num)

    # Получить инфо о рейтинге из текста родительского элемента элемента
    '''Метод element_obj'''
    def get_play_market_context_rating(self):  #, query, subquery, page_num

        context_elem = self.get_parent_element()
        context_text = context_elem.text
        context_text = context_text.split()
        context_rate = context_text[context_text.index('Рейтинг:') + 1]
        return context_rate

    # Клик по элементу класса class_value c совпадением в тексте элемента по паттерну query
    def set_btn_clicked(self, query, class_value):
        self.set_click_element(self.xpath_utility_locator(class_value, query))
        return self

    # Получить словарь группы элементов (метод для взаимодействия со списками кнопок)
    def get_panel(self, query, class_value):
        bar = {}
        elements = self.get_elements(self.xpath_utility_locator(class_value, query))
        for elem in elements:
            bar.update({elem.text : elem})
        return bar

    # Метод для клика по кнопкам Размер и Большой.
    # TODO найти компромисс между скриптом и ручной задержкой при ожидании динамических элементов
    def set_manage_picture_size(self, query, class_value):
        element = self.get_element(self.xpath_utility_locator(class_value, query))
        self.executor(element)
        return self

    # Собранный метод для TestSccenario1 по валидации наличия 3-ех картинок
    def set_validate_results(self, query, class_value):
        results = []
        links = self.get_elements(self.xpath_utility_locator(class_value, query))
        for link in links:
            if link.text == f'{query}.ru':
                results.append(link)
        return len(results)

