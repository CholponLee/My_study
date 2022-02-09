from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
from base import locators
from base.keys import CITY, HEADER_LINK_TEXT, ERROR_HEADER_LINK_TEXT, MAP_PAGE_TITLE, ERROR_MAP_PAGE_TITLE


class HomepageHeader(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__header_links: str = locators.HEADER_LINKS
        self.HEADER_LINK_TEXT = HEADER_LINK_TEXT
        self.ERROR_HEADER_LINK_TEXT = ERROR_HEADER_LINK_TEXT
        self.__selectcity_button = locators.SELECT_CITY_BUTTON
        self.__selectcity_form = locators.CITY_FORM
        self.__map_page = locators.MAP_PAGE_TITLE
        self.CITY = CITY
        self.MAP_PAGE_TITLE = MAP_PAGE_TITLE
        self.ERROR_MAP_PAGE_TITLE = ERROR_MAP_PAGE_TITLE

    # Get Header Links
    def get_header_links(self) -> List[WebElement]:
        return self.are_visible('css_selector', self.__header_links, 'Header Links')

    def get_header_links_text(self) -> str:
        header_links = self.get_header_links()
        header_links_text = self.get_text_from_webelements(header_links)
        return Utils.join_strings(header_links_text)

    def is_header_link_clickable(self):
        return self.is_clickable('css_selector', self.__header_links, 'Header Links')

    def get_header_link_back(self):
        return self.get_back()

    def is_city_visible(self) -> WebElement:
        return self.is_visible('css_selector', self.__selectcity_button, 'Select City Button')

    def get_city_text(self):
        city = self.is_city_visible()
        return self.get_text_from_web_element(city)

    def fill_city_form(self):
        return self.is_visible('css_selector', self.__selectcity_form, 'City Keys')

    def get_map_page_url(self):
        self.is_visible('css_selector', self.__map_page, 'Map Page')
        return self.get_current_url()

    def get_map_page_title_text(self):
        city = self.is_visible('css_selector', self.__map_page, 'Map Page Title Text')
        return self.get_text_from_web_element(city)

    def delete_cookies(self):
        return self.delete_cookie()
