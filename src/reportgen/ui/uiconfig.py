from configparser import ConfigParser
import os
class Config:
    def __init__(self, config_file_path ="src/reportgen/ui/uiconfig.ini"):
        self.config = ConfigParser()
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file not found: {config_file_path}")
        self.config.read(config_file_path)
    def get_llms(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    def get_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    def get_groq_model(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    def get_openai_model(self):
        return self.config["DEFAULT"].get("OPENAI_MODELS_OPTION").split(", ")
    
if __name__ == '__main__':
    configurator = Config()
    print(configurator.get_llms())