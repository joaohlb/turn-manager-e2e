class Base(object):
    def __init__(self, driver):
        self.driver = driver
    

    def enforce_dropdown(self, webelement):
        while 'display: none' in webelement.find_element_by_tag_name('ul').get_attribute('style'):
            webelement.click()