x= int(input("how many items are you buying? "))
total = float(0)
for i in range(0,x):
    w = input("what item are you buying? ")
    z = float(input("how much is the item? "))
    print("thank you for purchasing " + w)
    print("_______________________________________")
    total = z+total
print("for "+str(x)+" items, your total is "+ str(total))
print("have a nice day!")