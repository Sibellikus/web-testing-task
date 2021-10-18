#from selenium.webdriver.common.by import By
import time
from urllib.parse import quote_plus


class GoogleSearchPage:

    QUERY = 'ivi'

    def __init__(self, initiate=True, implicit_wait_time=10, explicit_wait_time=2):
        self.driver = driver

    def load(self, url):

        self.driver.get(url)
        print('Подключение будет осуществлено по адресу: {}'.format(url))
        time.sleep(10)

    def search(self, QUERY, page_num=0, per_page=10, lang='en'):
        query = quote_plus(QUERY)
        url = 'https://www.google.hr/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num*per_page, lang)
        self.load(url)




