from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
from base.keys import NAV_LINK_TEXT, ERROR_NAV_LINK_TEXT
from base import locators


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = locators.HEADER_NAV_LINKS
        self.NAV_LINK_TEXT = NAV_LINK_TEXT
        self.ERROR_NAV_LINK_TEXT = ERROR_NAV_LINK_TEXT

        # Get Header Navigation Links Locations
        self.__topfashion_link: str = locators.TOPFASHION_LINK
        self.__premium_link: str = locators.PREMIUM_LINK
        self.__ozontravel_link: str = locators.OZON_TRAVEL_LINK
        self.__ozonaccount_link: str = locators.OZON_ACCOUNT_LINK
        self.__ozonlive_link: str = locators.OZON_LIVE_LINK
        self.__sale_link: str = locators.SALE_LINK
        self.__brands_link: str = locators.BRANDS_LINK
        self.__sellers_link: str = locators.SELLERS_LINK
        self.__certificates_link: str = locators.CERTIFICATES_LINK
        self.__electronics_link: str = locators.ELECTRONICS_LINK
        self.__apparel_link: str = locators.APPAREL_LINK
        self.__childrengoods_link: str = locators.CHILDRENGOODS_LINK
        self.__home_link: str = locators.HOME_LINK
        self.__bestprice_link: str = locators.BESTPRICE_LINK

        # Get Page's Titles for Getting Theirs URLs
        self.__topfashion_title: str = locators.TOPFASHION_TITLE
        self.__premium_title: str = locators.PREMIUM_TITLE
        self.__ozontravel_title: str = locators.OZON_TRAVEL_TITLE
        self.__ozonaccount_page_button: str = locators.OZON_ACCOUNT_PAGE_BUTTON
        self.__ozonlive_image = locators.OZON_LIVE_IMAGE
        self.__sale_title: str = locators.SALE_PAGE_TEXT
        self.__brands_title: str = locators.BRANDS_TITLE
        self.__sellers_title: str = locators.SELLERS_TITLE
        self.__certificates_title: str = locators.CERTIFICATES_TITLE
        self.__electronics_title: str = locators.ELECTRONICS_TITLE
        self.__apparel_title: str = locators.APPAREL_TITLE_ONE
        self.__childrengoods_title: str = locators.CHILDRENGOODS_TITLE
        self.__home_title: str = locators.HOME_TITLE
        self.__bestprice_title: str = locators.BESTPRICE_TITLE

    # Get Header Navigation Links
    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css_selector', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)

    # Is Link Clickable
    def is_topfashion_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__topfashion_link, 'Top Fashion Link')

    def is_premium_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__premium_link, 'Premium Link')

    def is_ozontravel_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__ozontravel_link, 'Ozon Travel Link')

    def is_ozonaccount_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__ozonaccount_link, 'Ozon Account Link')

    def is_ozonlive_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__ozonlive_link, 'Ozon Live Link')

    def is_sale_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__sale_link, 'Sale Link')

    def is_brands_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__brands_link, 'Brands Link')

    def is_sellers_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__sellers_link, 'Sellers Link')

    def is_certificates_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__certificates_link, 'Certificates Link')

    def is_electronics_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__electronics_link, 'Electronics Link')

    def is_apparel_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__apparel_link, 'Apparel (Clothes and Footwear) Link')

    def is_childrengoods_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__childrengoods_link, "Ozon Сhildren's Goods Page Link")

    def is_home_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__home_link, 'Home Link')

    def is_bestprice_link_clickable(self) -> object:
        return self.is_clickable('css_selector', self.__bestprice_link, 'Best Price Link')

    # Get Page's URL
    def topfashion_current_url(self):
        self.is_presence('css_selector', self.__topfashion_title, 'Top Fashion Page Title')
        return self.get_current_url()

    def premium_current_url(self):
        self.is_presence('css_selector', self.__premium_title, 'Premium Page Title')
        return self.get_current_url()

    def ozontravel_current_url(self):
        self.is_presence('css_selector', self.__ozontravel_title, 'Ozon Travel Page Title')
        return self.get_current_url()

    def ozonaccount_current_url(self):
        self.is_visible('css_selector', self.__ozonaccount_page_button, 'Ozon Account Page Text')
        return self.get_current_url()

    def ozonlive_current_url(self):
        self.is_presence('css_selector', self.__ozonlive_image, 'Ozon Live Page Title')
        return self.get_current_url()

    def sale_current_url(self):
        self.is_visible('css_selector', self.__sale_title, 'Ozon Sale Page Text')
        return self.get_current_url()

    def brands_current_url(self):
        self.is_presence('css_selector', self.__brands_title, 'Ozon Brands Page Title')
        return self.get_current_url()

    def sellers_current_url(self):
        self.is_presence('css_selector', self.__sellers_title, 'Sellers Page Title')
        return self.get_current_url()

    def certificates_current_url(self):
        self.is_presence('css_selector', self.__certificates_title, 'Ozon Certificates Page Title')
        url = self.get_current_url().rpartition('/')
        return url[0]

    def electronics_current_url(self):
        self.is_presence('css_selector', self.__electronics_title, 'Ozon Electronics Page Title')
        return self.get_current_url()

    def apparel_current_url(self):
        self.is_presence('css_selector', self.__apparel_title, 'Ozon Apparel (Clothes and Footwear) Page Title')
        return self.get_current_url()

    def childrengoods_current_url(self):
        self.is_presence('css_selector', self.__childrengoods_title, "Ozon Сhildren's goods Page Title")
        return self.get_current_url()

    def home_current_url(self):
        self.is_presence('css_selector', self.__home_title, 'Home Page Title')
        return self.get_current_url()

    def bestprice_current_url(self):
        self.is_presence('css_selector', self.__bestprice_title, 'Best Price Page Title')
        return self.get_current_url()

    # Delete Cookies
    def delete_cookies(self):
        return self.delete_cookie()
