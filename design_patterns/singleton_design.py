class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.load_configuration()
        return cls._instance

    def load_configuration(self) -> None:
        try:
            with open('config.txt', 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    setattr(self, key, value)
        except FileNotFoundError:
            print("Configuration file 'config.txt' not found.")

    def get_setting(self, setting_name: str) -> str:

        return getattr(self, setting_name, None)


def main():
    config_manager = ConfigurationManager()

    print(config_manager.get_setting("setting1"))  # Output: value1
    print(config_manager.get_setting("setting2"))  # Output: value2


if __name__ == "__main__":
    main()
