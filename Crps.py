import random
you=int(input("what do you choose? 0 for rock, 1 for paper , 2 for scissors: "))
if you==0:
    print("rock")
elif you==1:
    print("paper")
else:
    print("scissors")

print("comp choose")
comp=random.randint(0,2)
if comp==0:
    print("rock")
elif comp==1:
    print("paper")
elif comp==2:
    print("scissors")

if (you==comp):
    print("tie")
elif (you==0 and comp==1):
    print("comp wins")
elif(you==0 and comp==2):
    print("you win")
elif(you==1 and comp==0):
    print("you win")
elif(you==1 and comp==2):
    print("comp win")
elif(you==2 and comp==0):
    print("comp win")
elif(you==2 and comp==1):
    print("you win")



