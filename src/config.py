Configs = {
    'menu_size': 20,
    'standard_opts': [1, 2, 3],
    'db_config': {
        'auto_create': True,
        'add_samples': True,
        'name': "user.db",
        'schema': [
            (
                "CREATE TABLE login("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "nick VARCHAR(20) UNIQUE, "
                "senha VARCHAR(15)"
                ")",
                [
                    (
                        "INSERT INTO login(nick, senha) VALUES(?, ?)",
                        ('Homem', '123456')
                    ),
                    (
                        "INSERT INTO login(nick, senha) VALUES(?, ?)",
                        ('Mulher', '123456')
                    )
                ]
            )
        ]
    }
}
