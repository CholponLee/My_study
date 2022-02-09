from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List



class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def get_current_url(self):
        return self.driver.current_url

    def get_forward(self):
        return self.driver.forward()

    def get_back(self):
        return self.driver.back()

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css_selector': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_presence(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_presence(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> object:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def get_text_from_web_element(self, element) -> str:
        return element.text

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def find_element(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.driver.find_element((self.__get_selenium_by(find_by), locator), locator_name)

    def delete_cookie(self) -> None:
        self.driver.delete_all_cookies()
