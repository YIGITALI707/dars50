# import os
# x=r"D:\data.txt"
# if os.path.exists(x):
#     print(f"{x}===> bunday fayl mavjud")
# else:
#     print(f"{x}===> bunday fayl mavjud emas")
# import json
# class FileWriter:
#     def __init__(self,fayl_nomi):
#         self.fayl_nomi=fayl_nomi
#     def Write(self,fayl_nomi):
#         file=open("yozish.txt","w")
#         file.write(self.fayl_nomi)
#         file.close()
#         return file
#     def Read(self):
#         file1=open("yozish.txt","r")
#         file1.read()
#         return file1
# class JsonSave(FileWriter):
#     def save(self):
#         with open("imtihon.json","w") as f:
#             json.dump(f,indent=4)
# x=JsonSave(fayl_nomi="aa")
# print(x.save())

# from abc import ABC,abstractmethod
# class Avto:
#     @abstractmethod
#     def run(self):
#         print("mashina yuryapti")
#     def stop(self):
#         print("mashina toxtadi")
#
# class Honda(Avto):
#     def __init__(self):
#         print("Honda")
# class Tayota(Avto):
#     def __init__(self):
#         print("Toyota")
# class Chevrolet(Avto):
#     def __init__(self):
#         print("Chevrolet")
#
# x=Honda()
# print(x.run())

class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
x=User()








