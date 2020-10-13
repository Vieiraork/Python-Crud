from bll_ops import BLLOps
from input_controller import InputController
from py_logger import PyLogger
from sqlite3_engine import establish_connection

if __name__ == '__main__':
    # setup PyLogger + terminal dependencies
    logger = PyLogger()
    logger.setup()

    # setup sqlite3 storage engine and create connection
    conn = establish_connection(logger=logger)

    # include BLL operations
    bll_ops = BLLOps(logger=logger, conn=conn)

    # configure input controller and internal handlers
    controller = InputController(bll_ops=bll_ops, logger=logger)
    controller.handler()

    # close connection with database
    conn.close()

    # stop running process
    exit(code=0)
