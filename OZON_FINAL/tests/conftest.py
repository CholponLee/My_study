import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options
from base.url import URL


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options


@pytest.fixture(scope='function')
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    url = URL
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()
