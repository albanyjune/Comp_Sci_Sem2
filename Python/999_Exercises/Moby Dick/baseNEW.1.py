sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
for i in range(len(sentence)):
    if (sentence[i]=="w"):
        sentence[i]
        if (sentence[i+5]=="s"):
            print(sentence[i:i+6])
#below is where it doesn't work anymore
x='s'            
y=0
with open('moby.txt') as f:
    for line in f:
       l = line.strip()
       for i in range(len(l)):
            if (l[i]=="w"):
                l[i]
                if (l[i+5]==x):
                    y=y+1
                break 
print("there are "+str(y)+ "whales in Moby Dick")
f.close()
