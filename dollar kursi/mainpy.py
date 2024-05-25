import json
import requests
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
r=requests.get(url)
data=r.json()
# print(data)
class Jsonsave:
    def save(self):
        file=open("19-dar.json","w")
        json.dump(self.data,file,indent=4)
        file.close()


class Request(Jsonsave):
    def __init__(self,url):
        self.url=url
        self.data=[]
    def run(self):
        r = requests.get(self.url)
        data = r.json()
        self.data=data
        return data

r=Request(url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
data=r.run()
print(data)
r.save
