from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

'''Это родительских класс для всех частных случаев Page object model'''
'''Содержит атрибуты и методы, применимые ко всем веб-страницам'''


class BasePage:

    PARENT_LOCATOR = (By.XPATH, './../..')
    EXPLICIT_TIME = 20
    # Инициалзация
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://google.com/"

    # метод возвращает локатор XPATH на основе наличия совпадения паттерна QUERY
    # в тексте ссылки <a> класса
    @classmethod
    def xpath_query_locator(cls, query):
        xpath = f"//a[contains(@href, '{query}')]"
        return (By.XPATH, xpath)

    # метод возвращает локатор XPATH на основе наличия совпадения паттерна QUERY
    # в тексте элемента класса class_value
    @classmethod
    def xpath_utility_locator(cls, class_value, query):
        xpath = f"//div[@class='{class_value}' and contains(/,'{query}')]"
        return (By.XPATH, xpath)

    # метод возвращает локатор XPATH на основе паттерна class_value
    # класса элеммента
    @classmethod
    def xpath_class_locator(cls, class_value):
        xpath = f"//div[@class='{class_value}']"
        return (By.XPATH, xpath)

    # Клик по элементу с задержкой до возмможности клика
    def set_click_element(self, locator, time=EXPLICIT_TIME):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}").click()
        return self

    # Получить заголовок страницы (Не ипользовано)
    def get_page_title(self, title, time=EXPLICIT_TIME):
        WebDriverWait(self.driver, time).until(EC.title_is(title))
        return self.driver.title

    # Получить True, если элемент найден
    def get_link_is_visible(self, locator, time=EXPLICIT_TIME):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")
        return bool(element)

    # Получить элемент, если он найден
    def get_element(self, locator, time=EXPLICIT_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # Получить элементы, если они найдены
    def get_elements(self, locator, time=EXPLICIT_TIME):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # Перейти на базовый адрес
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # Проверить наличие паттерна url в адресе текущей страницы
    def get_url(self, url, time=EXPLICIT_TIME):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url))

    # Получить родительский элемент
    '''Метод element_obj'''
    def get_parent_element(self, locator=PARENT_LOCATOR):
        return self.get_element(locator)

    # JS экзекутор. Психанул с подвижнымми элементами и необходимостью
    # вручную контролировать explicite задержку
    def executor(self, element):
        return self.driver.execute_script("arguments[0].click()", element)

