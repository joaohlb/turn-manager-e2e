from time import sleep
from selenium.webdriver import Chrome, ChromeOptions


def before_all(context):
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.browser = Chrome(options=options)
    context.browser.get('http://localhost:5555')


def after_step(context, step):
    sleep(1)


def after_all(context):
    context.browser.quit()
