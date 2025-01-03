import logzero
from logzero import logger


class Logger:
    def __init__(self, log_file="aoc.log") -> None:
        """Initialise logger class.

        Args:
            name (string): Executing class name.
        """
        self.logger = logzero.setup_logger(name=__name__)

        logzero.loglevel(logzero.logging.INFO)
        logzero.logfile(log_file, maxBytes=1000000, backupCount=3)

    def get_logger(self, name):
        return logzero.logger


custom_logger = Logger()
