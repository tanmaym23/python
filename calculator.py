import string

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

def calculator():
    cont=True
    while cont:
        num1=float(input("enter first no."))
        for symbols in operations:
            print(symbols)
        op_symbol=input("enter the operation")
        num2=float(input("enter 2nd number"))
        calc_func=(operations[op_symbol])
        answer=calc_func(num1,num2)
    
        print(num1 , op_symbol , num2 , " = " , answer)
    
        if input("type yes or no")== "yes":
            num1=calc_func
        else:
            cont=False
        
        if input("do u cont using calc y or n")== "y":
            calculator()
        else:
            return

calculator()


