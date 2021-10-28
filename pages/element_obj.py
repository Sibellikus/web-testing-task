from selenium.webdriver.common.by import By

'''Класс, который наверно, должен был быть >_>'''
'''Модель для обьекта webdriver.remote.support.WebElement'''
# Не используется, методы определены локально в BasePage from page.Base_app
#                                             и GooglePageHelper from pages.google_page


class WebElementObj:

    PARENT_LOCATOR = (By.XPATH, './../..')

    def __init__(self, element):
        self.element = element


    def get_parent_element_text(self, locator=PARENT_LOCATOR):
        parent_element = self.element.find_element(locator)
        return parent_element.text

    def get_play_market_context_rating(self):
        context_text = self.get_parent_element_text()
        context_text = context_text.split()
        context_rate = context_text[context_text.index('Рейтинг:') + 1]

        return context_rate
