from urllib.parse import urlparse
import yaml
import json

from connectivity_tool_cli.common.interfances import Protocols


def yaml_to_json(yaml_string) -> str:
    """
    Convert a YAML string to a JSON string.

    Args:
        yaml_string (str): The YAML input as a string.

    Returns:
        str: The JSON output as a string.
    """
    try:
        yaml_data = yaml.safe_load(yaml_string)
        json_data = json.dumps(yaml_data, indent=2)
        return json_data
    except Exception as e:
        raise e


def is_valid_url(url: str, protocol: Protocols = Protocols.HTTPS) -> bool:
    """Validate if the provided URL is valid."""
    parsed = urlparse(url)

    if parsed.scheme != protocol.value:
        return False

    return all([parsed.scheme, parsed.netloc])
