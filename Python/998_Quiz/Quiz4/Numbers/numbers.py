mynumbers=[6,9,32,28,15,22,3,18]
minimum=mynumbers[0]
for i in mynumbers:
    if i<minimum:
        minimum=i
print("minimum: "+ str(minimum))

maximum=mynumbers[0]
for i in mynumbers:
    if i>maximum:
        maximum=i
print("maximum: "+str(maximum))

avg=0
amount=0
for i in mynumbers:
    avg=avg+i
    amount=amount+1
avg=avg/amount
print("average: "+str(avg))