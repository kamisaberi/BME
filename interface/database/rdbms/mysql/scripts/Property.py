from interface.database.rdbms.mysql.scripts.Templates import *


class Property:

    @staticmethod
    def insert(table, item_id, data, connection):
        assigned_table_properties = str.format("{0}_assigned_properties", table)
        table_properties = str.format("{0}_properties", table)
        connection.cursor().execute(str.format(Templates.sqls["table.select.simple"], fields="*", table_name=table_properties))
        properties = connection.cursor().fetchall()
        # self.connection.cursor().execute(str.format(self.sql_templates["table.select.with.where"], fields="*", table_name=table_properties , where = 'item = ' + item_id))
        # assigned_properties = self.connection.cursor().fetchall()
        connection.cursor().execute(str.format(Templates.sqls["table.delete.with.where"], table_name=assigned_table_properties, where="item = " + item_id))

        for property in properties:
            if property['title'] in data:
                connection.cursor().execute(str.format(Templates.sqls["table.insert.single"], tabel_name=assigned_table_properties, fields="`item`,`property`,`value`",
                                                       values="'" + item_id + "','" + property['title'] + "','" + data[property['title']] + "'"))
            else:
                connection.cursor().execute(str.format(Templates.sqls["table.insert.single"], tabel_name=assigned_table_properties, fields="`item`,`property`",
                                                       values="'" + item_id + "','" + property['title'] + "'"))
            del data[property['title']]

    @staticmethod
    def update(table, item_id, data, connection):
        Property.delete(table, item_id, connection)
        Property.insert(table, item_id, data, connection)

    @staticmethod
    def delete(table, item_id, connection):
        connection.cursor().execute(str.format(Templates.sqls["table.delete.with.where"], fields="*", table_name=table, where='item=' + item_id))
