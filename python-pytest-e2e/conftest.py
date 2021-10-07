from pytest import fixture
from selenium.webdriver import Chrome, ChromeOptions


@fixture(scope='session')
def chrome():
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = Chrome(options=options)
    return browser