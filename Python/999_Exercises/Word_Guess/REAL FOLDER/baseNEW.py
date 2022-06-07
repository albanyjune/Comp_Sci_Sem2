import random 
word_list=[]
with open('allow_words.txt') as f:
    for line in f:
        l=line.strip()
        word_list.append(l)

num = random.randrange(12972)
answer=word_list[num]
print(answer)