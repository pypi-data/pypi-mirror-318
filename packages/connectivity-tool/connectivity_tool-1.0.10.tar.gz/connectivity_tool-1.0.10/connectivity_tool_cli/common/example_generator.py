import os

from connectivity_tool_cli.common.logger import logger

from connectivity_tool_cli.common.interfances import SuiteFormats
from connectivity_tool_cli.common.utils import yaml_to_json

yaml_example = """
suite:
  - protocol: DNS
    domain: "ynet.co.il"

  - protocol: DNS
    domain: "yahoo.com"

  - protocol: HTTP
    url: "http://www.google.com"

  - protocol: HTTPS
    url: "https://www.facebook.com"
    latency_threshold_deviation:
      value: 1
      unit: Millisecond
    test_upload_bandwidth: true
    test_download_bandwidth: true
"""


def generate_example_suite_file(path: str, format_type: SuiteFormats):
    # Create the path if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)

    # Create the file
    file_path = os.path.join(path, 'test_suite.' + format_type.value)
    logger.info(f'Creating example suite file at: {file_path}')
    with open(file_path, 'w') as f:
        if format_type == SuiteFormats.YAML:
            f.write(yaml_example)
            logger.info('Example YAML suite file created successfully')
            return

        if format_type == SuiteFormats.JSON:
            f.write(yaml_to_json(yaml_example))
            logger.info('Example JSON suite file created successfully')
            return
