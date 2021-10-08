from pytest import fixture
from selenium.webdriver import Firefox, Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@fixture(scope='session')
def chrome():
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return browser

@fixture(scope='session')
def firefox():
    browser = Firefox(executable_path=GeckoDriverManager().install())
    return browser