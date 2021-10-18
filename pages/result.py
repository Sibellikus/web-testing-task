
from selenium.webdriver.common.by import By


class GoogleResults:

    SEARCH_MATCH = 'wikipedia.org'
    LINKS_DIVS = (By.XPATH, "//div[@class='yuRUbf']/a")
    SEARCH_INPUT = (By.NAME, 'q')

    @classmethod
    def QUERY_RESULTS_Xpath(cls, query):
        xpath = f"//div[@class='yuRUbf']/a[contains(@href, '{query}')]"
        return (By.XPATH, xpath)

    @classmethod
    def QUERY_RESULTS_Linktxt(cls, query):
        LINK_TEXT = 'ivi.ru'
        return (By.LINK_TEXT, LINK_TEXT)






    def __init__(self):
        self.driver = driver

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

    def search_input_url(self, query):
        search_input = self.driver.find_element(*self.QUERY_RESULTS_Xpath(query))
        url = search_input.get_attribute('href')
        search_input.click()
        return url


    #def search_input_url(self, query):


