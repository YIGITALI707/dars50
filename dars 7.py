# #[]-list bu tartibli to'plam
# l=[1,2]
# l.extend("soya") #ichiga har birini list qilib joylaydi
# print(l)
# l.insert(1,"azim")# indexni bersangiz va nima qoshishni bersangiz shunga qoshadi
# print(l)
# l.remove(1)# list ichidagi qaysi malumotni ochirishni korsatish
# print(l)

# l=list(range(1,100))
# print(l)
# l.reverse() #teskari qilib beradi
# print(l)
#
# l1=[1,3,4,6,10,9,2,5,7,8]
# l2=["s","w","r","t","f","h","i","a"]
# l2.sort()# sort() tartiblab beradi sonlar va harflarni
# l1.sort()
# print(l1)
# print(l2)
# l1.sort(reverse=True) #teskari joylash uchun
# print(l1)

# l=[-1,5,6,7,5,7,9,-12]
# l2=[]
# for i in l:
#     if i<0:
#         l2.append(0)
#     else:
#         l2.append(i)
# print(l2)

# l=["as",12,"w",1,"uy",3,4,5,"e"] #list ichida almashtirsh
# for i in l:
#     if type(i)==str:
#         a=l.index(i)
#         l[a]=0
# print(l)

# l=[-1,5,6,7,5,7,9,-12]
# for obj_index,el in enumerate(l):
#     print(obj_index,el)
#     if el<0:
#         l[obj_index]=0
# print(l)

# t=("python","java") # tuple o'zgarmas,tartiblangan to'plam
# # t=tuple("python")
# # print(t)
# l2=list(t)
# print(l2)

# l=[-1,5,6,7,5,7,9,-12]
#  for obj_index,el in enumerate(l):# bitta index surilib qolishiga harflar qolyapti
#      if type(el)==str:
#          del l[obj_index]
#  print(l)
# start=True
# while start:
#     len_list=len(l)
#     for i in range(0,len_list-1):

# l=["assalom","nok","python","futbol","asad"]
# # l2=list(l)
# # print(l2)
# for i in l:
#     if i[0]=="a":
#      l2 = list(l)
#      print(l2)
# asab="wefiuerfpoeifewrufiepriu"
# # print(asab[0])
# v=asab.replace("w","kaluuuu")
# print(v)
plan="qbara kanimadaq"
# print(len(plan))
# print(plan[4:-4:2])
# print(plan.split("."))
# print(plan.find("b"))
# print(plan.count("1"))
# print(plan.split())
# print(plan[1:4:])
# print(plan.strip("q"))
# print(plan.capitalize())
# print(plan.title())
# print(plan.center(10))
# print(plan.split())
# a="deweferfrgetg"
# print(list(a))

# a = {'number_1': 1, 'number_2': 2, 'number_3': 3, 'number_4': 4}
# for x in a:
#     a[x]=False
# print(a)

list_1 = ["name","age","surname","adres"]
list_2 = ["Anvar",17,"Sobirov","Fergana"]
d = {'number_1':1,'name':"Olim","email":"Email","number_2":2,'number_3':3,'number_4':4 }
# def sumdict(d):
#     sum =0
#     for x in d.values():
#       if isinstance(x,int):
#         sum+=x
#     return sum
# print(sumdict(d))
# l=["aggahdgfsfkjsh","ehdqwiuehiuehqwhuuwi"]
# def maxword(l):
#     if len(l[0])>len(l[1]):
#         print(len(l[0]))
#     else:
#         print(len(l[1]))
# l = ["aggahdgfsfkjsh", "ehdqwiuehiuehqwhuuwi"]
# print(maxword(l))

list_1 = ["python","java","php","c++"]
def addstring(c):
    string=""
    for x in c:
        string+=x
    return string
list_1 = ["python", "java", "php", "c++"]
print(addstring(list_1))
