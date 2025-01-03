from abc import ABC
import socket
import requests

from connectivity_tool_cli.common.interfances import Protocols
from connectivity_tool_cli.common.logger import logger
from connectivity_tool_cli.models.conn_result import ConnResult
from connectivity_tool_cli.models.conn_test_suite import ConnTestSuiteDNS
from connectivity_tool_cli.protocoles.protocol import Protocol


class DNSProtocol(Protocol, ABC):

    def perform_check(self, conn_test_suite: ConnTestSuiteDNS) -> ConnResult:
        """
        Perform a connectivity check using the HTTPS protocol.
        :param conn_test_suite: The connectivity test suite containing the URL to check
        :return:
        """

        # Log the start of the check
        logger.info(f'Performing "DNS" check to "{conn_test_suite.domain}"...')

        # Return a success message
        results = ConnResult()
        results.protocol = Protocols.DNS
        results.asset = conn_test_suite.domain
        results.success = True  # Assume success unless an error occurs

        try:
            ip_address = socket.gethostbyname(conn_test_suite.domain)
            logger.info(f'Successfully resolved domain "{conn_test_suite.domain}" to IP address "{ip_address}" using DNS')
        except requests.exceptions.RequestException as e:
            results.success = False
            results.error_message = str(e)
            logger.error(f'Error resolving DNS domain "{conn_test_suite.domain}" to IP address: {e} ')

        return results

