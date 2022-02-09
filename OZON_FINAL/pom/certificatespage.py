from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import CERTIFICATES_PAGE_TITLE_TEXT, ERROR_CERTIFICATES_PAGE_TITLE_TEXT


class Certificates(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_CERTIFICATES
        self.__certificates_title: str = locators.CERTIFICATES_TITLE
        self.CERTIFICATES_PAGE_TITLE_TEXT = CERTIFICATES_PAGE_TITLE_TEXT
        self.ERROR_CERTIFICATES_PAGE_TITLE_TEXT = ERROR_CERTIFICATES_PAGE_TITLE_TEXT

    def get_certificates_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__certificates_title, 'Certificates Page Title')

    def get_certificates_title_text(self) -> str:
        title = self.get_certificates_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
