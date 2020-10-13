import _sqlite3
from config import Configs

# take values from config.py to set data base name
db_config = Configs['db_config']
res = db_config['name']

conn = _sqlite3.connect(res)
cur = conn.cursor()

# take color values from config.py
colors = Configs['colors']
# take value from lines of table in display mathod
lines = Configs['table_line']


class ControlUser:
    def show_menu_options(self) -> type(None):
        print(f'''{colors["white"]}    
    MENU OPTIONS, CHOOSE:
    1 - REGISTER
    2 - UPDATE
    3 - DELETE
    4 - LIST
    5 - QUIT''')

    def register(self, nick, passw) -> type(None):
        try:
            cur.execute('INSERT INTO login(nick, password) VALUES(?, ?)', (nick, passw))
        except _sqlite3.Error:
            print(f'{colors["red"]}Nick unavailable, try again.')
        else:
            print(f'{colors["green"]}Successful, user register!')
            conn.commit()

    def update(self, nick, passw) -> type(None):
        new_nick = input('Insert a new nick name: ')
        new_pass = input('Insert a new password: ')

        try:
            cur.execute('UPDATE login SET nick = ?, password = ? WHERE nick = ? AND password = ?',
                        (new_nick, new_pass, nick, passw))
        except _sqlite3.Error as e:
            print(f'{colors["red"]}Error: {e}')
        else:
            print(f'{colors["green"]}User successful updated!')
            conn.commit()

    def delete(self, nick, passw) -> type(None):
        try:
            cur.execute('DELETE FROM login WHERE nick = ? AND password = ?', (nick, passw))
        except Exception as ex:
            print(f'{colors["red"]}Error: {ex}')
        else:
            print('Successful')
            conn.commit()
        """except _sqlite3.DataError:
            print(f'{colors["red"]}Error')
        except _sqlite3.DatabaseError:
            print(f'{colors["red"]}Error')
        except _sqlite3.Error as e:
            print(f'{colors["red"]}{e}')
        except AttributeError:
            print(f'{colors["red"]}Error')
        except EnvironmentError:
            print(f'{colors["red"]}Error')
        except NameError:
            print(f'{colors["red"]}Error')
        except SyntaxError:
            print(f'{colors["red"]}Error')
        except TabError:
            print(f'{colors["red"]}Error')
        except IndexError:
            print(f'{colors["red"]}Error')"""

    def display(self) -> type(None):
        cur.execute('SELECT * FROM login')

        print(f'{"ID":^10}    {"Nick":^20}     {"Senha":^20}')
        print('-' * lines)

        for d in cur:
            print(f'{str(d[0]):^10}    {str(d[1]):^20}     {str(d[2]):^20} ')
            print('-' * lines)
