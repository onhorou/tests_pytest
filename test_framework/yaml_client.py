import yaml


class YamlClient:
    @staticmethod
    def write_to_yaml_file(generated_list: list) -> dict:
        with open("template_file.yaml", "w") as file:
            yaml.dump(generated_list, file)
        return {'file': open('template_file.yaml', 'rb')}

    @staticmethod
    def write_to_txt_file(generated_list: list) -> dict:
        with open("template_file.txt", "w") as file:
            yaml.dump(generated_list, file)
        return {'file': open('template_file.txt', 'rb')}
