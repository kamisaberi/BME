# from  pluralize import Translator
# import inflect
from interface.database.rdbms.mysql.scripts.Templates import *
from interface.database import *
import json
from core.data import *

Data.retrieve_all_data()
print(json.dumps(Globals.models))

# from  pattern3.text.en.inflect import pluralize,singularize
# print(pluralize("wolf"))
# a=[1,2,5,8]
# b=[12,15]
# print(a+b)
# exit(0)

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="online-service"
# )
#
# db_cursor = db.cursor()
# print(db.database)
#
# db_cursor.execute("DESCRIBE data_types")
# myresult = db_cursor.fetchall()
#
# print(myresult)
# tables = json.load(open('resources/database/middleware.json', 'r'))
# print(tables)
# templates = json.load(open('resources/templates.json', 'r'))
# sqls = json.load(open('resources/sql.json', 'r'))

# engine = inflect.engine()
# plural = engine.plural("wolf")
# print(engine.singular_noun('cats'))
#
# exit(0)
# print(templates['properties'])

# for relation in tables['relations']:
#     if 'extra_fields' in relation:
#         print("true")
#     else:
#         print("false")
# exit(0)

# install_database('bme_db')
# Templates.initialize()
# print(Templates.sqls)
#
# print(__file__)
# print(os.path.dirname(__file__))

# absolute path
# tables = json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/" + '../resources/database/Backend.py', 'r'))

