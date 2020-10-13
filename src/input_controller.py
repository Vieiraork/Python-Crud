from os import name, system
from time import sleep

from bll_ops import BLLOps
from config import Configs
from py_logger import PyLogger


def clear_console_by_platform() -> type(None):
    system(command="cls" if name == "nt" else "clear")


class InputController:
    def __init__(self, bll_ops: BLLOps, logger: PyLogger):
        self.__bll_ops = bll_ops
        self.__logger = logger

    @property
    def _logger(self) -> type(PyLogger):
        return self.__logger

    @_logger.setter
    def _logger(self, val: PyLogger) -> type(None):
        self.__logger = val

    @property
    def _bll_ops(self) -> type(BLLOps):
        return self.__bll_ops

    @_bll_ops.setter
    def _bll_ops(self, val: BLLOps) -> type(None):
        self.__bll_ops = val

    def handler(self) -> type(None):
        self.__bll_ops.show_menu_options()
        self.__logger.info(msg='-' * Configs['menu_size'])

        opt_str = input().strip()[0]
        self.__handle_options(opt_str=opt_str)

    def __unhandled_option(self, opt_str: str) -> type(None):
        self._logger.warn(msg=f"Invalid option! Option chosen -> '{opt_str}'")
        sleep(secs=1)

    def __handle_options(self, opt_str: str) -> type(None):
        # wipe console texts
        clear_console_by_platform()

        # check valid options
        if not opt_str.isdecimal():
            self.__unhandled_option(opt_str=opt_str)
        else:
            # handle options
            opt = int(opt_str)
            if not 0 <= opt <= 5:
                self.__unhandled_option(opt_str=opt_str)
            else:
                if Configs['standard_opts'].__contains__(opt):
                    self._logger.info("Nickname:")
                    nick_ = input()
                    self._logger.info("Password:")
                    pass_ = input()
                    if opt == 1:
                        self._bll_ops.register(
                            nick_=nick_,
                            pass_=pass_
                        )
                    elif opt == 2:
                        self._bll_ops.update(
                            nick_=nick_,
                            pass_=pass_
                        )
                    else:
                        self._bll_ops.delete(
                            nick_=nick_,
                            pass_=pass_
                        )
                elif opt == 4:
                    self._bll_ops.display()
                else:
                    return

        # internal loop
        self.handler()
