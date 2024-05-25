# class Animal:
#     def sleep(self):
#         print(self.__class__)
#         print("Animal is sleeping")

# class Rabbit(Animal):  
#     def sleep(self):
#         print(self.__class__.__mro__)
#         super().sleep()
#         print("Rabbit is sleeping") 

# rabbit = Rabbit()
# rabbit.sleep()  

# from abc import ABC,abstractmethod  

# class Electronics(ABC):
#     @abstractmethod
#     def on():
#         pass  
#     @abstractmethod
#     def off():
#         pass  

# class Tefal(Electronics):
#     def __init__(self, brend):
#         self.brend = brend
#         self.__state = "off"

#     def on(self):
#         if self.__state == "on":
#             print("Tefal is already on")
#         else:
#             self.__state = "on"        
#             print("Tefal is on")    

#     def off(self):
#         if self.__state == "off":
#             print("Tefal is already off")
#         else:
#             self.__state = "off"        
#             print("Tefal is off")  
        

# class Iron(Electronics):
      
#     def on():
#         pass  
    
#     def off():
#         pass  


# i = Iron()
# # t = Tefal(brend="Tefal")
# # t.on()
# # t.on()
# # t.off()

# import turtle


# class Square:
#     def __init__(self, a):
#         assert type(a) in (float, int) and a > 0," Invalid value for square "
#         self.a = a
    
#     def show(self):
#         turtle.forward(self.a)
#         turtle.left(90)
#         turtle.forward(self.a)
#         turtle.left(90)
#         turtle.forward(self.a)
#         turtle.left(90)
#         turtle.forward(self.a)
#         turtle.left(90)
#         turtle.exitonclick()

# s = Square(a=80)
# # s.show()

# class Circle():
#     def __init__(self, r):
#         assert type(r) in (float, int) and r > 0," Invalid value for circle "
#         self.r = r

#     def show(self):
#         turtle.circle(self.r)

# c = Circle(90)
# c.show()     