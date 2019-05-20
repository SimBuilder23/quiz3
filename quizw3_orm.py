#!/usr/bin/env python3

import csv
import sqlite3

class Database:
    def __init__ (self, database_pathname):
        self.connection = sqlite3.connect(database_pathname, check_same_thread=False)
        self.cursor     = self.connection.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, type_, value, traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit()
                self.cursor.close()
            self.connection.close()

    def create_table(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        self.cursor.execute(
            """CREATE TABLE {table_name}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(table_name = table_name))

    def add_column(self, table_name, column_name, column_type):
        self.cursor.execute(
            """ALTER TABLE {table_name}
                ADD COLUMN {column_name} {column_type}
                ;""".format(table_name = table_name, column_name = column_name, column_type = column_type))



if __name__ == "__main__":
    with Database("citi.db") as db:
        info = {"table_name" : "citi",
                "column_names" : [
                    {"column_name" : "Date", "column_type" : "VARCHAR"},
                    {"column_name" : "Open", "column_type" : "FLOAT"},
                    {"column_name" : "High", "column_type" : "FLOAT"},
                    {"column_name" : "Low", "column_type" : "FLOAT"},
                    {"column_name" : "Close", "column_type" : "FLOAT"},
                    {"column_name" : "Adj_Close", "column_type" : "FLOAT"},
                    {"column_name" : "Volume", "column_type" : "INTEGER"}]}


        db.create_table(info["table_name"])
        for column_name in info["column_names"]:
            db.add_column(
                info["table_name"],
                column_name["column_name"],
                column_name["column_type"])

