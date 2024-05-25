# import os
# path=os.getcwd()
# print(path)
#
# f=open(f"{path}\\")
import json
data={
    "name":"John",
    "age":30,
    "city":"new york"
}
f=open("data.json","w")
json.dump(data,f,indent=4)