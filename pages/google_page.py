from base_app import BasePage
import time
from urllib.parse import quote_plus


from selenium.webdriver.common.by import By


#class GooglePageLocators:
    #LINKS = (By.XPATH, "//div[@class='yuRUbf']/a")


class GooglePageHelper(BasePage):

    SEARCH_MATCH = 'wikipedia.org'
    LINKS_DIVS = (By.XPATH, "//div[@class='yuRUbf']/a")
    SEARCH_INPUT = (By.NAME, 'q')

    @classmethod
    def QUERY_RESULTS_Xpath(cls, query):
        xpath = f"//div[@class='yuRUbf']/a[contains(@href, '{query}')]"
        return (By.XPATH, xpath)


    def load(self, url):
        self.driver.get(url)
        print('Подключение будет осуществлено по адресу: {}'.format(url))
        time.sleep(10)

    def search(self, QUERY, page_num=0, per_page=10, lang='en'):
        query = quote_plus(QUERY)
        url = 'https://www.google.hr/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num * per_page,
                                                                               lang)
        self.load(url)

    # Подсчет длины списка результатов для валидации их наличия
    def link_count(self):
        link_divs = self.driver.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    # Подсчет длины списка искомого в результатах для валидации наличия искомого
    def query_count(self, query):
        query_results = self.driver.find_elements(*self.QUERY_RESULTS_Xpath(query))
        return len(query_results)

    # Поиск элемента на странице по совпадению паттерна SEARCH_MATCH в тексте ссылки LINK_DIVS

    # Определение значения запроса для валидации поиска?
    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def get_search_link(self, query):
        search_input = self.driver.find_element(*self.QUERY_RESULTS_Xpath(query))
        url = search_input.get_attribute('href')
        search_input.click()
        return url