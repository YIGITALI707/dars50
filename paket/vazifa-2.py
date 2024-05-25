# file=open("parol.txt")
# # print(file.read())
# urin_soni=0
# while urin_soni<3:
#     urin_soni += 1
#     parol=input("parolni kiriting:")
#     if parol==file.read():
#         print(f"muvaffaqqiyatli parol {urin_soni} ta urinishda topildi")
#     else:
#         print(f"qayta urining.")

urin_soni=0
file=open(f"parollar.txt","w")
# file.write("1998soliyev")
while urin_soni<3:
