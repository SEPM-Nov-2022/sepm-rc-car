"""
The purpose of this file is to maintain utility-based functions used
throughout the application.
"""
import yaml

from .constants import ENV_FILE_DIR


def get_env(variable_name: str) -> str:
    """utility to get one env value"""
    with open(ENV_FILE_DIR, "r", encoding="utf-8") as stream:
        try:
            yaml_content_read = yaml.safe_load(stream)
            return yaml_content_read.get('variables')[variable_name]
        except yaml.YAMLError as yaml_except:
            raise yaml_except
