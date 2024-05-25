import psycopg2
class Datebases():
    def __init__(self,database,user,password,host='localhost',port=5432):
        try:
            self.connection=psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.database=database
            self.user=user
            self.password=password
            self.host=host
            self.port=port
            self.cursor=self.connection.cursor()
        except ConnectionError as e:
          print(e)



    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
            id SERIAL PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            rating NUMERIC(5,3) NOT NULL,
            description VARCHAR(250) NOT NULL,
            price INTEGER NOT NULL
            )""")
            self.connection.commit()
        except Exception as e:
            print(e)

db=Datebases(database='fn19',user='Yigitali',password='yigitali1998')
db.create_table()
