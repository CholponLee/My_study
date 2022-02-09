from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import BRANDS_PAGE_TITLE_TEXT, ERROR_BRANDS_PAGE_TITLE_TEXT


class Brands(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_BRANDS
        self.__brands_title: str = locators.BRANDS_TITLE
        self.BRANDS_PAGE_TITLE_TEXT = BRANDS_PAGE_TITLE_TEXT
        self.ERROR_BRANDS_PAGE_TITLE_TEXT = ERROR_BRANDS_PAGE_TITLE_TEXT

    def get_brands_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__brands_title, 'Brands Page Title 1')

    def get_brands_title_text(self) -> str:
        title = self.get_brands_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
