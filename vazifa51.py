# # 1-masala
# class uzun_ismni_topish:
#     def __init__(self,ismlar):
#         self.ismlar=ismlar
#         self.qiymat = 0
#         self.topish()
#
#     def topish(self):
#         self.uzun_ism = max(self.ismlar, key=len)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             ism = self.ismlar[self.qiymat]
#             self.qiymat += 1
#             return ism
#         except:
#             raise StopIteration()
#
#
# ismlar= ["Abdulla", "Temur", "Mirjalol", "Samandar", "Otabek"]
# ism_topish =uzun_ismni_topish(ismlar)
# print(f"Eng uzun ism: {ism_topish.uzun_ism}")
#
# for ism in ism_topish:
#     print(ism)
#
#
#
#
# #2-masala
# class sonlarni_tartiblash:
#     def __init__(self, sonlar):
#         self.sonlar = sorted(sonlar)
#         self.qiymat = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             son= self.sonlar[self.qiymat]
#             self.qiymat += 1
#             return son
#         except:
#             raise StopIteration()
#
#
# tartibsiz_sonlar = [7, 6, 13, 2, 9, 3]
# tartibli_sonlar= sonlarni_tartiblash(tartibsiz_sonlar)
#
# for son in tartibli_sonlar:
#     print(son)


#3-masala
class Katta_son:
    def __init__(self, sonlar):
        self.sonlar = sonlar
        self.qiymat= 0
        self.katta_sonni_topish()


    def katta_sonni_topish(self):
        self.katta_son= max(self.sonlar)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.qiymat += 1
            return self.katta_son
        except:
            raise StopIteration()

sonlar = [5, 2, 8, 1, 9, 3]
topuvchi= Katta_son(sonlar)

for kattasi in topuvchi:
    print(f"Eng katta son: {kattasi}")
