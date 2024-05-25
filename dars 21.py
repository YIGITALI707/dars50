


# from abc import ABC,abstractmethod
# class Animal:
#     @abstractmethod
#     def sleep(ABC):
#         print("animal sleep")
#     def run(self):
#         print("animal run")
# class Cat(Animal):
#     pass
# x=Cat()
# print(x.run())


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def rect_perm(self):
        return (self.width+self.height)*2

class Triangle:
    def __init__(self,a,b,s):
        self.a=a
        self.b=b
        self.s=s
    def triangle_perm(self):
        return self.a+self.b+self.s

class Square:
    def __init__(self,q):
        self.q=q
    def square_perm(self):
        return self.q*4

r=Rectangle(10,20)
r2=Rectangle(11,12)
print(r.rect_perm())
t=Triangle(1,2,3)
t1=Triangle(4,5,6)
print(t.triangle_perm())
w=Square(2)
w1=Square(3)
print(w1.square_perm())

geo=[r,r2,t,t1,w,w1]
for i in geo:
    if isinstance(i,Rectangle):
        print(i.rect_perm())
    elif isinstance(i,Triangle):
        print(i.triangle_perm())





