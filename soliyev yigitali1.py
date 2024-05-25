#1-masala
# Oy  tartib raqami inputdan kiritiladi.Masalan ( 1 , 2 ... 7)
# Kiritilgan oy tartib raqamga qarab oy nomi nomini ekranga chiqaruvchi match/case yozing
# x=int(input("son kiriting:"))
# if x==1:
#     print("yanvar")
# if x==2:
#     print("fevral")
# if x==3:
#     print("mart")
# if x==4:
#     print("aprel")
# if x==5:
#     print("may")
# if x==6:
#     print("iyun")
# if x==7:
#     print("iyul")
# if x==8:
#     print("avgust")
# if x==9:
#     print("sentabr")
# if x==10:
#     print("oktabr")
# if x==11:
#     print("noyabr")
# if x==12:
#     print("dekabr")


#2-masala
#N dan 1 sonigacha bo'lgan juft sonlarni ekranga chiqaruvchi for loop yozing
#N inputdan qabul qilinadi (N > 10 , N < 100000)
# x=int(input("son kiriting:"))
# for i in range(x):
#     if i%2==0:
#         print(i)

#3-masala
#N dan 1 sonigacha bo'lgan toq sonlarni ekranga chiqaruvchi while loop yozing
# N inputdan qabul qilinadi (N > 10 , N < 100000)
# x=int(input("son kiriting:"))
# for i in range(x):
#     if i%2==1:
#         print(i)

#4-masala
# s = "Python iS tHe bEst ProgramMing lanGuaGe"  #for loop yordamida satr ichidagi katta harflar sonini hisoblang
# import string
# x=string.ascii_uppercase
# for i in s:
#     # print(i)
#     if i==string.ascii_uppercase:
#         print(s.count(x))
# #5-masala
# s = "Python is the best programming language"  #for loop yordamida satr ichidagi  probellar  sonini hisoblang
# x=" "
# for i in s:
#     if i==x:
#      print(s.count(" "))


#6-masala
# numbers = [8,9,7,5,6,4,2,1,3]  #ushbu list ichidan o’rta qiymatni toping
# print(sum(numbers)/9)

#13 Dictonary berilgan ushbu dict ichidagi barcha qiymatlarni  darajaga ko’taruvchi dastur tuzing
# a = {'number_1':1 , 'number_2':2,'number_3':3,'number_4':4 }
# for i in a.values():
#     print(i)
#8-masala
# word = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione reiciendis aliquid qui!"
# #Berilgan Satr ichidagi harflar sonini sanab qaytaruvchi word_count nomli funksiya yozing  (Probel va simvollar hisobga olinmasin)
# for i in word:
#     if i.isalpha():
#         print(word.count(i))

# # 9-masala
r = []  #ushbu list ichini 10 tasodifiy  harf bilan to'ldiring . for va while dan foydalanilmasin
import random
import string
r=[random.choice(string.ascii_uppercase) for _ in range(1,10)]
print(r)

#14-masala
#Dictonary berilgan ushbu dict ichidagi barcha kalitlarni alohida listga  qiymatlarni esa boshqa listga
#joylovchi dastur tuzing
# a = {'number_1':1 , 'number_2':2,'number_3':3,'number_4':4 }
# b=list(a.keys())
# x=list(a.values())
# print(x,b)


#15-masala
# List berilgan ushbu list ichidagi takroran kelgan elementlarni boshqa listga
# joylovchi dastur tuzing. Set ma'lumot turidan foydalanilsin
# a = ['a','b','a','c','f','d','c','r','y','f']
# b=[]
# for i in a:
#     b.append(i)
# print(b)
# print(set(b))



