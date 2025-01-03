import sys
from abc import ABC, abstractmethod
from typing import Type
import validators
from unitsnet_py.units.duration import Duration

from connectivity_tool_cli.common.constances import MAX_TEST_TIMEOUT
from connectivity_tool_cli.common.interfances import Protocols
from connectivity_tool_cli.common.logger import logger
from connectivity_tool_cli.common.utils import is_valid_url


class ConnTestSuite(ABC):
    protocol: Protocols

    @staticmethod
    def create_suite(input_data: dict) -> "ConnTestSuite":
        """ Create a connectivity test suite instance based on the provided input. """
        protocol_raw: str = input_data['protocol']
        if not protocol_raw:
            logger.critical(f'The "protocol" field is required')
            sys.exit(1)

        protocol: Protocols = Protocols(protocol_raw.lower())
        if not protocol in Protocols.__members__.values():
            logger.critical(f"Protocol with name '{protocol}' is not supported")
            sys.exit(1)

        # Create the appropriate suite model based on the protocol
        suite_model = suite_map.get(protocol)()
        suite_model.protocol = protocol
        suite_model.load_data(input_data)
        return suite_model

    @abstractmethod
    def load_data(self, input_data: dict):
        """ Load the data from the input dictionary """
        pass


class ConnTestSuiteWWW(ConnTestSuite):
    url: str
    latency_threshold_deviation: Duration
    test_upload_bandwidth: bool
    test_download_bandwidth: bool

    def load_data(self, input_data: dict):
        self.url = input_data.get('url')
        if not self.url:
            logger.critical(f'Missing parameter "url" for the {self.protocol} protocol')
            sys.exit(1)

        if not is_valid_url(self.url, self.protocol):
            logger.critical(f'The "{self.url}" is not a valid url for the {self.protocol} protocol')
            sys.exit(1)

        self.latency_threshold_deviation = MAX_TEST_TIMEOUT
        latency_threshold_deviation = input_data.get('latency_threshold_deviation')
        if latency_threshold_deviation:
            self.latency_threshold_deviation = Duration.from_dto_json(latency_threshold_deviation)

        self.test_upload_bandwidth = input_data.get('test_upload_bandwidth') or False
        self.test_download_bandwidth = input_data.get('test_download_bandwidth') or False


class ConnTestSuiteDNS(ConnTestSuite):
    domain: str

    def load_data(self, input_data: dict):
        self.domain = input_data.get('domain')
        if not self.domain:
            logger.critical(f'Missing parameter "domain" for the {self.protocol} protocol')
            sys.exit(1)

        if not validators.domain(self.domain):
            logger.critical(f'The "{self.domain}" is not a valid domain')
            sys.exit(1)


suite_map: dict[Protocols, Type[ConnTestSuite]] = {
    Protocols.HTTPS: ConnTestSuiteWWW,
    Protocols.HTTP: ConnTestSuiteWWW,
    Protocols.DNS: ConnTestSuiteDNS,
}
