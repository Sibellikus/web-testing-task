from pages.base_app import BasePage


'''Класс наследует от BasePage и является POM для веб-страницы google.com'''
'''Содержит методы для взаимодействия с страницей'''


class PlayMarketPageHelper(BasePage):

    PM_PAGE_RATING_CLASS = 'BHMmbe'

    def __init__(self, driver):
        super().__init__(driver)

    # Получение значения рейтинга из текста элемента с классом PM_PAGE_RATING_CLASS
    def get_play_market_page_rating(self, class_value=PM_PAGE_RATING_CLASS):
        play_market_rate = self.get_element(self.xpath_class_locator(class_value))
        play_market_rate = play_market_rate.text

        return play_market_rate
