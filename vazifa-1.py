from datetime import datetime
class Bugun:
    def __init__(self,datetime):
       self.datetime=datetime
    def day(self):
        return self.datetime.now().day
    def month(self):
        return self.datetime.now().month
    def year(self):
        return self.datetime.now().year
a=Bugun(datetime)
print(a.day())




