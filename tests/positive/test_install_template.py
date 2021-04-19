import pytest
import allure
from testfixtures import compare
from test_framework.test_data.yaml_data_generator import *


@allure.story("Successful template installation")
@pytest.mark.parametrize(
    argnames="generated_list_for_yml_file, tmpl_id",
    argvalues=[
        [one_button_with_id_and_label(), 1],
        [two_button_with_id_and_label(), None],
        [buttons_with_id_and_label(100), 2],
        [one_button_with_id_and_label(), "id_button"],
        [buttons_with_id_and_label(500), 3]
    ],
)
def test_success_template_install(api_client, base_page, generated_list_for_yml_file, tmpl_id):
    with allure.step('upload template'):
        response = api_client.upload_template(generated_list_for_yml_file, tmpl_id)
        tmpl_id = response['message'].split("tmpl_id=")[-1]
    with allure.step('check that Id appears in the list of templates'):
        list_templates = api_client.get_list_templates()
        assert tmpl_id in list_templates
    with allure.step('install the added template'):
        response = api_client.install_template(tmpl_id)
        response[0].raise_for_status()
    with allure.step('open the template in a browser and get a list of page elements'):
        list_elements_from_page = base_page.get_list_page_elements()
    with allure.step('creating a list of items to compare'):
        expected_list_elements_for_compare = list_elements_for_compare(generated_list_for_yml_file)
    with allure.step('compare the resulting list from the page, with the expected'):
        compare(list_elements_from_page, expected_list_elements_for_compare)


@allure.story("Successful template installation with label")
@pytest.mark.parametrize(
    argnames="generated_list_for_yml_file, tmpl_id",
    argvalues=[
        [hundred_button_with_link(), 1],
    ],
)
def test_success_template_with_link(api_client, base_page, generated_list_for_yml_file, tmpl_id):
    with allure.step('upload template'):
        response = api_client.upload_template(generated_list_for_yml_file, tmpl_id)
        tmpl_id = response['message'].split("tmpl_id=")[-1]
    with allure.step('check that Id appears in the list of templates'):
        list_templates = api_client.get_list_templates()
        assert tmpl_id in list_templates
    with allure.step('install the added template'):
        response = api_client.install_template(tmpl_id)
        response[0].raise_for_status()
    with allure.step('open the template in a browser and '
                     'check that I can click on the element if it has a label'):
        id_element = hundred_button_with_link()[0]['id']
        base_page.go_to_page()
        base_page.element_by_selector(f'[id="{id_element}"]').click()
    with allure.step('check that the address pages has changed to the expected'):
        expected_link = hundred_button_with_link()[0]['link']
        current_link = base_page.get_current_link()
        compare(current_link, expected_link)


@allure.story("Successful template installation with depends")
@pytest.mark.parametrize(
    argnames="generated_list_for_yml_file, tmpl_id",
    argvalues=[
        [two_button_with_id_and_label(), 1],
    ],
)
def test_success_template_with_depends(api_client, base_page, generated_list_for_yml_file, tmpl_id):
    with allure.step('upload template'):
        response = api_client.upload_template(generated_list_for_yml_file, tmpl_id)
        tmpl_id = response['message'].split("tmpl_id=")[-1]
    with allure.step('check that Id appears in the list of templates'):
        list_templates = api_client.get_list_templates()
        assert tmpl_id in list_templates
    with allure.step('install the added template'):
        response = api_client.install_template(tmpl_id)
        response[0].raise_for_status()
    with allure.step('open the template in a browser and get a list of page elements'):
        list_elements_from_page = base_page.get_list_page_elements()
    with allure.step('creating a list of items to compare'):
        expected_list_elements_for_compare = list_elements_for_compare(generated_list_for_yml_file)
    with allure.step('compare the resulting list from the page, with the expected'):
        compare(list_elements_from_page, expected_list_elements_for_compare)


