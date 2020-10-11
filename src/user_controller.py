import _sqlite3

conn = _sqlite3.connect('user.db')
cur = conn.cursor()


class ControlUser:
    def __init__(self):
        pass

    def show_menu_options(self):
        print('''\033[1;30m    
Menu de opções, digite uma das opções:
    1 - REGISTRAR
    2 - ALTERAR
    3 - APAGAR
    4 - LISTAR
    5 - SAIR''')
        print('-=-' * 15)

    def register(self, nick, senha):
        cur.execute('INSERT INTO login(nick, senha) VALUES(?, ?)', (nick, senha))
        conn.commit()

    def update(self, nick, senha):
        novon = str(input('Digite o novo nick: '))
        novas = str(input('Digite a nova senha: '))

        cur.execute('UPDATE login SET nick = ?, senha = ? WHERE nick = ? AND senha = ?',
                    (novon, novas, nick, senha))
        conn.commit()

    def delete(self, nick, senha):
        cur.execute('DELETE FROM login WHERE nick = ? AND senha = ?', (nick, senha))
        conn.commit()

    def display(self):
        cur.execute('SELECT * FROM login')

        print(f'{"ID":^20}    {"Nick":^20}     {"Senha":^20}')
        print('-' * 50)

        for d in cur:
            print(f'{str(d[0]):^20}    {str(d[1]):^20}     {str(d[2]):^20} ')
            print('-' * 25)
            #
