#!usr/bin/env python3

import csv
import sqlite3

from quizw3_orm import Database

class Stock:

    def seed(self, file_pathname):
        with Database("citi.db") as db:
            with open (file_pathname, "r") as f:
                rows = csv.reader(f)
                next (rows)
                for row in rows:
                    db.cursor.execute(
                        """INSERT INTO citi(
                            Date,
                            Open,
                            High,
                            Low,
                            Close,
                            Adj_Close,
                            Volume
                        ) VALUES (?, ?, ?, ?, ?, ?, ?);""",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                        )


if __name__ == "__main__":
    stock = Stock()
    stock.seed("C.csv")