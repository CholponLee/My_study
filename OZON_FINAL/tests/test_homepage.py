import time

import pytest
import requests
from pom.homepage_nav import HomepageNav
from pom.topfashionpage import TopFashion
from pom.premiumpage import Premium
from pom.ozontravelpage import OzonTravel
from pom.ozonaccountpage import OzonAccount
from pom.ozonlivepage import OzonLive
from pom.sale import Sale
from pom.brandspage import Brands
from pom.sellerspage import Sellers
from pom.certificatespage import Certificates
from pom.electronicspage import Electronics
from pom.apparelpage import Apparel
from pom.childrengoodspage import Childrengoods
from pom.homepage import Home
from pom.bestpricepage import BestPrice
from base.url import URL, URL_TOPFASHION, URL_PREMIUM, URL_OZONTRAVEL, URL_OZONACCOUNT, URL_OZONLIVE, URL_SALE, \
    URL_BRANDS, URL_SELLERS, URL_CERTIFICATES, URL_ELECTRONICS, URL_APPAREL, URL_CHILDRENGOODS, URL_HOME, URL_BESTPRICE


@pytest.mark.usefixtures('setup')
class TestHomePage:

    # Testing Home Page Status Code
    def test_home_page_response(self):
        homepage_nav = HomepageNav(self.driver)
    
        response = requests.get(URL)
        assert response.status_code == 200
    
        homepage_nav.delete_cookies()
    
    # Testing Header Navigation Links (positive and negative)
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
    
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validate Nav Links Text'
    
        error_links = homepage_nav.ERROR_NAV_LINK_TEXT
        assert actual_links != error_links
    
        homepage_nav.delete_cookies()
    
    
    '''
        Header Links Links testing:
        1) Link clickability checking
        2) Transition to correct URL checking
        3) Page code status checking
        4) Transition to the correct page checking
    '''
    
    # Testing Header Topfashion Link
    def test_topfashion_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_topfashion_link_clickable()
    
        homepage_nav.get_nav_links()[0].click()
        actual_url = homepage_nav.topfashion_current_url()
        expected_url = URL_TOPFASHION
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        topfashion = TopFashion(self.driver)
        actual_title = topfashion.get_topfashion_title_text()
        expected_title = topfashion.TOPFASHION_PAGE_TITLE_TEXT
        error_title = topfashion.ERROR_TOPFASHION_PAGE_TITLE_TEXT
        assert expected_title == actual_title, 'Validate TOP Fashion Page Title Text'
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Premium Link
    def test_premium_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_premium_link_clickable()
    
        homepage_nav.get_nav_links()[1].click()
        actual_url = homepage_nav.premium_current_url()
        expected_url = URL_PREMIUM
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        premium = Premium(self.driver)
        actual_title = premium.get_premium_title_text()
        expected_title = premium.PREMIUM_PAGE_TITLE_TEXT
        error_title = premium.ERROR_PREMIUM_PAGE_TITLE_TEXT
        assert expected_title == actual_title, 'Validate Premium Page Title Text'
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Ozon Travel Link
    def test_ozontravel_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_ozontravel_link_clickable()
    
    
        homepage_nav.get_nav_links()[2].click()
        actual_url = homepage_nav.ozontravel_current_url()
        expected_url = URL_OZONTRAVEL
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        ozontravel = OzonTravel(self.driver)
        actual_title = ozontravel.get_ozontravel_title_text()
        expected_title = ozontravel.OZONTRAVEL_PAGE_TITLE_TEXT
        error_title = ozontravel.ERROR_OZONTRAVEL_PAGE_TITLE_TEXT
        assert expected_title == actual_title, 'Validate Ozon Travel Page Title Text'
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Ozon Account Link
    def test_ozonaccount_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_ozonaccount_link_clickable()
    
        homepage_nav.get_nav_links()[3].click()
        actual_url = homepage_nav.ozonaccount_current_url()
        expected_url = URL_OZONACCOUNT
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        ozonaccount = OzonAccount(self.driver)
        actual_text = ozonaccount.get_ozon_account_page_text()
        expected_text = ozonaccount.OZONACCOUNT_PAGE_TEXT
        error_text = ozonaccount.ERROR_OZONACCOUNT_PAGE_TEXT
        assert expected_text == actual_text, 'Validate Ozon Account Page Text'
        assert actual_text != error_text
    
        homepage_nav.delete_cookies()
    
    # Testing Header Ozon Live Link
    def test_ozonlive_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_topfashion_link_clickable()
    
        homepage_nav.get_nav_links()[4].click()
        actual_url = homepage_nav.ozonlive_current_url()
        expected_url = URL_OZONLIVE
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        ozonlive = OzonLive(self.driver)
        actual_attribute = ozonlive.get_ozonlive_attribute()
        expected_attribute = ozonlive.OZONLIVE_IMAGE_ATTRIBUTE
        error_attribute = ozonlive.ERROR_OZONLIVE_IMAGE_ATTRIBUTE
        assert expected_attribute == actual_attribute, 'Validate Ozon Live Page Title Image Attribute'
        assert actual_attribute != error_attribute
    
        homepage_nav.delete_cookies()
    
    # Testing Header Sale Link
    def test_actions_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_sale_link_clickable()
    
        homepage_nav.get_nav_links()[5].click()
        actual_url = homepage_nav.sale_current_url()
        expected_url = URL_SALE
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        sale = Sale(self.driver)
        actual_title = sale.get_sale_title_text()
        expected_title = sale.SALE_PAGE_TEXT
        error_title = sale.ERROR_SALE_PAGE_TEXT
        assert expected_title == actual_title, 'Validate Sale Page Title Text'
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Brands Link
    def test_brands_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_brands_link_clickable()
    
        homepage_nav.get_nav_links()[6].click()
        actual_url = homepage_nav.brands_current_url()
        expected_url = URL_BRANDS
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        brands = Brands(self.driver)
        actual_title = brands.get_brands_title_text()
        expected_title = brands.BRANDS_PAGE_TITLE_TEXT
        error_title = brands.ERROR_BRANDS_PAGE_TITLE_TEXT
        assert expected_title == actual_title, 'Validate Brands Page Title Text'
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Sellers Link
    def test_sellers_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_sellers_link_clickable()
    
        homepage_nav.get_nav_links()[7].click()
        actual_url = homepage_nav.sellers_current_url()
        expected_url = URL_SELLERS
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        sellers = Sellers(self.driver)
        actual_title = sellers.get_sellers_title_text()
        expected_title = sellers.SELLERS_PAGE_TITLE_TEXT
        error_title = sellers.ERROR_SELLERS_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Certificates Link
    def test_certificates_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_certificates_link_clickable()
    
        homepage_nav.get_nav_links()[8].click()
        actual_url = homepage_nav.certificates_current_url()
        expected_url = URL_CERTIFICATES
        assert expected_url == actual_url
        response = requests.get(actual_url)
    
        assert response.status_code == 200
        certificates = Certificates(self.driver)
    
        actual_title = certificates.get_certificates_title_text()
        expected_title = certificates.CERTIFICATES_PAGE_TITLE_TEXT
        error_title = certificates.ERROR_CERTIFICATES_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Electronics Link
    def test_electronics_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_electronics_link_clickable()
    
        homepage_nav.get_nav_links()[9].click()
        actual_url = homepage_nav.electronics_current_url()
        expected_url = URL_ELECTRONICS
        assert expected_url == actual_url
        response = requests.get(actual_url)
    
        assert response.status_code == 200
        electronics = Electronics(self.driver)
    
        actual_title = electronics.get_electronics_title_text()
        expected_title = electronics.ELECTRONICS_PAGE_TITLE_TEXT
        error_title = electronics.ERROR_ELECTRONICS_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Apparel (Clothes and Footwear) Link
    def test_apparel_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_apparel_link_clickable()
    
        homepage_nav.get_nav_links()[10].click()
        actual_url = homepage_nav.apparel_current_url()
        expected_url = URL_APPAREL
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        apparel = Apparel(self.driver)
        actual_title = apparel.get_apparel_title_text_one()
        expected_title = apparel.APPAREL_PAGE_TITLE_TEXT_ONE
        error_title = apparel.ERROR_APPAREL_PAGE_TITLE_TEXT_ONE
        assert expected_title == actual_title
        assert actual_title != error_title
    
        actual_title = apparel.get_apparel_title_text_two()
        expected_title = apparel.APPAREL_PAGE_TITLE_TEXT_TWO
        error_title = apparel.ERROR_APPAREL_PAGE_TITLE_TEXT_TWO
        assert expected_title == actual_title
        assert actual_title != error_title
    
        actual_title = apparel.get_apparel_title_text_three()
        expected_title = apparel.APPAREL_PAGE_TITLE_TEXT_THREE
        error_title = apparel.ERROR_APPAREL_PAGE_TITLE_TEXT_THREE
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Children's Goods Link
    def test_childensgoods_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_electronics_link_clickable()
    
        homepage_nav.get_nav_links()[11].click()
        actual_url = homepage_nav.childrengoods_current_url()
        expected_url = URL_CHILDRENGOODS
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        childrengoods = Childrengoods(self.driver)
        actual_title = childrengoods.get_childrengoods_title_text()
        expected_title = childrengoods.CHILDRENGOODS_PAGE_TITLE_TEXT
        error_title = childrengoods.ERROR_CHILDRENGOODS_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Header Home and Garden Link
    def test_home_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_home_link_clickable()
    
        homepage_nav.get_nav_links()[12].click()
        actual_url = homepage_nav.home_current_url()
        expected_url = URL_HOME
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        home = Home(self.driver)
        actual_title = home.get_home_title_text()
        expected_title = home.HOME_PAGE_TITLE_TEXT
        error_title = home.ERROR_HOME_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
    
    # Testing Best Price Link
    def test_bestprice_link(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.is_bestprice_link_clickable()
    
        homepage_nav.get_nav_links()[13].click()
        actual_url = homepage_nav.bestprice_current_url()
        expected_url = URL_BESTPRICE
        assert expected_url == actual_url
    
        response = requests.get(actual_url)
        assert response.status_code == 200
    
        bestprice = BestPrice(self.driver)
        actual_title = bestprice.get_bestprice_title_text()
        expected_title = bestprice.BESTPRICE_PAGE_TITLE_TEXT
        error_title = bestprice.ERROR_BESTPRICE_PAGE_TITLE_TEXT
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_nav.delete_cookies()
