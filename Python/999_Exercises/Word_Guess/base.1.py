import random 
myfile = open("allow_words.txt")
wordlist = []
for g in myfile:
    wordlist.append(myfile)
r = random.randrange(0,12973)
w= wordlist[r]
x=input("guess a 5 letter word!")
for i in range(0,7):
    if (x==r):
        print("congratulations! you guessed the right word!")
        print(end="")
    else:
        print("sorry! you guessed the wrong word. try again")
print(w)