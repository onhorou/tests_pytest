import pytest
import allure
from test_framework.test_data.yaml_data_generator import *


@allure.story("Template update with parent element NOT present in the list of elements")
@pytest.mark.parametrize(
    argnames="generated_list_for_yml_file, tmpl_id",
    argvalues=[
        [two_button_with_depends_not_present_parents(), 3]
    ],
)
def test_depends_not_present_parents_update(api_client, base_page, generated_list_for_yml_file, tmpl_id):
    with allure.step('upload template'):
        response = api_client.upload_template(generated_list_for_yml_file, tmpl_id)
        tmpl_id = response['message'].split("tmpl_id=")[-1]
    with allure.step('check that Id appears in the list of templates'):
        list_templates = api_client.get_list_templates()
        assert tmpl_id in list_templates
    with allure.step('install the added template'):
        response = api_client.install_template(tmpl_id)
        assert response[0].status_code == 400
