from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import BESTPRICE_PAGE_TITLE_TEXT, ERROR_BESTPRICE_PAGE_TITLE_TEXT


class BestPrice(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_BESTPRICE
        self.__bestprice_title: str = locators.BESTPRICE_TITLE
        self.BESTPRICE_PAGE_TITLE_TEXT = BESTPRICE_PAGE_TITLE_TEXT
        self.ERROR_BESTPRICE_PAGE_TITLE_TEXT = ERROR_BESTPRICE_PAGE_TITLE_TEXT

    def get_bestprice_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__bestprice_title, 'Best Price Page Title')

    def get_bestprice_title_text(self) -> str:
        title = self.get_bestprice_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
