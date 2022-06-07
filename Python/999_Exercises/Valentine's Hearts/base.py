import datetime
import random
peoplelist=[]
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        peoplelist.append(l)
        person=random.randrange(12)
p=peoplelist[person]
complist=[]
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        complist.append(l)
        compliment=random.randrange(9) 
c=complist[compliment]
print(p+" "+c)