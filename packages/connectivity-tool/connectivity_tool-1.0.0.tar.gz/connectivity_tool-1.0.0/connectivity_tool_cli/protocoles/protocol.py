import sys
from abc import ABC, abstractmethod

from connectivity_tool_cli.common.logger import logger
from connectivity_tool_cli.models.conn_result import ConnResult
from connectivity_tool_cli.models.conn_test_suite import ConnTestSuite

class Protocol(ABC):
    """
    Abstract base class representing a protocol.
    Child classes must implement specific protocol behavior.
    """

    @abstractmethod
    def perform_check(self, parameter: ConnTestSuite) -> ConnResult:
        """
        Perform the connectivity check using the provided parameter.
        Should return a response string indicating success or failure.
        """
        pass



