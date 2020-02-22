import mysql.connector
from interface.database.rdbms.mysql.scripts.Templates import *
from base.models import *
import inflect
from interface.database.rdbms.include.Commands import *
from config.base import *
from config.connection import *


class Database:
    connection = None
    cursor = None
    db_nam = None

    def __init__(self, db_name):
        self.db_name = db_name

    def open(self):
        self.connection = mysql.connector.connect(
            host=Connection.connections[Base.active_connection][0]['host'],
            user=Connection.connections[Base.active_connection][0]['user'],
            passwd=Connection.connections[Base.active_connection][0]['password'],
            database=Connection.connections[Base.active_connection][0]['database']
        )

    def close(self):
        self.connection.close()

    def get_data(self, table="all"):
        self.open()
        models = Models.base.copy()
        output = {}
        if table == "all":
            for model_name in models:
                try:
                    if models[model_name]['has_properties']:
                        output[model_name] = self.parse_data(model_name, True)
                    else:
                        output[model_name] = self.parse_data(model_name, False)
                except NameError as error:
                    print(error)
                except mysql.connector.errors.ProgrammingError as error:
                    print(error.msg)
            return output
        else:
            try:
                if models[table]['has_properties']:
                    return self.parse_data(table, True)
                else:
                    return self.parse_data(table, False)
            except NameError as error:
                print(error)
            except mysql.connector.errors.ProgrammingError as error:
                print(error.msg)

    def parse_data(self, table, has_property=False):
        engine = inflect.engine()
        cursor = self.connection.cursor()
        cursor.execute(str.format(Commands.sqls['table.select.simple'], fields='*', table_name=engine.plural(str.lower(table))))
        columns = cursor.column_names
        result = cursor.fetchall()

        datas = []
        for x in result:
            data = {}
            for y in columns:
                data[y] = x[columns.index(y)]
            datas.append(data)

        if has_property:
            datas = self.parse_properties(table, datas)

        return datas

    def parse_properties(self, model_name, datas):
        try:
            cursor = self.connection.cursor()
            cursor.execute(str.format(Commands.sqls['table.select.simple'], fields='*', table_name=str.lower(model_name) + "_properties"))
            properties = cursor.fetchall()
            prp_keys = cursor.column_names
            cursor = self.connection.cursor()
            cursor.execute(
                str.format(Commands.sqls['table.select.simple'] + " ORDER BY item", fields='*', table_name=str.lower(model_name) + "_assigned_properties"))
            assigned_properties = cursor.fetchall()
            ass_keys = cursor.column_names
            ass_prps = []
            for data in datas:
                ass_prp = {}
                id = data['id']
                tmp_assg = []
                for assigned_property in assigned_properties:
                    if assigned_property[ass_keys.index('item')] == id:
                        tmp_assg.append(assigned_property)

                for tmp in tmp_assg:
                    for prp in properties:
                        if tmp[ass_keys.index("property")] == prp[prp_keys.index("id")]:
                            ass_prp[prp[prp_keys.index("title")]] = tmp[ass_keys.index("value")]

                ass_prps.append(ass_prp)
                data['properties'] = ass_prp
        except mysql.connector.errors.ProgrammingError as error:
            print(error)
        return datas

    def install(self):
        engine = inflect.engine()
        models = Models.base.copy()
        for model_name in models:
            try:
                fn = str.format(Commands.sqls["table.create"], table_name=str(model_name), fields=",".join(models[model_name]['main']))
                self.connection.cursor.execute(fn)

                if models[model_name]['has_properties']:
                    template = Templates.tables['properties']
                    fn = str.format(Commands.sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(model_name)),
                                    fields=",".join(template["fields"]))
                    self.connection.cursor.execute(fn)
                    template = Templates.tables['assigned_properties']
                    fn = str.format(Commands.sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(model_name)),
                                    fields=",".join(template["fields"]))
                    self.connection.cursor.execute(fn)

                if models[model_name]['has_settings']:
                    template = Templates.tables['settings']
                    fn = str.format(Commands.sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(model_name)),
                                    fields=",".join(template["fields"]))
                    self.connection.cursor.execute(fn)
                    template = Templates.tables['assigned_settings']
                    fn = str.format(Commands.sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(model_name)),
                                    fields=",".join(template["fields"]))
                    self.connection.cursor.execute(fn)

            except NameError as error:
                print(error)
            except mysql.connector.errors.ProgrammingError as error:
                print(error.msg)

        for model_name in models:
            for relation in models[model_name]['relations']:
                try:
                    type = relation['type']
                    model = relation['model']
                    if type == "hasOne":
                        print("hasOne")
                    elif type == "belongsTo":
                        print("belongsTo")
                    elif type == "hasMany":

                        fn = str.format(Commands.sqls["table.add.fields"], table_name=str(model), fields=",".join(model_name))
                        self.connection.cursor.execute(fn)
                        print("hasMany")

                    elif type == "belongsToMany":
                        print("belongsToMany")

                except:
                    print("error")

        self.connection.close()

    def update(self, table, item_id, data):
        print("hello world")
