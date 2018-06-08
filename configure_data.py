from tinydb import TinyDB, Query
import os
data_file = "data.json"
if os.path.isfile(data_file) :

	os.remove(data_file)
db = TinyDB(data_file)
User = Query()
db.purge_tables()



for item in db:
    print(item)

import yaml



fileSt = open('ex1.yaml', 'r')
y = yaml.load(fileSt) 
top_dev = y.pop('device')
print(top_dev)
print()
#print(y)
#y['device']
# print("y  [" ,type(y).__name__, "]   :", y)
#for a in y: 
#	y[a]['parent'] = 'blc00'
fin = {}
for a in y: 
	top_dev['children'] = y
print(top_dev)
# for a in y: 
# 	db.insert(y[a])
db.insert(top_dev)

#db.insert(y)
#for a in db:

# fileOut = open('ex1.json', 'w')
# for a in y:
# 	fileOut.write("".join(a))