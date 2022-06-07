length = input("please enter line length ")
direct = input("vertical or horizontal? ")
y = "*"
if (direct == "vertical"):
    for x in range(0,int(length)):
        print(y)
elif (direct == "horizontal"):
    for x in range(0, int(length)):
        print(y, end=" ")
