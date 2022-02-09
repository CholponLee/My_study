from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from base import locators
from base.keys import WRONG_SEARCH_PAGE_TITLE_TEXT, EXPECTED_WRONG_SEARCH_PAGE_TITLE_TEXT


class HomepageSearchField(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__searchfield: str = locators.SEARCH_FIELD
        self.__searchbutton: str = locators.SEARCH_BUTTON
        self.__searchanswer: str = locators.SEARCH_ANSWER
        self.__searchwrong: str = locators.SEARCH_WRONG
        self.WRONG_SEARCH_PAGE_TITLE_TEXT = WRONG_SEARCH_PAGE_TITLE_TEXT
        self.EXPECTED_WRONG_SEARCH_PAGE_TITLE_TEXT = EXPECTED_WRONG_SEARCH_PAGE_TITLE_TEXT

    # Search field
    def is_searchfield_visible(self):
        return self.is_visible('css_selector', self.__searchfield, 'Search Field')

    # Clear search field
    def searchfield_clear(self):
        return self.is_visible('css_selector', self.__searchfield, 'Search Field').clear()

    # Search field for sending keys
    def fill_searchfield(self):
        return self.is_visible('css_selector', self.__searchfield, 'Search Field')

    # Search button
    def search_button(self):
        return self.is_visible('css_selector', self.__searchbutton, 'Search Button')

    # Click button to start searching
    def search_button_click(self):
        return self.is_visible('css_selector', self.__searchbutton, 'Search Button').click()

    # Get searching page URL
    def get_searching_url(self):
        self.is_presence('css_selector', self.__searchanswer, 'Search Answer Page')
        url = self.get_current_url().rpartition('/')
        return url[0]

    # Get URL if search field is empty
    def get_url_empty_search(self):
        self.is_visible('css_selector', self.__searchfield, 'Search Field')
        return self.get_current_url()

    # Get URL if keys in search field is wrong
    def get_url_wrong_search(self):
        self.is_visible('css_selector', self.__searchwrong, 'Search Field')
        url = self.get_current_url().rpartition('/')
        return url[0]

    # Get tittle from page after wong search
    def get_wrong_search_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__searchwrong, 'Actions Page Title')

    # Get tittle text from page after wong search
    def get_wrong_search_title_text(self) -> str:
        title = self.get_wrong_search_title()
        title_text = self.get_text_from_web_element(title)
        return title_text

    # Delete cookies
    def delete_cookies(self):
        return self.delete_cookie()
