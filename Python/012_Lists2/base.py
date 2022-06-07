import random 
numlist=["6", "5", "9", "8", "1", "2", "3", "4", "0"]
x = int(input("how many random numbers would you like? "))
for i in range(0,x-1):
    print(numlist[i], end=", ")
print(random.randrange(0,10))
    