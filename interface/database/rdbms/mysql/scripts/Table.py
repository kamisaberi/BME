from interface.database.rdbms.include.Commands import *


class Table:
    @staticmethod
    def search(connection, table_name):
        fn = str.format(Commands.sqls["table.show.like"], table_name=table_name)
        cursor = connection.cursor()
        cursor.execute(fn)
        tables = cursor.fetchall()
        if table_name in tables:
            return True
        else:
            return False
