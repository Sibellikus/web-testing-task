import json
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

'''Вспомогательный пакет Pytest с фикстурами и настройками'''
'''Выдача вебдрайвера на сессию каждого теста'''

# класс настроек
# При запуске менеджер установит драйвер
class UtilData:
    SCOPE = 'class'
    EXECUTABLE_PATH = r'C:\Users\Home\Git\web-testing-task\tests\chromedriver.exe'
    SERV = Service(ChromeDriverManager().install())

# идея вывести все атрибуты из классов в json 'дб' (Не используется)
@pytest.fixture(scope=UtilData.SCOPE)
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data

# путь к драйверу в проекте. Вообще, он там не нужен ><
#serv = Service(executable_path=UtilData.EXECUTABLE_PATH)

'''Генератор вебдрайвера, который цепляется к тест_классам через фиксутуру в Test_base'''
@pytest.fixture(scope=UtilData.SCOPE)
def init_driver(request):
    driver = Chrome(service=UtilData.SERV)
    request.cls.driver = driver
    # Неявное ожидание готовности элементов перед попыткой взаимодействия
    driver.implicitly_wait(10)
    yield
    driver.close()







'''@pytest.fixture(scope=UtilData.SCOPE)
def driver():
    driver = Chrome(executable_path=UtilData.EXECUTABLE_PATH)
    # Неявное ожидание готовности элементов перед попыткой взаимодействия
    #driver.implicitly_wait(config)['wait_time']


    # Возвращение объекта драйвера в конце настройки
    yield driver
    # Для очистки покиньте драйвер
    driver.quit()
    
    
    if config['browser'] == 'chrome':

        else:
 
 
 
           raise Exception(f'"{config["browser"]}" is not a supported browser')'''



