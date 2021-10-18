from pages.search import GoogleSearchPage
from pages.result import GoogleResults
from pages.google_page import GooglePageHelper





def test_basic_google_search_1(driver):

    #Настройка данных тест-кейса
    PAGE_NUMBER = 0
    QUERY = 'ivi'
    WIKI_QUERY = 'wikipedia.org'

    #Поиск по запросу
    search_page = GoogleSearchPage(driver)
    search_page.search(QUERY)

    #Проверка, что результаты появились
    result_page = GoogleResults(driver)

    assert result_page.link_count() > 0
    assert result_page.query_count(QUERY) > 0
    assert result_page.search_input_value() == QUERY

    result_page.search_input_url(WIKI_QUERY)

