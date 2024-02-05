# ENEMURATE:
#---keep the count in the iteration while iterating over thye list.

l1=["tanmay","didi","papa"]
for i in range (3):
    print (i,"-",l1[i])

#above we used range function. better way is to use enumerte function.
# syntax -- enumerate(iterable,start)
for i in  enumerate(l1):#default it starts from 0
    print (i)

for i in  enumerate(l1,start=1):
    print (i) 

print("---------------")

# ZIP:
# --- helps in iterating over multiple lists parallely1
# can be more than 2 lists also
# can zip other data structures like ductionary etc.
l2=["mahajan","hehe","haha"]
for i in range (3):
    print(l1,"-",l2)
#above we used range function. better way is to use zip function.
for i in zip(l1,l2):
    print (i)

print("---------------")

# MAP

numbers=[1,2,3,4,5]
double_numbers=[]
for num in numbers:
    double_numbers.append(2*num)
print (double_numbers)
#above we used for loop. better way is to use map function.
def double(num):
    return 2*num
final=map(double,numbers)
list(final)
print("........")
# que: construct a list which contains the length of all elements in the list
words=["tanmay","meetu","shubhangi"]
# hint:use len and map function

print(list(map(len,words)))
