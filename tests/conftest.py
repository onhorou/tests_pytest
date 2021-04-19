import pytest
from selenium import webdriver

from test_framework.api_client import ApiClient
from test_framework.base_page import BasePage
from test_framework.yaml_client import YamlClient


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture
def api_client(get_yaml_client):
    return ApiClient(get_yaml_client)


@pytest.fixture
def get_yaml_client():
    return YamlClient()


@pytest.fixture
def base_page(browser):
    return BasePage(browser)
