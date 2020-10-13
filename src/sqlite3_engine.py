from os import path
from sqlite3 import connect, Connection

from config import Configs
from py_logger import PyLogger


def establish_connection(logger: PyLogger) -> type(Connection):
    # check auto_create option
    db_config = Configs['db_config']
    res = db_config['name']
    drop_db = False

    # enable drop action when file exists only
    if path.exists(res):
        logger.info(msg=f'Database resource already exists.')
        logger.warn(msg="Do you want to DROP it or keep? (Y/N) [default: NO]")

        drop_db = input().lower()[0] == "y"

    # establish connection
    conn = connect(res)

    if not drop_db:
        logger.info(msg=f"Success! Using local configuration from '{res}'.")
        return conn

    cur = conn.cursor()

    logger.info(msg="Checking pre-schema drop actions...")

    # accurate pre-schema actions
    pre_schemas = db_config['pre_schema']
    for pre_schema in pre_schemas:
        if pre_schema.lower().startswith("drop"):
            cur.execute(pre_schema)

    pre_schema_count = len(pre_schemas)
    if pre_schema_count > 0:
        logger.info(msg=f"Successfully executed {pre_schema_count} pre-schema actions!")
    else:
        logger.info(msg="None pre-schema action executed.")

    logger.info(msg="Creating schema...")

    # accurate schema actions
    schema = db_config['schema']
    for table_def in schema:
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

    schema_count = len(schema)
    if schema_count > 0:
        logger.info(msg=f"Successfully executed {schema_count} schema actions!")
    else:
        logger.info(msg="None schema action executed.")

    conn.commit()
    logger.info(msg=f"Changes have been committed!")

    cur.close()
    logger.info(msg="Successfully created a new database schema!")

    return conn
