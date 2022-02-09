from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import SELLERS_PAGE_TITLE_TEXT, ERROR_SELLERS_PAGE_TITLE_TEXT


class Sellers(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_SELLERS
        self.__sellers_title: str = locators.SELLERS_TITLE
        self.SELLERS_PAGE_TITLE_TEXT = SELLERS_PAGE_TITLE_TEXT
        self.ERROR_SELLERS_PAGE_TITLE_TEXT = ERROR_SELLERS_PAGE_TITLE_TEXT

    def get_sellers_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__sellers_title, 'Sellers Page Title')

    def get_sellers_title_text(self) -> str:
        title = self.get_sellers_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
