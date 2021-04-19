import allure


@allure.story("Delete not existing template")
def test_delete_not_existing_template(api_client):
    with allure.step('delete not existing template'):
        response = api_client.delete_template(88)
        assert response[0].status_code == 404
