from war import Warrior

class Hero(Warrior):
    def __init__(self,name,int):
        self.name = name
        self.healt = 100
        self.damage=int
