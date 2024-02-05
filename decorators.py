def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(funct):
    # storing the function in a variable
    greeting = funct("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)

# details='tanmay mahajan 23 2003'
# first,last,dob,yr=details.split(' ')
# print(first)
# print(last)
 