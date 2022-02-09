from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import CHILDRENGOODS_PAGE_TITLE_TEXT, ERROR_CHILDRENGOODS_PAGE_TITLE_TEXT


class Childrengoods(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_CHILDRENGOODS
        self.__childrengoods_title: str = locators.CHILDRENGOODS_TITLE
        self.CHILDRENGOODS_PAGE_TITLE_TEXT = CHILDRENGOODS_PAGE_TITLE_TEXT
        self.ERROR_CHILDRENGOODS_PAGE_TITLE_TEXT = ERROR_CHILDRENGOODS_PAGE_TITLE_TEXT

    def get_childrengoods_title(self) -> WebElement:
        return self.is_visible('css_selector', self.__childrengoods_title, "Сhildren's Goods Page Title")

    def get_childrengoods_title_text(self) -> str:
        title = self.get_childrengoods_title()
        title_text = self.get_text_from_web_element(title)
        return title_text
