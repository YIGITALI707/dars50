import requests
import json

class Dummy:
    def download(self,yol):
        x=requests.get(yol)
        saqlash=x.json()
        with open("vazifa.json","a") as file:
            json.dump(saqlash,file)
        return saqlash

a=Dummy()
yol="https://dummyjson.com/users"
print(a.download(yol))




