import psycopg2

class Database(object):
    def __init__(self, database,user,password,host='localhost',port=5432):
        try:
            self.connection = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.database = database
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.cursor = self.connection.cursor()
        except ConnectionError as e:
            print(e)

    def create_users_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS userss(
            id SERIAL PRIMARY KEY,
            body VARCHAR(255) NOT NULL,
            postId INTEGER NOT NULL,
            user VARCHAR(255) NOT NULL,
            )""")
            self.connection.commit()
            print("Created table")
        except Exception as e:
            print(e)

    def add_user(self,userss ):
        for i in userss:
            body= i['body']
            postId = i['postId ']
            user = i['user']
            data = (body, postId, user)
            print( data )
            self.cursor.execute(""" INSERT INTO userss (body, postId, user)
                                VALUES(%s,%s,%s) """, data )
            self.connection.commit()

db = Database(database='postgres',user='postgres',password='soliyev1998')
db.create_users_table()