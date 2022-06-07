import random
olivegarden=["pasta", "salad", "soup"]
mcd=["nuggets", "fries", "cone"]
mex=["taco", "quesadilla", "churro"]

x=input("please pick a restaurant out of olive garden, mcdonalds, or del taco  ")
r=random.randrange(2)
if (x=="olive garden"):
    print(olivegarden)
    print("a suggested item would be "+ olivegarden[r])
elif(x=="mcdonalds"):
    print(mcd)
    print("a suggested item would be "+mcd[r])
elif(x=="del taco"):
    print(mex)
    print("a suggested item would be "+ mex[r])