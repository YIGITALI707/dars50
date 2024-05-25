# def chek_title(func):
#     def wrapper(*args,**kwargs):
#         if 10==10:
#             result=func(*args,**kwargs)
#             if len(result)>3:
#                 return result
#             else:
#                 return None
#         else:
#             return None

# numbers=[1,3,6,19]
# def find_max_difference(numbers):
#     if not numbers:
#         return None
#
#     max_difference = 0
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             difference = abs(numbers[i] - numbers[j])
#             if difference > max_difference:
#                 max_difference = difference
#
#     return max_difference
# numbers=[1,3,6,19]
# print(find_max_difference(numbers))

# def eng_katta_farqni_topish(a):
#     b = []
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             farq=a[j]-a[i]
#             b.append(farq)
#     return max(b)
# a=[13,19,25,39,42,49]
# print(eng_katta_farqni_topish(a))

# import random
#
# def matematik_savol(func):
#     def tekshirish(*args,**kwargs):
#         a=random.randint(1,5)
#         b=random.randint(1,5)
#         c=random.randint(1,5)
#         d=random.choice(["*","-","+"])
#         savol=f"{a} {d} {c} {d} {b} {d} {c}"
#         javob=int(input(f"javob yozing {savol}="))
#         togri_javob=eval(savol)
#         if javob==togri_javob:
#             x=func(*args,**kwargs)
#             return x
#         else:
#             print("noto'g'ri")
#     return tekshirish
# @matematik_savol
# def top():
#     print("ok")
# top()


# def teskari(x):
#     a = x[12:17:]
#     b = x[6:11:]
#     c=x[0:5:]
#     teskari_gap=f"{a} {b} {c}"
#     return teskari_gap
# x="salom senga baxor"
# print(teskari(x))

b=[]
sonlar=(1,45,16,24,64,19)
for i in range(len(sonlar)):
    for j in range(i+1,len(sonlar)):
       farq=abs(sonlar[i]-sonlar[j])
       print(sonlar[i],sonlar[j])




