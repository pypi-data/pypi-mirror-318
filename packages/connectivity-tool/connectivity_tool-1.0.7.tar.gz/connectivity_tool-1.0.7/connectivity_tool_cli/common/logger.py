import logging

logger = logging.getLogger("ConnectivityTool")

# Configure logging
def setup_logger(verbose: bool):
    global logger
    logger.setLevel(logging.DEBUG)

    ## TODO: Add a file handler to log messages to a file

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO if verbose else logging.ERROR)  # Log to console based on verbosity
    console_formatter = logging.Formatter('[%(levelname)s][%(asctime)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger
