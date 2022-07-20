import os

fileLocation = "C:\\Users\\Yanek\\Dropbox\\Programming\\Python\\Codes\\Python-Tasks\\Lessons\\DuringLessons\\JSONS\\"
# fileLocation = os.getcwd()
print(fileLocation)
import json
mydict = {
    'firstname':'Yanek',
    'lastname':'Hayrapetyan',
    'age':20,
    'cities':["Nor Hachn","Yerevan","Abovyan","Rostov on Don","Nojniy Novgorod"]
}

mydict1 = {
    'firstname':'asd',
    'lastname':'Hayrapetyan',
    'age':20,
    'cities':["Nor Hachn","Yerevan","Abovyan","Rostov on Don","Nojniy Novgorod"]
}

with open(fileLocation + 'new.json') as x:
    mylist = json.load(x)

mylist.append(mydict)

with open(fileLocation + 'new.json','w') as file:
    json.dump(mylist,file)

with open(fileLocation + 'new.json') as x:
    res = json.load(x)

print(res)
