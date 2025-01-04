import time
from abc import ABC, abstractmethod
import requests
from unitsnet_py.units.bit_rate import BitRate
from unitsnet_py.units.duration import Duration, DurationUnits

from connectivity_tool_cli.common.constances import MAX_TEST_TIMEOUT
from connectivity_tool_cli.common.interfances import Protocols
from connectivity_tool_cli.common.logger import logger
from connectivity_tool_cli.models.conn_result import ConnResult
from connectivity_tool_cli.models.conn_test_suite import ConnTestSuiteWWW
from connectivity_tool_cli.protocoles.protocol import Protocol
from connectivity_tool_cli.store.store_manager import StoreManager


class WWWProtocol(Protocol, ABC):
    def __check_upload_bandwidth(self, url, data_size=1024 * 1024) -> BitRate:
        payload = b'a' * data_size  # Create a payload of the specified size
        start_time = time.time()
        response = requests.post(url, data=payload, timeout=MAX_TEST_TIMEOUT.seconds)
        elapsed_time = time.time() - start_time

        if elapsed_time > 0:
            bandwidth = (data_size / elapsed_time) / 1024  # Bandwidth in KB/s
            return BitRate.from_kilobits_per_second(bandwidth)
        return BitRate.from_kilobits_per_second(0)

    def __check_download_bandwidth(self, url, chunk_size=1024) -> BitRate:
        start_time = time.time()
        response = requests.get(url, stream=True, timeout=MAX_TEST_TIMEOUT.seconds)
        total_data = 0

        # Read data in chunks
        for chunk in response.iter_content(chunk_size=chunk_size):
            total_data += len(chunk)

        elapsed_time = time.time() - start_time
        response.close()

        if elapsed_time > 0:
            bandwidth = (total_data / elapsed_time) / 1024  # Bandwidth in KB/s
            return BitRate.from_kilobits_per_second(bandwidth)
        return BitRate.from_kilobits_per_second(0)

    def __www_check(self, conn_test_suite: ConnTestSuiteWWW, curr_results: ConnResult):
        try:
            # Record the start time
            start_time = time.time()

            # Send the GET request
            response = requests.get(conn_test_suite.url, timeout=MAX_TEST_TIMEOUT.seconds)

            # Record the end time
            end_time = time.time()

            # Measure latency in milliseconds
            latency = Duration.from_seconds(end_time - start_time)
            curr_results.latency = latency
            # Check if the response status is >=200 and < 400
            if 200 <= response.status_code < 400:
                logger.info(f"URL returned status code 200. Latency: {latency.to_string()}")
            else:
                curr_results.success = False
                curr_results.error_message = f"URL returned status code {response.status_code}"
                logger.error(f"URL returned status code {response.status_code}. Latency: {latency.to_string()}")
        except requests.exceptions.RequestException as e:
            curr_results.success = False
            logger.error(f"Error accessing URL: {e}")
            curr_results.error_message = str(e)

    def __deviation_check(self, conn_test_suite: ConnTestSuiteWWW, curr_results: ConnResult):
        last_result = StoreManager.store().get_last_result(curr_results)
        if last_result is None:
            logger.info(
                f"No previous results found for deviation check on {curr_results.asset} using {curr_results.protocol}")
            return

        deviation = curr_results.latency - last_result.latency

        if deviation > conn_test_suite.latency_threshold_deviation:
            curr_results.deviation = deviation
            curr_results.alert = True
            curr_results.error_message = f"Latency deviation of {deviation.to_string()} exceeds threshold of {conn_test_suite.latency_threshold_deviation.to_string(DurationUnits.Second)} by {(deviation - conn_test_suite.latency_threshold_deviation).to_string(DurationUnits.Second)}"
            logger.error(
                f"Latency deviation from last run of {deviation.to_string()} exceeds threshold of {conn_test_suite.latency_threshold_deviation.to_string()} by {deviation - conn_test_suite.latency_threshold_deviation} for {curr_results.asset} using {curr_results.protocol}")
            return

        if curr_results.latency < last_result.latency:
            logger.info(f"The performance of {curr_results.asset} using {curr_results.protocol} has improved. Removed latency in {deviation.to_string(DurationUnits.Millisecond)} compared to {last_result.latency.to_string(DurationUnits.Millisecond)}")
        else:
            logger.info(f"The performance of {curr_results.asset} using {curr_results.protocol} has degraded. Yet, latency deviation of {deviation.to_string(DurationUnits.Millisecond)} does not exceed threshold of {conn_test_suite.latency_threshold_deviation.to_string(DurationUnits.Second)}")

    @abstractmethod
    def perform_check(self, conn_test_suite: ConnTestSuiteWWW):
        pass

    def _perform_www_check(self, protocol: Protocols, conn_test_suite: ConnTestSuiteWWW) -> ConnResult:
        pass
        """
        Perform a connectivity check using the HTTPS protocol.
        :param conn_test_suite: The connectivity test suite containing the URL to check
        :return:
        """
        # Simulate an HTTPS connectivity check
        # In a real implementation, this would involve making an HTTPS request
        # to the provided URL and checking the response status code
        logger.info(f'Performing "{protocol.value}" check to "{conn_test_suite.url}"...')

        # Return a success message
        results = ConnResult()
        results.protocol = protocol
        results.asset = conn_test_suite.url
        results.success = True  # Assume success unless an error occurs

        # Start with the most simple, WWW URL check
        self.__www_check(conn_test_suite, results)

        # Once there is no communication, abort the next checks
        if not results.success:
            return results

        self.__deviation_check(conn_test_suite, results)

        try:
            if conn_test_suite.test_upload_bandwidth:
                results.upload_bandwidth = self.__check_upload_bandwidth(conn_test_suite.url)
        except requests.exceptions.RequestException as e:
            results.success = False
            logger.error(f"Error testing upload bandwidth: {e}")
            results.error_message = str(e)

        try:
            if conn_test_suite.test_download_bandwidth:
                results.download_bandwidth = self.__check_download_bandwidth(conn_test_suite.url)
        except requests.exceptions.RequestException as e:
            results.success = False
            logger.error(f"Error testing download bandwidth: {e}")
            results.error_message = str(e)

        return results


class HTTPSProtocol(WWWProtocol, ABC):
    def perform_check(self, conn_test_suite: ConnTestSuiteWWW) -> ConnResult:
        return self._perform_www_check(Protocols.HTTPS, conn_test_suite)


class HTTPProtocol(WWWProtocol, ABC):
    def perform_check(self, conn_test_suite: ConnTestSuiteWWW) -> ConnResult:
        return self._perform_www_check(Protocols.HTTP, conn_test_suite)
