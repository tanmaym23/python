def myfunc(multiple):
    return lambda n: multiple*n

n=10

doubler=myfunc(2)
tripler=myfunc(3)

print(doubler(n))