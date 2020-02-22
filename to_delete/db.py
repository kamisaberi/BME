import mysql.connector
import json
import inflect


def open_database(db_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=db_name
    )
    return mydb


def install_database(db_name):

    db = open_database(db_name)
    db_cursor = db.cursor()

    tables = json.load(open('../resources/database/Backend.py', 'r'))
    templates = json.load(open('../resources/templates/templates.json', 'r'))
    sqls = json.load(open('../resources/templates/sql.json', 'r'))

    engine = inflect.engine()
    for table in tables["tables"]:
        fn = str.format(sqls["table.create"], table_name=str(table["title"]), fields=",".join(table["fields"]))
        db_cursor.execute(fn)

        if table['has_property_table'] == True:
            template = templates['properties']
            fn = str.format(sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(table["title"])), fields=",".join(template["fields"]))
            db_cursor.execute(fn)
            template = templates['assigned_properties']
            fn = str.format(sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(table["title"])), fields=",".join(template["fields"]))
            db_cursor.execute(fn)

        if table['has_setting_table'] == True:
            template = templates['settings']
            fn = str.format(sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(table["title"])), fields=",".join(template["fields"]))
            db_cursor.execute(fn)
            template = templates['assigned_settings']
            fn = str.format(sqls["table.create"], table_name=str.format(template["title"], engine.singular_noun(table["title"])), fields=",".join(template["fields"]))
            db_cursor.execute(fn)

    for relation in tables['relations']:
        tbls = relation['tables']
        template = templates[relation['template']]
        table_name = str.format(template['title'], tbls)

        fields = template['fields'].copy()

        for i, s in enumerate(fields):
            fields[i] = str.format(fields[i], tbls)

        if 'extra_fields' in relation:
            fields = fields + relation['extra_fields']
        # fields = str.format(template['fields'], tbls)

        fn = str.format(sqls["table.create"], table_name=table_name, fields=",".join(fields))
        db_cursor.execute(fn)

    db.close()
