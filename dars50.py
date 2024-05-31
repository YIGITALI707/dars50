# class Student:
#     objects=[]
#     counter=0
#     def __init__(self,f_name):
#      self.f_name=f_name
#      self.objects.append(self)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         try:
#             object=self.objects[self.counter]
#             self.counter+=1
#             return object
#         except IndexError:
#             self.counter=0
#             raise StopIteration
# Student("Hayrullo")
# Student("Muhammad")
# Student("Abdulaziz")
# Student("Yigitali")
# for student in Student("Nusratilloh"):
#     print(student)

# class MyList:
#     def __init__(self, items):
#         self.items = items
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.items):
#             item = self.items[self.index]
#             self.index += 1
#             return item
#         else:
#             raise StopIteration()
#
# my_list = MyList([1, 2, 3, 4, 5])
# for item in my_list:
#     print(item)
class uzun_ismni_topish:
    def __init__(self,ismlar):
        self.ismlar=ismlar
        self.qiymat = 0
        self.topish()

    def topish(self):
        self.uzun_ism = max(self.ismlar, key=len)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            ism = self.ismlar[self.qiymat]
            self.qiymat += 1
            return ism
        except:
            raise StopIteration()


ismlar= ["Abdulla", "Temur", "Mirjalol", "Samandar", "Otabek"]
ism_topish =uzun_ismni_topish(ismlar)
print(f"Eng uzun ism: {ism_topish.uzun_ism}")

for ism in ism_topish:
    print(ism)


