import json
import sys
from argparse import Namespace

from connectivity_tool_cli.common.interfances import SuiteFormats
from connectivity_tool_cli.common.logger import logger
from connectivity_tool_cli.common.utils import yaml_to_json
from connectivity_tool_cli.models.conn_test_suite import ConnTestSuite


def _load_suite_file(file_path: str, format_type: SuiteFormats) -> dict:
    content = ''
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        logger.critical(f'File {file_path} not found.')
        exit(1)
    if format_type == SuiteFormats.YAML:
        return json.loads(yaml_to_json(content))
    return json.loads(content)


def _suite_file_input(args: Namespace) -> [ConnTestSuite]:
    suite = _load_suite_file(args.suite_file, SuiteFormats(args.type_format))

    conn_test_suite = []
    for input_data in suite['suite']:
        conn_test_suite.append(ConnTestSuite.create_suite(input_data))

    return conn_test_suite


def parse_input(args: Namespace) -> [ConnTestSuite]:
    # Once we have the suite file, we can ignore all other parameters
    if args.suite_file:
        return _suite_file_input(args)

    if not args.protocol:
        logger.critical('Protocol parameter is missing, see --help for all available protocols')
        sys.exit(1)

    param_dict = {'protocol': args.protocol}
    if args.url:
        param_dict['url'] = args.url
    if args.domain:
        param_dict['domain'] = args.domain

    return [ConnTestSuite.create_suite(param_dict)]
