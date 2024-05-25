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
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            adress VARCHAR(255) NOT NULL,
            )""")
            self.connection.commit()
            print("Created table")
        except Exception as e:
            print(e)

class User(Database):
    def create_user(self, first_name, last_name, age, email, phone, address):
        insert_user_query = '''
        INSERT INTO users (first_name, last_name, age, email, phone, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        user_data = (first_name, last_name, age, email, phone, address)
        self.cursor.execute(insert_user_query, user_data)
        self.connection.commit()

    def update_user(self, user_id, update_data):
        update_user_query = '''
        UPDATE users SET 
            first_name = %s,
            last_name = %s,
            age = %s,
            email = %s,
            phone = %s,
            address = %s
        WHERE id = %s
        '''
        updated_data = (*update_data, user_id)
        self.cursor.execute(update_user_query, updated_data)
        self.connection.commit()