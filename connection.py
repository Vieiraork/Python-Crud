import _sqlite3

conect = _sqlite3.connect('user.db')
cursor = conect.cursor()

cursor.execute('DROP TABLE login')
cursor.execute('CREATE TABLE login(id INTEGER PRIMARY KEY AUTOINCREMENT, nick VARCHAR(20) UNIQUE, senha VARCHAR(15))')
# CREATE TABLE login(id INTEGER PRIMARY KEY AUTOINCREMENT, nick VARCHAR(20) UNIQUE, senha VARCHAR(15))

cursor.execute('INSERT INTO login(nick, senha) VALUES(?, ?)', ('Homem', '123456'))
cursor.execute('INSERT INTO login(nick, senha) VALUES(?, ?)', ('Mulher', '123456'))

conect.commit()

cursor.close()
conect.close()
