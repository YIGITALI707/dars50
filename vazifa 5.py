class Tekshirish:
    def __init__(self,x):
        self.x=x
    def sonlar(self):
        if len(self.x)!=len(set(self.x)):
            print("true")
        else:
            print("false")
javob=Tekshirish(x=[1,2,3,4,1])

print(javob.sonlar())