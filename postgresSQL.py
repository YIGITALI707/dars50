import psycopg2

class Datebase():
    def __init__(self,port,host,password,user,datebase):
        self.connection=psycopg2.connect(
            port=port,
            host=host,
            password=password,
            datebase=datebase,
            user=user
        )
        self.cursor=self.connection.cursor()

    def create_user_table(self):
        create_table_query='''
        create table users (
        id serial primary key,
      
        )
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()
        create_table_product_query='''
        
        
        '''
        self.cursor.execute(create_table_product_query)
        self.connection.commit()

class User(Datebase):
    def create_user(self,firtsname,lastname,age,email):
        insert_user_query='''
        insert into user (firstname,lastname,age,email)
        values(%s,%s,%s,%s)
        '''
        user_date=(firtsname,lastname,age,email)
        self.cursor.execute(insert_user_query,user_date)
        self.connection.commit()

        insert_product_query='''
        insert into product(djsjfhjhfadchjsdh) 
        values(gfyfjffkhkjg)
        '''
        self.cursor.execute(insert_product_query)
        self.connection.commit()
    def update_user_email(self,user_id,new_email):
        update_query='''
        update user 
        set email=
        
        '''
    def join_product_user_query(self):
        join_query='''
        select users.lastname,usersjfgjdfgj,
        '''

        def update_user_email(self, user_id, new_email):
            update_query = """
              UPDATE users
              SET email = %s
              WHERE id = %s
              """
            self.cursor.execute(update_query, (new_email, user_id))
            self.connection.commit()

        def join_users_and_products(self):
            join_query = """
              SELECT users.first_name, users.last_name, users.email, products.name, products.price
              FROM users
              CROSS JOIN products
              """
            self.cursor.execute(join_query)
            rows = self.cursor.fetchall()
            return row

import psycopg2

class Database:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100)
        )
        """
        self.cursor.execute(create_users_table_query)
        self.connection.commit()

        create_products_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            price DECIMAL(10, 2)
        )
        """
        self.cursor.execute(create_products_table_query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def insert_user(self, first_name, last_name, email):
        insert_query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(insert_query, (first_name, last_name, email))
        self.connection.commit()

    def insert_product(self, name, price):
        insert_query = """
        INSERT INTO products (name, price)
        VALUES (%s, %s)
        """
        self.cursor.execute(insert_query, (name, price))
        self.connection.commit()

    def update_user_email(self, user_id, new_email):
        update_query = """
        UPDATE users
        SET email = %s
        WHERE id = %s
        """
        self.cursor.execute(update_query, (new_email, user_id))
        self.connection.commit()

    def join_users_and_products(self):
        join_query = """
        SELECT users.first_name, users.last_name, users.email, products.name, products.price
        FROM users
        CROSS JOIN products
        """
        self.cursor.execute(join_query)
        rows = self.cursor.fetchall()
        return rows

# Bazaga bog'lanish
db = Database(host="localhost", database="my_database", user="my_user", password="my_password")

# Jadvallarni yaratish
db.create_tables()

# Foydalanuvchilarni qo'shish
db.insert_user("John", "Doe", "john@example.com")
db.insert_user("Jane", "Doe", "jane@example.com")

# Mahsulotlarni qo'shish
db.insert_product("Laptop", 1500.00)
db.insert_product("Smartphone", 800.00)

# Foydalanuvchi email manzilini yangilash
db.update_user_email(1, "new_email@example.com")

# Bog'lanish so'rovi
joined_data = db.join_users_and_products()

# Natijalarni chiqarish
for row in joined_data:
    print(row)

# Bog'lanishni yopish
db.close_connection(