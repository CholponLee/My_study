from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import HOME_PAGE_TITLE_TEXT, ERROR_HOME_PAGE_TITLE_TEXT


class Home(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_HOME
        self.__home_title: str = locators.HOME_TITLE
        self.HOME_PAGE_TITLE_TEXT = HOME_PAGE_TITLE_TEXT
        self.ERROR_HOME_PAGE_TITLE_TEXT = ERROR_HOME_PAGE_TITLE_TEXT

    def get_home_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__home_title, 'Home Page Title')

    def get_home_title_text(self) -> str:
        title = self.get_home_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
