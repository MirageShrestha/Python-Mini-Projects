import random
def check (User, Computer):
    if User == Computer:
        return 0
    if (User==1 and Computer==2):
        return -1
    if (User==2 and Computer==3):
        return -1
    if (User==3 and Computer==1):
        return -1 
    else:
        return 1

User=int(input("Choose\n 1 for Rock\n 2 for Paper\n 3 for Scissor\n"))
Computer=random.randint(1,3)

Score=check(User, Computer)
print("You: ", User)
print("Computer: ", Computer)
if (Score==0):
    print("Draw")
if (Score==-1):
    print("You Lose")
if (Score==1):
    print("You Won")