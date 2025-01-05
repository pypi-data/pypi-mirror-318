from enum import Enum


class Protocols(str, Enum):
    HTTPS = "https"
    HTTP = "http"
    DNS = "dns"


class SuiteFormats(str, Enum):
    YAML = "yaml"
    JSON = "json"
