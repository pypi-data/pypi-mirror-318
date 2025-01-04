import argparse
import json
import sys

from connectivity_tool_cli.common.example_generator import generate_example_suite_file
from connectivity_tool_cli.common.input_loader import parse_input
from connectivity_tool_cli.common.interfances import Protocols, SuiteFormats
from connectivity_tool_cli.common.logger import setup_logger, logger
from connectivity_tool_cli.generated_build.build_info import print_cli_build_info
from connectivity_tool_cli.models.conn_test_suite import ConnTestSuite
from connectivity_tool_cli.protocoles.dns_protocol import DNSProtocol
from connectivity_tool_cli.protocoles.www_protocol import HTTPSProtocol, HTTPProtocol
from connectivity_tool_cli.protocoles.protocol import Protocol
from connectivity_tool_cli.store.store_manager import StoreManager

protocols_map: dict[Protocols, Protocol] = {
    Protocols.HTTPS: HTTPSProtocol(),
    Protocols.HTTP: HTTPProtocol(),
    Protocols.DNS: DNSProtocol(),
}


def main_function():
    parser = argparse.ArgumentParser(description='Welcome to the Connectivity Tool CLI')

    parser.add_argument('-i', '--info',
                        action='store_true',
                        help='Show CLI info')

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Show verbose output')

    parser.add_argument('-p', '--protocol',
                        choices=[protocol.value for protocol in Protocols],
                        help='Protocol to use for the connectivity test # used when file is not provided')

    parser.add_argument('-u', '--url',
                        help='The URL to use for the connectivity test e.g. https://www.google.com # used when file is not provided')

    parser.add_argument('-d', '--domain',
                        help='Domain to use for the connectivity test e.g. google.com # used when file is not provided')

    parser.add_argument('-f', '--suite-file',
                        help='Path to the suite file with all the connectivity tests')

    parser.add_argument('-t', '--type-format',
                        choices=[suiteFormat.value for suiteFormat in SuiteFormats],
                        default=SuiteFormats.YAML.value,
                        help='The format of the test suite file')

    parser.add_argument('-s', '--store',
                        default='./store_data/conn_tool_store.jsonl',
                        help='Path to the connectivity tool store file, in case of a docker use, make sure to mount the volume')

    parser.add_argument('-g', '--generate-path',
                        help='Path to a directory to generate the suite file example (see --type-format options)')

    parser.add_argument('-o', '--output-store',
                        type=int,
                        help='Print the last X lines store data to the output, set -1 to print all')

    # Parse the command-line arguments
    args = parser.parse_args()
    verbose = args.verbose
    info = args.info

    store_path = args.store
    if info:
        print('Connectivity Tool CLI by Haim Kastner hello@haim-kastner.com')
        print(f'    {print_cli_build_info()}')
        print()
        return

    setup_logger(verbose)
    if verbose:
        print(f'Connectivity Tool CLI')
        print(f'    {print_cli_build_info()}')

    if args.generate_path:
        generate_example_suite_file(args.generate_path, args.type_format)
        return



    try:
        # Init the store
        StoreManager.initialize(store_path)
    except Exception as e:
        logger.critical(f'Failed to init the connectivity tool store at {store_path} {str(e)}')
        sys.exit(1)

    if args.output_store:
        try:
            StoreManager.initialize(store_path)
            store_lines = StoreManager.store().get_last_results(args.output_store if args.output_store != -1 else None)
            logger.info(f'Printing {len(store_lines)} fetched lines from the store')
            for line in store_lines:
                print(json.dumps(line.to_dics()))
        except Exception as e:
            logger.critical(f'Failed to print the store data {str(e)}')
        return

    suites: [ConnTestSuite] = parse_input(args)

    try:
        for inx, suite in enumerate(suites):
            logger.info(f'-- Running test suite #{inx + 1} using {suite.protocol.value} protocol --')
            logger.debug(suite)

            # Get the protocol to use
            protocol = protocols_map[suite.protocol]
            # Run the test/s
            result = protocol.perform_check(suite)
            # Log the result
            StoreManager.store().log_results(result)
            logger.info(f'Connectivity check result: {result.to_dics()}')

    except Exception as e:
        logger.critical(f'Fatal error during connectivity check {str(e)}')


if __name__ == "__main__":
    main_function()
