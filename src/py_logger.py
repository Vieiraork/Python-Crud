import sys
from datetime import datetime
from enum import Enum

from colorama import init
from termcolor import cprint


class PyLevel(Enum):
    INFO = 1,
    WARNING = 2,
    ERROR = 3,
    FATAL = 4


class PyLogger:
    def __init__(self):
        self.__log_pattern = None
        self.__log_stream = None

    def setup(self) -> type(None):
        self.__log_pattern = "[{time}] [{level}] {message}"

        # init colorama module
        init(autoreset=True)

    @property
    def __time_pattern(self) -> type(str):
        return "%d/%m/%Y - %H:%M:%S"

    @property
    def __get_time(self) -> type(str):
        now = datetime.now()
        return now.strftime(self.__time_pattern)

    def __format_log(self, lvl: PyLevel, msg: str) -> type(str):
        return str(self.__log_pattern).format(
            time=self.__get_time,
            level=lvl.name,
            message=msg
        )

    def info(self, msg: str) -> type(None):
        cprint(
            text=self.__format_log(
                lvl=PyLevel.INFO,
                msg=msg
            ),
            color='white',
            file=sys.stderr
        )

    def warn(self, msg: str) -> type(None):
        cprint(
            text=self.__format_log(
                lvl=PyLevel.WARNING,
                msg=msg
            ),
            color='yellow',
            file=sys.stderr
        )

    def error(self, msg: str) -> type(None):
        cprint(
            text=self.__format_log(
                lvl=PyLevel.ERROR,
                msg=msg
            ),
            color='red',
            file=sys.stderr
        )

    def fatal(self, msg: str) -> type(None):
        cprint(
            text=self.__format_log(
                lvl=PyLevel.FATAL,
                msg=msg
            ),
            color='white',
            on_color='on_red',
            file=sys.stderr
        )
