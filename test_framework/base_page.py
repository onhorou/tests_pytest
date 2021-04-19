from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from test_framework import log

DEFAULT_WAITING_ELEMENTS = 2
BASE_PAGE_URL = "http://0.0.0.0:5000"


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def element_by_selector(
            self, selector: str, delay=DEFAULT_WAITING_ELEMENTS
    ) -> Optional[WebElement]:
        try:
            el = WebDriverWait(self.browser, delay).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )

            log.info(f"Element by selector {selector} found")
            return el
        except Exception as e:
            log.info(f"Element by selector {selector} NOT found {e}")
            return None

    def elements_by_selector(
            self, selector, delay=DEFAULT_WAITING_ELEMENTS
    ):
        try:
            elems = WebDriverWait(self.browser, delay).until(
                expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, selector))
            )

            log.info(f"Elements by selector {selector} found")
            return elems
        except Exception as e:
            log.info(f"Elements by selector {selector} NOT found {e}")
            return None

    def go_to_page(self, uri=""):
        self.browser.get(BASE_PAGE_URL + uri)

    def get_current_link(self):
        current_url = self.browser.current_url
        return current_url.replace(BASE_PAGE_URL, "")

    def get_list_page_elements(self) -> Optional[list]:
        list_page_elements = []

        self.go_to_page()
        list_button = self.elements_by_selector('.form-group')
        for button in list_button:
            attribute_id = button.find_element_by_css_selector('button').get_attribute('id')
            attribute_label = button.find_element_by_css_selector('button').text
            list_page_elements.append({"id": attribute_id, "label": attribute_label})

        log.info(f"list page elements: {list_page_elements}")
        return list_page_elements
