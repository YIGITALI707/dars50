#name=input("ism ")
#lastname=input("familiya ")
#age=input("yosh ")
#sms=f"Ism familiya:{name} \n{lastname} \nYoshi: {age}" # "\n" bitta satr pasga tushiradi
#print(sms)
# Constant
# Constantalar katta harflarda yoziladi
PI=3.14
s="123"
print(int(s)+7)
# bool()- qiymat qabul qiladi masalan a=10,a="11wmqsjx", bunda true chiqadi
# a=0,a="" bunda bool()-false deydi

#print("o" in "olma")
#z=10
#x=z
#y=z
#print(x is y)

#print(x<y and y>z)
#age=int(input("Yoshingizni kiriting "))
#a=2024
#print(a-age)
# x=int(input("son kiriting "))
# #print(x%2==0)
# if x%2==0:
#     print("juft son")
# elif x==0:
#     print("nol kiritdingiz")
# else:
#     print("toq son")

month_number=int(input("Oy raqamini kiriting:"))

if month_number>13 or month_number<0:
    print ("to'gri kiriting")
elif month_number==1:
    print ("yanvar")
elif month_number==2:
    print("fevral")
elif month_number==3:
    print("mart")
elif month_number==4:
    print("aprel")
elif month_number==5:
    print("may")
elif month_number==6:
    print("iyun")
x,y,z=15,16,17 #shunday qiymat bersa bo'ladi