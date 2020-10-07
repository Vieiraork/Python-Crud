import _sqlite3

conect = _sqlite3.connect('user.db')
mycursor = conect.cursor()


class ControlUser:
    def __init__(self):
        pass

    def opcoes(self):
        print('''\033[1;30m    
Menu de opções, digite uma das opções:
    1 - REGISTRAR
    2 - ALTERAR
    3 - APAGAR
    4 - LISTAR''')
        print('-=-' * 15)

    def registrar(self, nick, senha):
        mycursor.execute('INSERT INTO login(nick, senha) VALUES(?, ?)', (nick, senha))
        conect.commit()

    def alterar(self, nick, senha):
        novon = str(input('Digite o novo nick: '))
        novas = str(input('Digite a nova senha: '))

        mycursor.execute('UPDATE login SET nick = ?, senha = ? WHERE nick = ? AND senha = ?', (novon, novas, nick, senha))
        conect.commit()

    def apagar(self, nick, senha):
        mycursor.execute('DELETE FROM login WHERE nick = ? AND senha = ?', (nick, senha))
        conect.commit()

    def listar(self):
        mycursor.execute('SELECT * FROM login')

        print('ID      Nick     Senha')
        print('-' * 25)

        for d in mycursor:
            print(f'{d[0]}    {d[1]}    {d[2]}')
            print('-' * 25)
