from time import sleep
from pytest import mark


class CharacterTests:
    
    @mark.ui
    def test_character_button_shows_creation_form(self, chrome):
        # setup
        browser = chrome
        browser.get('http://localhost:5555')
        # action
        browser.find_element_by_id('add-char').click()
        # assertion
        assert browser.find_element_by_css_selector('form.char-form').is_displayed()
    
    @mark.ui
    def test_character_button_hides_creation_form(self, chrome):
        # setup
        browser = chrome
        browser.get('http://localhost:5555')
        if not browser.find_element_by_css_selector('form.char-form').is_displayed():
            browser.find_element_by_id('add-char').click()
        # action
        browser.find_element_by_id('add-char').click()
        # assertion
        sleep(1)
        assert not browser.find_element_by_css_selector('form.char-form').is_displayed()