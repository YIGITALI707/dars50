# x="ok"
# match x:
#     case "ok":
#         print("x==ok")
#     case "error":
#         print("x==error")
# password=input("parol kiriting ")
# print(len(password))
# password=input("parol kiriting")
# print(password[len(password)-1]) #yoki print(password[-1]) #indeks olish
# password=input()
# print(password[0:7]) #so'zlarni qirqib olish uchun [] tortburchak qavs indekslarni olish ya'ni char ni vazifasini beradi

# password=int(input("parol kiriting "))
# x=len(str(password))
# if x<8:
#     print("error")
# else:
#     print("togri")

# palindrom=input()
# if palindrom==palindrom[::-1]:
#     print("togri")
# else:
#     print("notogri")

# for i in "python":
#     print(i)
# for i in range(1,101):
#     if i%2==0:
#         print(i)

# for i in range(100,1,-2):
#     print(i)

def create_user_table(cursor,connect):
    """Create user table"""
    query = """CREATE TABLE IF NOT EXISTS tgusers (
        id BIGSERIAL PRIMARY KEY,
        tgid BIGINT NOT NULL DEFAULT 0,
        username VARCHAR(255),
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) ,
        ad_date DATE NOT NULL DEFAULT NOW(),
        state VARCHAR(255)
    );"""
    cursor.execute(query)
    connect.commit()






