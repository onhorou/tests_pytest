from test_framework.test_data import log


def list_elements_for_compare(generated_list_for_yml_file):
    for item in generated_list_for_yml_file:
        item.pop("link", None)
        item.pop("depends", None)

    log.info(f"list generated elements: {generated_list_for_yml_file}")
    return generated_list_for_yml_file


def one_button_with_id_and_label() -> list:
    return [{'id': '1', 'label': 'button1'}]


def two_button_with_id_and_label() -> list:
    return [{'id': '1', 'label': 'button1'}, {'id': '2', 'label': 'button2'}]


def buttons_with_id_and_label(number_buttons) -> list:
    list_elements = []
    for item in range(1, number_buttons+1):
        list_elements.append({"id": f"{item}", "label": f"button{item}"})
    return list_elements


def hundred_button_with_link() -> list:
    return [{"id": "1", "label": f"button1", "link": "/link1"}]


def two_button_with_depends() -> list:
    return [{'id': '1', 'label': 'button1'},
            {'id': '2', 'label': 'button2', 'depends': 1}]


def two_button_with_depends_not_present_parents() -> list:
    return [{'id': '1', 'label': 'button1'},
            {'id': '2', 'label': 'button2', 'depends': "3"}]
