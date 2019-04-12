import json


class Configurator:

    def __init__(self, config_file):
        self.config = None
        with open(config_file) as json_file:
            self.config = json.load(json_file)

    def get_config(self, component_name):
        return self.config[component_name]
