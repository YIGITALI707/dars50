import json

import requests
URL = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"

#
# def get():
#     r = requests.get(URL)
#     data = r.json()
#     return data[:3]

def save():
    r = requests.get(URL)
    data=r.json()
    with open("kurs.json","a") as file:
        json.dump(data,file,indent=4)
        return data[:3]
save()

