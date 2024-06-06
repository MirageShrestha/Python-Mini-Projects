import random
cl=input("Enter Code Language")
words=cl.split(" ")
coding=input("1 for coding and 0 for decoding")
coding=True if coding=="1" else False
if coding:
    newWords=[]
    for word in words:
        if len(word)>=3:
            r=['a','b','c','d','e','i','o','u']
            r1=random.choice(r)
            r2=random.choice(r)
            clNew=r1+word[1:]+word[0]+r2
            newWords.append(clNew)
        else:
            newWords.append(word[::-1])
    print(" ".join(newWords))
else:
    pass