# class Mashina:
#     def __init__(self,nomi,rangi,tezligi):
#         self.nomi=nomi
#         self.rangi=rangi
#         self.tezligi=tezligi
#     def xarakteristiaksi(self):
#      return
# x=Mashina(nomi="Gentra",rangi="qora",tezligi="200 km/soat")
# print(x.nomi)



# class Triangle:
#     def __init__(self,a,b,c):
#         assert type(a) in (int,float)
#         assert type(b) in (int, float)
#         assert type(c) in (int, float)
#         self.a=a
#         self.b=b
#         self.c=c
#     @property
#     def a(self): # getter
#         return self.__dict__["a"]
#     @a.setter
#     def a(self,value):
#         assert type(value) in (int,float)
#         self.__dict__["a"]=value
#     @a.deleter
#     def a(self):# deleter
#         raise PermissionError("ochirish mumkin emas")
#     #   del self.__dict__["a"]
#
#     def perimetr(self):
#         return self.a+self.b+self.c
# x=Triangle(6,4,6)
# print(x.a)
# del x.a
# # x.a="sakkiz"
# print(x.perimetr())

class Line:
    def __init__(self,width,height,length):
        self.width=width   #public
        self._height=height    #protect
        self.__length=length   #private

