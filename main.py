from ControlUser import ControlUser
from connection import setup
from crud_controller import CrudController

if __name__ == '__main__':
    setup()

    ctrl_usr = ControlUser()
    controller = CrudController()
    controller.handler(ctrl_usr)

    exit(0)
