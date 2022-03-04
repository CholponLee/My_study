import pytest
import requests
from base.url import URL, URL_MAP_PAGE
from pom.homepage_header import HomepageHeader
import time


@pytest.mark.usefixtures('setup')
class TestHomePage:

    # Testing Home Page Status Code
    def test_home_page_response(self):
        response = requests.get(URL)
        assert response.status_code == 200
    
    # Testing Header Links
    def test_header_links(self):
        homepage_header = HomepageHeader(self.driver)
        actual_links = homepage_header.get_header_links_text()
        expected_links = homepage_header.HEADER_LINK_TEXT
        error_links = homepage_header.ERROR_HEADER_LINK_TEXT
        assert expected_links == actual_links, 'Validate Header Links Text'
        assert actual_links != error_links
    
        homepage_header.delete_cookies()
    
    # Clicking all header links
    def test_header_links_clickable(self):
        homepage_header = HomepageHeader(self.driver)
    
        for index in range(0, 6):
            homepage_header.get_header_links()[index].click()
            time.sleep(2)
            homepage_header.get_header_link_back()
            time.sleep(2)
    
    # Testing City Choose Button
    def test_city_choose_button(self):
        homepage_header = HomepageHeader(self.driver)
    
        homepage_header.is_city_visible().click()
    
        city = homepage_header.CITY
        homepage_header.fill_city_form().send_keys(city)
        homepage_header.fill_city_form().send_keys(u'\ue007')
    
        actual_city = homepage_header.get_city_text()
        expected_city = homepage_header.CITY
        assert actual_city == expected_city
    
        homepage_header.delete_cookies()
    
    # Testing "Пункы выдачи" Link
    def test_pick_up_points_headerlink(self):
        homepage_header = HomepageHeader(self.driver)
        homepage_header.get_header_links()[6].click()
    
        homepage_header.is_city_visible().click()
        city = homepage_header.CITY
        homepage_header.fill_city_form().send_keys(city)
        homepage_header.fill_city_form().send_keys(u'\ue007')
    
        actual_url = homepage_header.get_map_page_url()
        expected_url = URL_MAP_PAGE
        assert expected_url == actual_url
    
        actual_title = homepage_header.get_map_page_title_text()
        expected_title = homepage_header.MAP_PAGE_TITLE
        error_title = homepage_header.ERROR_MAP_PAGE_TITLE
        assert expected_title == actual_title
        assert actual_title != error_title
    
        homepage_header.delete_cookies()
