class DispatchConfig:
    def __init__(self, raw_config):
        self.registered_commands = {}
        for package in raw_config["handlers"]:
            for command in package["commands"]:
                self.registered_commands[command] = {
                    "class": package["class"],
                    "fullpath": ".".join([package["package"], package["module"], package["class"]])
                }

    def get_handler_by_command(self, command):
        if command in self.registered_commands:
            return self.registered_commands[command]
        else:
            return None
