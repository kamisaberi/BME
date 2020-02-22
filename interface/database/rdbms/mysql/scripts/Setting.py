import mysql.connector
import json
import inflect


class Setting:
    id = 0
    table = ''
    data = []

    def __init__(self, table, id):
        self.id = id
        self.table = table

    def insert(self):
        print("Insert Item")

    def update(self):
        print("Update Item")

    def delete(self):
        print("Update Item")
