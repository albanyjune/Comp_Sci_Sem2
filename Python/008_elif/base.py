a = input("please enter the first number ")
x = input("please enter an operation ")
b = input("please enter the second number ")
if (x == "-"):
    c=(int(a)-int(b))
    print(str(a)+x+str(b)+"="+str(c))
elif (x == "+") :
    d=(int(a)+int(b))
    print(str(a)+x+str(b)+"="+str(d))
elif (x == "*") :
    e=(int(a)*int(b))
    print(str(a)+x+str(b)+"="+str(e))
elif (x == "/") :
    f=(int(a)/int(b))
    print(str(a)+x+str(b)+"="+str(f))
else:
    print("please enter a valid operation")
