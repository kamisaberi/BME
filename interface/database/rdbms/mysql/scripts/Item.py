from interface.database.rdbms.mysql.scripts.Field import *
from interface.database.rdbms.mysql.scripts.Property import *
from resources.database.Tables import *


class Item:
    id = 0
    table = ''
    data = []
    connection = None

    def __init__(self, table, id, connection):
        self.id = id
        self.table = table
        self.connection = connection

    def insert(self):
        fields = Field.get_available_fields(self.table, self.data, self.connection)
        f_names = []
        f_values = []
        for field in fields:
            f_names.append("`" + field + "`")
            f_values.append("'" + fields[field] + "'")
        self.connection.cursor().execute(Templates.sqls["table.insert.single"], table_name=self.table, fields=",".join(f_names), values=",".join(f_values))
        last_item_id = self.connection.cursor().lastrowid
        for tbl in Tables.backends['tables']:
            if self.table == tbl['title']:
                if "has_property_table" in tbl and tbl["has_property_table"]:
                    Property.insert(self.table, last_item_id, self.data, self.connection)

    def update(self):
        fields = Field.get_available_fields(self.table, self.data, self.connection)
        f_names = []
        f_values = []
        for field in fields:
            f_names.append("`" + field + "`")
            f_values.append("'" + fields[field] + "'")
        self.connection.cursor().execute(Templates.sqls["table.update.with.where"], table_name=self.table, fields_values=",".join(f_names), where=",".join(f_values))
        last_item_id = self.connection.cursor().lastrowid
        for tbl in Tables.backends['tables']:
            if self.table == tbl['title']:
                if "has_property_table" in tbl and tbl["has_property_table"]:
                    Property.insert(self.table, last_item_id, self.data, self.connection)

    def delete(self):
        sql = str.format(Templates.sqls["table.delete.with.where"], table_name=self.table, where="WHERE id=" + self.id)
        self.connection.cursor().execute(sql)
        for tbl in Tables.backends['tables']:
            if self.table == tbl['title']:
                if tbl['table_has_property']:
                    sql = str.format(Templates.sqls["table.delete.with.where"], table_name=self.table + "_assigned_properties", where="WHERE item=" + self.id)
                    self.connection.cursor().execute(sql)
