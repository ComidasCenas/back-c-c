import logging
import os


class Logger:
    def __init__(self, runpath):
        self.runpath = runpath
        log_levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.logging = logging
        if 'LOG_FILE' in os.environ:
            self.logging.basicConfig(
                format=os.environ['LOG_FORMAT'],
                datefmt=os.environ['LOG_DATE_FORMAT'],
                level=log_levels[os.environ['LOG_LEVEL']],
                filename=os.environ['LOG_FILE'],
                filemode=os.environ['LOG_MODE']
            )
        else:
            self.logging.basicConfig(
                format=os.environ['LOG_FORMAT'],
                datefmt=os.environ['LOG_DATE_FORMAT'],
                level=log_levels[os.environ['LOG_LEVEL']]
            )

    def debug(self, message):
        self.logging.debug(f'#{self.runpath}# {message}')

    def info(self, message):
        self.logging.info(f'#{self.runpath}# {message}')

    def warning(self, message):
        self.logging.warning(f'#{self.runpath}# {message}')

    def error(self, message):
        self.logging.error(f'#{self.runpath}# {message}')

    def critical(self, message):
        self.logging.critical(f'#{self.runpath}# {message}')
