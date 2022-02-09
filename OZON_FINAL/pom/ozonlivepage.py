from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base import locators, url
from base.keys import OZONLIVE_IMAGE_ATTRIBUTE, ERROR_OZONLIVE_IMAGE_ATTRIBUTE


class OzonLive(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = url.URL_OZONLIVE
        self.__ozonlive_image = locators.OZON_LIVE_IMAGE
        self.OZONLIVE_IMAGE_ATTRIBUTE = OZONLIVE_IMAGE_ATTRIBUTE
        self.ERROR_OZONLIVE_IMAGE_ATTRIBUTE = ERROR_OZONLIVE_IMAGE_ATTRIBUTE

    def find_ozonlive_title_img(self) -> WebElement:
        return self.find_element('css_selector', self.__ozonlive_image, 'Ozon Live Page Title')

    def get_ozonlive_attribute(self) -> str:
        return self.is_visible('css_selector', self.__ozonlive_image, 'Ozon Live Page Title').\
            get_attribute('style')
