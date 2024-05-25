
import random

class Warrior(object):
    def attack(self,target):
        print(f"{self.name} attacking {target.name}")
        target.health-=self.damage
        print(f"{target.name} health={target.health}")
        if target.health=0:
            print(f"{target.name} is dead")

    def defence(self):
        print(f"{self.name} defence")
