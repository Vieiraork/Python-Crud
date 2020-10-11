from _sqlite3 import connect
from os import path

from config import Configs


def setup() -> type(None):
    # check auto_create option
    db_config = Configs['db_config']
    if not db_config['auto_create']:
        return

    res = db_config['name']
    drop_db = False

    # enable drop action when file exists only
    if path.exists(res):
        print("Database resource already exists.")
        drop_db = input("Do you want to DROP it or keep? (Y/N) [default: NO] ").lower() == "y"

    if not drop_db:
        print("Success! Using local configuration.")
        return

    conn = connect(res)
    cur = conn.cursor()

    # accurate drop action
    cur.execute("DROP TABLE login")
    print("Disposing database data...")

    # create tables
    print("Creating schema...")
    for table_def in db_config['schema']:
        # create table
        cur.execute(table_def[0])

        # verify and add samples
        if db_config['add_samples'] \
                and not table_def[1] is None \
                and len(table_def[1]) > 0:
            for table_sample in table_def[1]:
                cur.execute(
                    table_sample[0],
                    None if table_sample[1] is None else table_sample[1]
                )

    print("Changes have been committed!")
    conn.commit()

    cur.close()
    conn.close()
    print("Successfully created a new database schema!")
