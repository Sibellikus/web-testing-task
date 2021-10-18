from BaseApp import BasePage
from selenium.webdriver.common.by import By


class WikiPageLocators:
    LOCATOR_WIKI_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_GOOGLE_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


#class WikiPageHelper(BasePage):
