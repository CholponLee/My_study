from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import APPAREL_PAGE_TITLE_TEXT_ONE, APPAREL_PAGE_TITLE_TEXT_TWO, APPAREL_PAGE_TITLE_TEXT_THREE, \
    ERROR_APPAREL_PAGE_TITLE_TEXT_ONE, ERROR_APPAREL_PAGE_TITLE_TEXT_TWO, ERROR_APPAREL_PAGE_TITLE_TEXT_THREE


class Apparel(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_APPAREL
        self.__apparel_title_one: str = locators.APPAREL_TITLE_ONE
        self.__apparel_title_two: str = locators.APPAREL_TITLE_TWO
        self.__apparel_title_three: str = locators.APPAREL_TITLE_THREE

        self.APPAREL_PAGE_TITLE_TEXT_ONE = APPAREL_PAGE_TITLE_TEXT_ONE
        self.APPAREL_PAGE_TITLE_TEXT_TWO = APPAREL_PAGE_TITLE_TEXT_TWO
        self.APPAREL_PAGE_TITLE_TEXT_THREE = APPAREL_PAGE_TITLE_TEXT_THREE

        self.ERROR_APPAREL_PAGE_TITLE_TEXT_ONE = ERROR_APPAREL_PAGE_TITLE_TEXT_ONE
        self.ERROR_APPAREL_PAGE_TITLE_TEXT_TWO = ERROR_APPAREL_PAGE_TITLE_TEXT_TWO
        self.ERROR_APPAREL_PAGE_TITLE_TEXT_THREE = ERROR_APPAREL_PAGE_TITLE_TEXT_THREE

    def get_apparel_title_one(self) -> WebElement:
        return self.is_visible('css_selector', self.__apparel_title_one, 'Apparel (Clothes and Footwear) Page Title 1')

    def get_apparel_title_text_one(self) -> str:
        title = self.get_apparel_title_one()
        title_text = self.get_text_from_web_element(title)
        return title_text

    def get_apparel_title_two(self) -> WebElement:
        return self.is_visible('css_selector', self.__apparel_title_two, 'Apparel (Clothes and Footwear) Page Title 2')

    def get_apparel_title_text_two(self) -> str:
        title = self.get_apparel_title_two()
        title_text = self.get_text_from_web_element(title)
        return title_text

    def get_apparel_title_three(self) -> WebElement:
        return self.is_visible('css_selector', self.__apparel_title_three, 'Apparel (Clothes and Footwear) Page Title 3')

    def get_apparel_title_text_three(self) -> str:
        title = self.get_apparel_title_three()
        title_text = self.get_text_from_web_element(title)
        return title_text
