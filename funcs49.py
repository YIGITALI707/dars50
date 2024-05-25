# from decor49 import chek_title
# @chek_title
# def salom_ber(ism):
#     return "assalomu alaykum"
# @chek_title
# def fio_salom_ber(ism,familiya,i_o):
#     return "assalomu alaykum"

# import string
# def clear_punctuation(func):
#     def wrapper(*args,**kwargs):
#         clear_args=[]
#         for word in args:
#             word_clear=""
#             for letter in word:
#                 if letter not in string.punctuation:
#                    word_clear+=letter
#             clear_args.append(word_clear)
#         result=func(*clear_args,**kwargs)
#         return result
#     return wrapper

# def en_katta_farqni_topish(sonlar):
#     b=[]
#     for i in range(len(sonlar)):
#         for j in range(i+1,len(sonlar)):
#             farq=abs(sonlar[i]-sonlar[j])
#             b.append(farq)
#     return max(b)
# sonlar=(1,45,16,24,64,19)
# print(en_katta_farqni_topish(sonlar))
#
# def bosqich_1(func):
#     def bosqich_2(sonlar):
#         b=[]
#         for i in range(len(sonlar)):
#             for j in range(i+1,len(sonlar)):
#                 farq=abs(sonlar[i]-sonlar[j])
#                 b.append(farq)
#                 c=max(b)
#             return func(sonlar,c)
#     return bosqich_2
#
#
#
# @bosqich_1
# def bajar(sonlar,c):
#     print(f"{sonlar}")
#     print(f"{c}")
# sonlar = (1, 45, 16, 24, 64, 19)
# bajar(sonlar)

# def birinchi(sonlar):
#     b=[]
#     for i in range(len(sonlar)):
#         for j in range(i+1,len(sonlar)):
#             farq=abs(sonlar[i]-sonlar[j])
#             b.append(farq)
#     return max(b)
# sonlar = (1, 45, 16, 24, 64, 19)
# print(birinchi(sonlar))
import random

def birinchi(func):
    def ikkinchi(*args,**kwargs):
        a=random.randint(1,4)
        b=random.randint(1,4)
        c=random.choice("*","+","-")
        misol=f"{a} {c} {b}"
        kirit=int(input(f"javob bering {misol}"))
        javob=eval(misol)
        if kirit==javob:
            x=func(*args,**kwargs)
            return x
        else:
              print("noto'g'ri")




"""
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YIGITALI707/dars50.git
git push -u origin main
"""