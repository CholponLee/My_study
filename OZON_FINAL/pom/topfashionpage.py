from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import TOPFASHION_PAGE_TITLE_TEXT, ERROR_TOPFASHION_PAGE_TITLE_TEXT


class TopFashion(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_TOPFASHION
        self.__topfashion_title: str = locators.TOPFASHION_TITLE
        self.TOPFASHION_PAGE_TITLE_TEXT = TOPFASHION_PAGE_TITLE_TEXT
        self.ERROR_TOPFASHION_PAGE_TITLE_TEXT = ERROR_TOPFASHION_PAGE_TITLE_TEXT

    def get_topfashion_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__topfashion_title, 'Top Fashion Page Title')

    def get_topfashion_title_text(self) -> str:
        title = self.get_topfashion_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
