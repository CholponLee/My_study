from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import PREMIUM_PAGE_TITLE_TEXT, ERROR_PREMIUM_PAGE_TITLE_TEXT


class Premium(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_PREMIUM
        self.__premium_title: str = locators.PREMIUM_TITLE
        self.PREMIUM_PAGE_TITLE_TEXT = PREMIUM_PAGE_TITLE_TEXT
        self.ERROR_PREMIUM_PAGE_TITLE_TEXT = ERROR_PREMIUM_PAGE_TITLE_TEXT

    def get_premium_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__premium_title, 'Premium Page Title')

    def get_premium_title_text(self) -> str:
        title = self.get_premium_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
