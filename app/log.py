import logging


class Log:
    def __init__(self):
        pass
    @staticmethod
    def init():
        logging.basicConfig(filename="/tmp/happay.log", level=logging.ERROR)

    @staticmethod
    def log_error(msg):
        logging.error(msg)

    @staticmethod
    def log_debug(msg):
        logging.debug(msg)

    @staticmethod
    def log_warning(msg):
        logging.warning(msg)
