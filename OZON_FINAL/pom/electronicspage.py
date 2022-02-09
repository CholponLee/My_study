from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import ELECTRONICS_PAGE_TITLE_TEXT, ERROR_ELECTRONICS_PAGE_TITLE_TEXT


class Electronics(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_ELECTRONICS
        self.__electronics_title: str = locators.ELECTRONICS_TITLE
        self.ELECTRONICS_PAGE_TITLE_TEXT = ELECTRONICS_PAGE_TITLE_TEXT
        self.ERROR_ELECTRONICS_PAGE_TITLE_TEXT = ERROR_ELECTRONICS_PAGE_TITLE_TEXT

    def get_electronics_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__electronics_title, 'Electronics Page Title')

    def get_electronics_title_text(self) -> str:
        title = self.get_electronics_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
