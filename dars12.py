# import os
# print(os.getcwd())
# file=open("fayl.txt","w") #yozish uchun
# # open("fayl1.txt","r") #o'qish uchun
# # fayl.write("salom")
# while True:
#    x=input("izoh kiriting")
#    file.write(x)
# # print(fayl)

# print(file.read()) o'qish uchun


file = open("data.txt", "a")
def last_number():
    file = open("data.txt", "r")
    users = file.readlines()
    if len(users) != 0:
        last = users[-1]
        return int( last.split('.')[0]) + 1
    return 1

print("Ro'yxatga olish boshlandi !!! ")
number = last_number()
while True:
    info = input("Ism Familyani kiriting: (or stop) ")
    if info == "stop":
        break
    file.write(f"{number}.{info}\n")
    number += 1

