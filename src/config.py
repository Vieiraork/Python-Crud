Configs = {
    'menu_size': 30,
    'standard_opts': [1, 2, 3],
    'colors': {
        'white': '\033[1;30m',
        'red': '\033[1;31m',
        'green': '\033[1;32m'
    },
    'table_line': 55,
    'db_config': {
        'auto_create': True,
        'add_samples': True,
        'name': "user.db",
        'schema': [
            (
                '''CREATE TABLE login(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nick VARCHAR(20) UNIQUE,
                password VARCHAR(15)
                )''',
                [
                    (
                        "INSERT INTO login(nick, password) VALUES(?, ?)",
                        ('Man', '123456')
                    ),
                    (
                        "INSERT INTO login(nick, password) VALUES(?, ?)",
                        ('Woman', '123456')
                    )
                ]
            )
        ]
    }
}
