import random

words=["sdfghj","ertyudftyi","xcvbngm"]

rand_word=random.choice(words)
print(rand_word)

user_input=(input("enter a letter ")).lower()

blanks=[]
for _ in range(len(rand_word)):
    blanks += "_"
print(blanks)

for position in range(len(rand_word)):
    letter=rand_word[position]
    if letter==user_input:
        blanks[position]=letter
print(blanks)

