import re
from typing import Optional, Tuple, Any

import requests

from test_framework import log

BASE_URL = "http://0.0.0.0:5000"


class ApiClient:
    def __init__(self, yaml_client):
        self.yaml_client = yaml_client

    def upload_template(self, generated_list, tmpl_id=None) -> int:
        file = self.yaml_client.write_to_yaml_file(generated_list)
        if tmpl_id is not None:
            payload = {'data': '{"tmpl_id": "%s"}' % tmpl_id}
        else:
            payload = {}

        response = requests.post(f"{BASE_URL}/api/v1/templates",
                                 files=file,
                                 data=payload)
        log.info(f"upload_template: {response.json()}")
        response.raise_for_status()

        return response.json()

    def upload_template_txt_file(self, generated_list, tmpl_id=None) -> Tuple[Any, Any]:
        file = self.yaml_client.write_to_txt_file(generated_list)
        if tmpl_id is not None:
            payload = {'data': '{"tmpl_id": "%s"}' % tmpl_id}
        else:
            payload = {}

        response = requests.post(f"{BASE_URL}/api/v1/templates",
                                 files=file,
                                 data=payload)
        log.info(f"upload_template: {response.json()}")

        return response, response.json()

    @staticmethod
    def install_template(tmpl_id):
        response = requests.post(f"{BASE_URL}/api/v1/templates/{tmpl_id}/install")
        log.info(f"install_template code: {response} json: {response.json()}")

        return response, response.json()

    @staticmethod
    def get_list_templates() -> Optional[list]:
        response = requests.get(f"{BASE_URL}/api/v1/templates")
        response.raise_for_status()
        response = response.json()

        log.info(f"get_list_templates: {response}")
        return response['templates']

    @staticmethod
    def delete_template(tmpl_id):
        response = requests.delete(f"{BASE_URL}/api/v1/templates/{tmpl_id}")
        log.info(f"delete_template: code: {response} json: {response.json()}")

        log.info(f"delete_template: {response}")

        return response, response.json()

    @staticmethod
    def clearing_list_templates():
        list_templates = ApiClient.get_list_templates()
        for item in list_templates:
            ApiClient.delete_template(item)
