import yaml

def load_config(file_path='config/config.yaml'):
    """
    Cargar la configuración desde un archivo YAML.
    """
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
