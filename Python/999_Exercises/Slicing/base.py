x=input("enter your first and last name: ")

for i in range (len(x)):
    print(x[i])
for i in range(len(x)):
    if(x[i] ==" "):
        print(x[i+1:len(x)]+", "+x[0:i])