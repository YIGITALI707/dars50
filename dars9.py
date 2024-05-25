# for x in range(0,20):
#     print("salom %s" % x)
#     if x<9:
#      break
#     s="p4kdfkj539"
#     if i in string.punctuation:
#         d.append(i)
#         print(d)
# user=dict(name="olim",surname="olimov")
# # print(user)
# user["name"]="sobir"
# print(user)
# # del user["name"]
# print(user)
# men=dict(ism="soliyev",familiya="yosh",yosh="26",pochta="soliyev.g@mail.com")
# print(men)
# income={"total_summa":0}
# fruits={"banan": {"price":25000,"kg":21},"olma":{"price":2000,"kg":25},"mandarin":{"price":30000,"kg":39},"uzum":{"price":52000,"kg":5},"limon":{"price":33000,"kg":5}}
# print("assalomu alaykum xush kelibsiz")
# while True:
#     user_choice=input("meva nomini kiriting  yoki stop deng")
#     if user_choice=="stop":
#        if income["total_summa"]>0:
#            print(f"sizdan jami {income["total_summa"]} sum boldi")
#        break
#     if user_choice.lower() in fruits:
#         print(f"bor bunday meva {user_choice} va narxi {fruits[user_choice]["price"]}")
#         kg=input("necha kg olasiz:")
#         if kg.isdigit():
#             kg = int(kg)
#             if kg<=fruits[user_choice]["kg"]:
#                 summa=kg*fruits[user_choice]["price"]
#                 income["total_summa"]+=summa
#                 fruits[user_choice]["kg"]-=kg
#             else:
#                print(f"{user_choice} dan {kg} kilo qolmagan.")
#         else:
#             print("kecha tugadi")
#     print("tushum",income["total_summa"])
# print("ombor xolati", fruits)
# def addString(lst):
#     result_string =""
#     for item in lst:
#         result_string += item
#     return result_string
#
# # Test uchun list
# list_1 = ["python", "java", "php", "c++"]
# print("Natija:", addString(list_1))

d2=dict().fromkeys(["a","b","c"],0) # fromkeys kalitlardan dict yasash
#d.get("key3") kalit qiymatini olish,kalit bo'lmasa none qaytaradi
#print(d.get("key5","kalit yo'q"))
#
#d.items() kalit va qiymatlarni beradi
#for key,val in d.items():

#print(list(d.keys())) kalitlarni listga aylantirish
#print(list(d.values())) qiymatlarni listga aylantirish

#r=d.pop("key") kalit bersa o'chiradi
#=d.popitem() bittasini o'chirib tashlaydi  va qiymatini qaytaradi
#r=d.setdefault("key55",15) kalit bor bo'lsa olib beradi kalit yo'q bo'lsa dict ichiga shuni ochib qiymat o'rnatadi

#bo'sh dictni qiymatlar bilan to'ldirish
#1-usul
# alpha={}
# import string
# print(string.ascii_uppercase)
# c=1
# for i in string.ascii_uppercase :
#     alpha[i]=c
#     c+=1
# print(alpha)
#2-usul
# for index,letter in enumerate(string.ascii_uppercase):
# alpha[letter]=index+1
# print(alpha)

# words="python java php go php c++ java python javascript".split()
# print(words)
# # result={"python":3}
# #
# import random
# # d=list(range(1,100))
# # print(d)
# d=[]
# for i in range(1,10):
#     x=random.randint(1,100)
#     if x in d:
#         d.append(x)
#     print(x)

d={
    "users":[
        {"name":"sobir","score":10},
        {"name":"asror","score":56},
        {"name":"aziz","score":45},
        {"name":"asad","score":53}
    ]}

succes=[]
fail=[]

for i in d["users"]:
    if i["score"]>50:
        succes.append(i)
        print("succes=",succes)
    else:
        fail.append(i)
        print("fail=",fail)




    

