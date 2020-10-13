from sqlite3 import Connection, Error

from config import Configs
from py_logger import PyLogger


class BLLOps:
    def __init__(self, logger: PyLogger, conn: Connection):
        self._logger = logger
        self._conn = conn
        self.__line = Configs['table_line']

    @property
    def _logger(self) -> type(PyLogger):
        return self.__logger

    @_logger.setter
    def _logger(self, val: PyLogger) -> type(None):
        self.__logger = val

    @property
    def _conn(self) -> type(Connection):
        return self.__conn

    @_conn.setter
    def _conn(self, val: Connection) -> type(None):
        self.__conn = val

    def show_menu_options(self) -> type(None):
        self._logger.info(
            msg=f'''MENU OPTIONS, CHOOSE:
            1 - REGISTER
            2 - UPDATE
            3 - DELETE
            4 - LIST
            5 - QUIT'''
        )

    def register(self, nick_: str, pass_: str) -> type(None):
        try:
            cur.execute(
                sql='INSERT INTO login(nick, password) VALUES(?, ?)',
                parameters=(nick_, pass_)
            )
        except Error:
            self._logger.error(msg='Nick unavailable, try again.')
        else:
            self._logger.info(msg='Successful, user register!')
            self._conn.commit()

    def update(self, nick_: str, pass_: str) -> type(None):
        self._logger.info(msg="Insert a new nickname:")
        new_nick = input()

        self._logger.info(msg="Insert a new password:")
        new_pass = input()

        cur = self._conn.cursor()
        try:
            cur.execute(
                sql='UPDATE login SET nick = ?, password = ? WHERE nick = ? AND password = ?',
                parameters=(new_nick, new_pass, nick_, pass_)
            )
            self._logger.info(msg='Successfully updated the user!')
            self._conn.commit()
        except Error as e:
            self._logger.error(msg=f'Error: {e}')
        finally:
            cur.close()

    def delete(self, nick_: str, pass_: str) -> type(None):
        cur = self._conn.cursor()
        try:
            cur.execute(
                sql='DELETE FROM login WHERE nick = ? AND password = ?',
                parameters=(nick_, pass_)
            )
            self._logger.info(msg='Successfully deleted the user!')
            self._conn.commit()
        except Exception as e:
            self._logger.error(msg=f'Error: {e}')
        finally:
            cur.close()

    def display(self) -> type(None):
        cur = self._conn.cursor()
        cur.execute('SELECT * FROM login')

        self._logger.info(msg=f'{"ID":^10}    {"Nickname":^20}     {"Password":^20}')
        self._logger.info(msg='-' * self.__line)

        rows = cur.fetchall()
        for row in rows:
            self._logger.info(msg=f'{str(row[0]):^10}    {str(row[1]):^20}     {str(row[2]):^20} ')
            self._logger.info(msg='-' * self.__line)
