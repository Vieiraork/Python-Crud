Configs = {
    'menu_size': 30,
    'standard_opts': [1, 2, 3],
    'table_line': 55,
    'db_config': {
        'add_samples': True,
        'name': "user.db",
        'pre_schema': [
            "DROP TABLE IF EXISTS `login`"
        ],
        'schema': [
            (
                "CREATE TABLE IF NOT EXISTS `login`(`id` INTEGER PRIMARY KEY AUTOINCREMENT, `nick` VARCHAR(20) "
                "UNIQUE, `password` VARCHAR(15))",
                [
                    (
                        "INSERT INTO `login`(`nick`, `password`) VALUES(?, ?)",
                        ('Man', '123456')
                    ),
                    (
                        "INSERT INTO `login`(`nick`, `password`) VALUES(?, ?)",
                        ('Woman', '123456')
                    )
                ]
            )
        ]
    }
}
