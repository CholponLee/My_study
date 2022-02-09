import pytest
import requests
from base.url import URL, PARTIAL_URL_SEARCHING, PARTIAL_URL_WRONG_SEARCHING
from pom.homepage_searchfield import HomepageSearchField
from base.keys import SEARCH_FIELD_KEY, WRONG_SEARCH_FIELD_KEY


@pytest.mark.usefixtures('setup')
class TestSearchField:

    # Testing Home Page Status Code
    def test_home_page_response(self):
        response = requests.get(URL)
        assert response.status_code == 200

    # Testing Search Field
    def test_search_field(self):
        searchfield = HomepageSearchField(self.driver)

        searchfield.searchfield_clear()
        searchfield.fill_searchfield().send_keys(SEARCH_FIELD_KEY.lower())
        searchfield.search_button().click()

        actual_url = searchfield.get_searching_url()
        expected_partial_url = PARTIAL_URL_SEARCHING
        assert expected_partial_url == actual_url

        response = requests.get(actual_url)
        assert response.status_code == 200

        searchfield.delete_cookies()

    # Testing Search Field (Empty)
    def test_search_field_empty(self):
        searchfield = HomepageSearchField(self.driver)

        searchfield.searchfield_clear()
        searchfield.fill_searchfield().send_keys()
        searchfield.search_button_click()

        actual_url = searchfield.get_url_empty_search()
        expected_partial_url = URL
        assert expected_partial_url == actual_url

        response = requests.get(actual_url)
        assert response.status_code == 200

        searchfield.delete_cookies()

    # Testing Search Field (Wrong Keys)
    def test_search_field_wrong_keys(self):
        searchfield = HomepageSearchField(self.driver)

        searchfield.searchfield_clear()
        searchfield.fill_searchfield().send_keys(WRONG_SEARCH_FIELD_KEY.lower())
        searchfield.search_button_click()

        actual_title = searchfield.get_wrong_search_title_text()
        expected_title = searchfield.EXPECTED_WRONG_SEARCH_PAGE_TITLE_TEXT
        searchfield.get_wrong_search_title()
        assert expected_title == actual_title

        actual_url = searchfield.get_url_wrong_search()
        expected_url = PARTIAL_URL_WRONG_SEARCHING
        assert expected_url == actual_url

        response = requests.get(actual_url)
        assert response.status_code == 200

        searchfield.delete_cookies()
