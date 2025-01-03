from abc import ABC, abstractmethod

from connectivity_tool_cli.models.conn_result import ConnResult


class StoreBase(ABC):
    """
    Abstract base class representing a store service.
    """

    @abstractmethod
    def log_results(self, result: ConnResult):
        """
        Log the results of a connectivity check to the store.

        :param result: The results of the connectivity check.
        """
        pass

    @abstractmethod
    def get_last_result(self, curr_result: ConnResult) -> ConnResult | None:
        """
        Retrieve last result from the store.

        :return: The last result from the store, or None if no results are available.
        """
        pass