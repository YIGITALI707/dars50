#1-masala
#1.	PostgreSql da Online_shop nomli baza oching .Python yordamida
# Online_shop nomli bazaga ulanuvchi Database nomli class yozing

# import psycopg2
# class Database():
#     def __init__(self,host,port,password,user,datebase):
#         self.connection=psycopg2.connect(
#             host=host,
#             port=port,
#             password=password,
#             user=user,
#             datebase=datebase
#         )
#         self.cursor=self.connection.cursor()
#
# db=Database(host='localhost',port=5432,password='soliyev1998',user='Yigitali',datebase='Online_shop')




#3-masala
#Database  class ichiga create_tables nomli classmethod yozing ushbu method
# bazaga quyidagi sxema bo’yicha jadvallarni ochsin

# import psycopg2
# class Database():
#     def __init__(self,host,port,password,user,datebase):
#         self.connection=psycopg2.connect(
#             host=host,
#             port=port,
#             password=password,
#             user=user,
#             datebase=datebase
#         )
#         self.cursor=self.connection.cursor()
#
#     def create_tables(self):
#         create_table_query='''
#         CREATE TABLE users IF NOT EXISTS(
#         id integer,
#         name character,
#         reg_date date
#         )
#         '''
#         self.cursor.execute(create_table_query)
#         self.connection.commit()
#
#         create_table2_query = '''
#         CREATE TABLE category IF NOT EXISTS(
#         id integer,
#         name character,
#         products_count integer
#         )
#         '''
#         self.cursor.execute(create_table2_query)
#         self.connection.commit()
#
#         create_table3_query = '''
#                 CREATE TABLE products IF NOT EXISTS(
#                 id integer,
#                 title character,
#                 qrt integer,
#                 price integer,
#                 color character,
#                 category integer
#                 )
#                 '''
#         self.cursor.execute(create_table3_query)
#         self.connection.commit()
#
#         create_table4_query = '''
#                 CREATE TABLE comment IF NOT EXISTS(
#                 id integer,
#                 product_id integer,
#                 reg_date date,
#                 text character,
#                 user_id integer
#                 )
#                 '''
#         self.cursor.execute(create_table4_query)
#         self.connection.commit()
#
#         create_table5_query = '''
#                 CREATE TABLE cart IF NOT EXISTS(
#                 id integer,
#                 user_id integer,
#                 total_summa integer,
#                 add_date date
#                 )
#                 '''
#         self.cursor.execute(create_table5_query)
#         self.connection.commit()
#
#         create_table6_query='''
#                 CREATE TABLE cart_detail IF NOT EXISTS(
#                 id integer,
#                 product_id integer,
#                 qty integer,
#                 total_summa integer,
#                 cart_id integer,
#                 add_date date
#                 )
#                 '''
#           self.cursor.execute(create_table6_query)
#           self.connection.commit()
#
# db=Database(host='localhost',port=5432,password='soliyev1998',user='Yigitali',datebase='Online_shop')
# db.create_tables()

#6-masala
# Id si 1 ga teng bo’lgan category ga bog’langan
# barcha productlarni bazadan oluvchi
# so’rov yozing.(Barcha so’rovlar Database classi
# ichidagi sql methodi yordamida amalga oshirilsin)

# import psycopg2
# class Database():
#     def __init__(self,host,port,password,user,datebase):
#         self.connection=psycopg2.connect(
#             host=host,
#             port=port,
#             password=password,
#             user=user,
#             datebase=datebase
#         )
#         self.cursor=self.connection.cursor()
#
#     def sql(self):
#         select_query='''
#         select category from products where id=1
#         '''
#         self.cursor.execute(select_query)
#         self.connection.commit()
#
# db=Database(host='localhost',port=5432,password='soliyev1998',user='Yigitali',datebase='Online_shop')
# db.sql()


#7-masala
#7.users id ga bog’langan barcha commentlar va user
# ma’lumotlarni birlashtiruvchi so’rov namunasini yozing
# (JOIN)  users(name)
#comment(product_id,reg_date,text).  (Barcha so’rovlar
# Database classi ichidagi sql methodi yordamida amalga oshirilsin)

     # def sql(self):
     #     join_query='''
     #     select users.name,comment.product_id,
     #     comment.reg_date,comment.text
     #     from users
     #     join comment
     #     '''
     #     self.cursor.execute(join_query)
     #     self.connection.commit()
# db.sql()

#8-masala
#. Products jadvalidagi barcha soni 5 tadan kam
# qolgan tovarlarni sonini 10 ga tenglab qo’yuvchi
# so’rov yozing . (Barcha so’rovlar Database classi
# ichidagi sql methodi yordamida amalga oshirilsin)

#         def sql(self):
#             update_query='''
#             UPDATE products
#             SET qty=10
#             where qty=5
#             '''
#             self.cursor.execute(update_query)
#             self.connection.commit()
#
# db.sql()


#10-masala
#cart jadvalidagi add_date qo’shilgan sanasi
# 10 kundan oshgan ma’lumotlarni o’chiruvchi
# so’rov yozing (Barcha so’rovlar Database classi
# ichidagi sql methodi yordamida amalga oshirilsin)


#           def sql(self):
#               delete_query='''
#               delete from cart_detail
#               where add_date>10
#               '''
#               self.cursor.execute(delete_query)
#               self.connection.commit()
# db.sql()



















