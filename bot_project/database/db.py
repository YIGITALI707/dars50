import os
import psycopg2
from dotenv import load_dotenv
from .table import *

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DBNAME = os.getenv('DBNAME')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

class Database:
    def __init__(self):
        self.connect = psycopg2.connect(
            dbname=DBNAME,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        self.cursor = self.connect.cursor()
        create_user_table(self.cursor, self.connect)
    def users_exists(self,tg_id):
        """Check if a user exists in the database"""
        query = """SELECT * FROM tgusers WHERE tgid=%s"""
        self.cursor.execute(query,(tg_id,))
        result = self.cursor.fetchone()
        if result is None:
            return False
        return True
    def add_user(self, tg_id,username,first_name=None,last_name=None):
        """Add a new user to the database"""
        query = """INSERT INTO tgusers (tgid,username,firstname,lastname) 
        VALUES (%s,%s,%s,%s)"""
        self.cursor.execute(query,(tg_id,username,first_name,last_name))
        self.connect.commit()

