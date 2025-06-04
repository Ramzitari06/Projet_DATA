import yaml

def load_config(config_path="C:/Users/User/OneDrive/Desktop/Formation/ECO_TRANS/config.yaml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)