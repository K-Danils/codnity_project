from flask_mysqldb import MySQL
import json
from markupsafe import Markup 

# Class for Database connection and manipulation
class DB():
    def __init__(self, app):
        self.app = app
        self.mysql = MySQL(app)
        self.init_db()

    def __data_to_dict(self, data):
        # convert data from DB to dict and return it
        # initial = ((val1, val2), (val1, val2)...)
        # to = [{col1:val1, col2: val2}, {col1:val1, col2: val2}...]
        res = []
        
        for row in data:
            res.append({
                "id": row[0],
                "title": Markup(row[1]).unescape(),
                "link": Markup(row[2]).unescape(),
                "points": row[3],
                "date_created": row[4]
            })

        return res

    def init_db(self):
        # Create table in case it doesn't exist
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS articles 
                (
                    id INT NOT NULL PRIMARY KEY,
                    title TEXT NOT NULL,
                    link TEXT NOT NULL,
                    points INT,
                    date_created DATETIME NOT NULL
                );

            ''')

            # save and close
            self.mysql.connection.commit()
            cursor.close()
    
    def execute(self, command):
        # simplified execute command, so that we can do everything with single method
        # later on
        if len(command) == "":
            raise Exception("query must not be empty")
            
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute(command)

            # save and close
            self.mysql.connection.commit()
            cursor.close()

    def get_data(self):
        # select all the data from DB
        with self.app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM articles")

            # fetch the data and convert it to dict
            val = self.__data_to_dict(cursor.fetchall())

            # save and close
            self.mysql.connection.commit()
            cursor.close()

            return val
