from pages.base_app import BasePage

'''Класс наследует от BasePage и является POM для веб-страницы wikipedia.org'''
'''Содержит методы для взаимодействия с страницей'''


class WikiPageHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    #Проверка ссылки на наличие
    def wiki_link_is_existed(self, query):
        return self.get_link_is_visible(self.xpath_query_locator(query))

    # Клик по ссылке
    def get_link_clicked(self, query):
        self.set_click_element(self.xpath_query_locator(query))

    # Получить все элементы с ссылкаммми по запросу QUERY
    def get_all_links(self, query):
        links = self.get_elements(self.xpath_query_locator(query))
        return links

    # Проверка наличия элементов с ссылкой по запросу QUERY
    def get_links_are_existed(self, links):
        return len(links) > 0


