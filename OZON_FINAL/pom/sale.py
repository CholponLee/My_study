from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import SALE_PAGE_TEXT, ERROR_SALE_PAGE_TEXT


class Sale(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_SALE
        self.__sale_title: str = locators.SALE_PAGE_TEXT
        self.SALE_PAGE_TEXT = SALE_PAGE_TEXT
        self.ERROR_SALE_PAGE_TEXT = ERROR_SALE_PAGE_TEXT

    def get_sale_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__sale_title, 'Sale Page Text')

    def get_sale_title_text(self) -> str:
        title = self.get_sale_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
