sym=input("what symbol would you like to use? ")
width=int(input("what's the width of your box? "))
length=int(input("what's the length of your box? "))

for x in range(length):
    print("")
    for x in range(width):
        print(sym, end="")