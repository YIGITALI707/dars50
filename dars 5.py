# s="page olma page"
# print(s.replace(" ","",isalpha()))
# import datetime
# def today():
#     """Bugungi sanani qaytaruvchi funksiya"""
#     t=datetime.date.today()
#     print(t)
#
# today()

# def to_upper():
#     """salom"""
#     x=input("ism kiriting")
#     print(x.upper())
#     return x
# print(to_upper.__doc__)
# to_upper()

# def to_upper(value):
#     """salom"""
#     return value.upper()
# surname=input("familiya kirit")
# res=to_upper(surname)
# print(res)
def palindrom(a):
    if type(a)==str:
        return a[::-1]
    return False

r=palindrom("banan")
palindrom(r)




