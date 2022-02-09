from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import OZONACCOUNT_PAGE_TEXT, ERROR_OZONACCOUNT_PAGE_TEXT


class OzonAccount(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_OZONACCOUNT
        self.__ozonaccount_button: str = locators.OZON_ACCOUNT_PAGE_BUTTON
        self.__ozonaccount_button: str = locators.OZON_ACCOUNT_PAGE_TEXT
        self.OZONACCOUNT_PAGE_TEXT = OZONACCOUNT_PAGE_TEXT
        self.ERROR_OZONACCOUNT_PAGE_TEXT = ERROR_OZONACCOUNT_PAGE_TEXT

    def get_ozon_account_page(self) -> WebElement:
        return self.is_visible('css_selector', self.__ozonaccount_button, 'Ozon Account Page')

    def get_ozon_account_page_text(self) -> str:
        page = self.get_ozon_account_page()
        page_text = self.get_text_from_web_element(page)
        return page_text
