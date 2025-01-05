import logging
from logging.handlers import RotatingFileHandler

logging.root.setLevel(logging.DEBUG)
automation_ide_logger = logging.getLogger("TestPioneer")
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class AutomationIDELoggingHandler(RotatingFileHandler):

    # redirect logging stderr output to queue

    def __init__(self, filename: str = "TestPioneer.log", mode="w",
                 maxBytes:int=1073741824, backupCount:int=0):
        super().__init__(filename=filename, mode=mode, maxBytes=maxBytes, backupCount=backupCount)
        self.formatter = formatter
        self.setLevel(logging.DEBUG)

    def emit(self, record: logging.LogRecord) -> None:
        super().emit(record)


# File handler
file_handler = AutomationIDELoggingHandler()
automation_ide_logger.addHandler(file_handler)
