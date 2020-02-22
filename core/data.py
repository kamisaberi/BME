from config.base import *
from core.globals import *


class Data:

    @staticmethod
    def retrieve_all_data(table="all"):
        Globals.models = {}
        if Base.active_connection == "mysql":
            from interface.database.rdbms.mysql.scripts.Database import Database
            db = Database('bme_db')
            datas = db.get_data(table)
            datas = Data.normalize_data(datas)
            Globals.models = datas
        elif Base.active_connection == "mongodb":
            from interface.database.rdbms.mysql.scripts.Database import Database
            print("mongodb")

    @staticmethod
    def normalize_data(datas):
        return datas
