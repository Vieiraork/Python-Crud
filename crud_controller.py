from os import name, system
from time import sleep

from ControlUser import ControlUser
from config import Configs


def unhandled_option(opt_str: str) -> type(None):
    print(f"Invalid option! Option chosen -> '{opt_str}'")
    sleep(1)


def clear_console_by_platform() -> type(None):
    system("cls" if name == "nt" else "clear")


class CrudController:
    def handler(self, ctrl_usr: ControlUser) -> type(None):
        ctrl_usr.show_menu_options()
        print('-' * Configs['menu_size'])
        opt_str = input().strip()[0]
        self.handle_options(ctrl_usr, opt_str)

    def handle_options(self, ctrl_usr: ControlUser, opt_str: str) -> type(None):
        # check valid options
        if not opt_str.isdecimal():
            unhandled_option(opt_str)
        else:
            # handle options
            opt = int(opt_str)
            if not 0 <= opt <= 5:
                unhandled_option(opt_str)
            else:
                if Configs['standard_opts'].__contains__(opt):
                    nick_ = input("Your nickname: ")
                    pass_ = input("Your password: ")
                    if opt == 1:
                        ctrl_usr.register(nick_, pass_)
                    elif opt == 2:
                        ctrl_usr.update(nick_, pass_)
                    else:
                        ctrl_usr.delete(nick_, pass_)
                elif opt == 4:
                    ctrl_usr.display()
                else:
                    return

        # internal loop
        clear_console_by_platform()
        self.handler(ctrl_usr)
