from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import OZONTRAVEL_PAGE_TITLE_TEXT, ERROR_OZONTRAVEL_PAGE_TITLE_TEXT


class OzonTravel(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_OZONTRAVEL
        self.__ozontravel_title: str = locators.OZON_TRAVEL_TITLE
        self.OZONTRAVEL_PAGE_TITLE_TEXT = OZONTRAVEL_PAGE_TITLE_TEXT
        self.ERROR_OZONTRAVEL_PAGE_TITLE_TEXT = ERROR_OZONTRAVEL_PAGE_TITLE_TEXT

    def get_ozontravel_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__ozontravel_title, 'Ozon Travel Page Title')

    def get_ozontravel_title_text(self) -> str:
        title = self.get_ozontravel_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
