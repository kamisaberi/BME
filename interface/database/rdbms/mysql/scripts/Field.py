from interface.database.rdbms.mysql.scripts.Templates import *
from base.database_types import *


class Field:
    @staticmethod
    def create_fields_for_install(self, fields):
        flds = []
        for field in fields:
            flds.append(Field.create_field(self, field, fields[field]))

        return ",".join(flds)

    @staticmethod
    def generate_appropriate_type(type, database_type='mysql'):
        return DataBaseTypes.types[mysql][type]

    @staticmethod
    def create_field(self, title, properties):
        s = title + ""

        if "type" in properties:
            s += Field.generate_appropriate_type(properties["type"])

        if "key" in properties and properties["key"]:
            s += " PRIMARY KEY "

        if "default" in properties:
            s += " DEFAULT " + properties["default"] + " "

        if "extra" in properties:
            if "ai" in properties['extra']:
                s += " AUTO_INCREMENT "

            if "not null" in properties['extra']:
                s += " NOT NULL "

        return s

    @staticmethod
    def get_fields(table, connection=None):
        connection.cursor().execute(str.format(Templates.sqls['table.get.fields'], table_name=table))
        return connection.cursor.fetchall()

    @staticmethod
    def get_available_fields(table, data, connection=None):
        all_fields = Field.get_fields(table, connection)
        fields = {}
        for field in all_fields:
            if field[0] in data:
                fields[field[0]] = data[field[0]]
        return fields
