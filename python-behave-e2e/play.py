from selenium.webdriver import Chrome
from time import sleep


character_dropdown = '//*[@class="select-wrapper"][input[@value="Character Type"]]'
reroll_dropdown = '//*[@class="select-wrapper"][input[@value="All Allies"]]'

def enforce_dropdown(webelement):
    while 'display: none' in webelement.find_element_by_tag_name('ul').get_attribute('style'):
        webelement.click()
        sleep(.5)

browser = Chrome()
browser.get('http://localhost:5555')