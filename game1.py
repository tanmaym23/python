#rock paper scissor
import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=="r":
        if you=="s":
            return False
        elif you=="p":
            return True
    elif comp=="p":
        if you=="r":
            return False
        elif you=="s":
            return True
    elif comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True

print("comp turn:rock(r),paper(p), scissor(s)")
randno=random.randint(1,3)
if randno==1:
    comp = ("r")
elif randno==2:
    comp = ("p")
elif randno==3:
    comp = "s"

you = input("your turn:rock(r),paper(p), scissor(s)")
a=game(comp,you)

print ( f"comp choose {comp}")
print ( f"you choose {you}" )

if a==None:
    print("its a tie")
elif a :
    print("you loose")
else :
    print("you win")
