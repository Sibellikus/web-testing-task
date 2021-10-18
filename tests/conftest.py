import json

import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture#(scope='session')
def driver():
    driver = Chrome()
    # Неявное ожидание готовности элементов перед попыткой взаимодействия
    driver.implicitly_wait(config['wait_time'])


    # Возвращение объекта драйвера в конце настройки
    yield driver
    # Для очистки покиньте драйвер
    driver.quit()
    ''' if config['browser'] == 'chrome':

        else:
            raise Exception(f'"{config["browser"]}" is not a supported browser')'''