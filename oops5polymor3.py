# METHOD OVERLOADING AND METHOD OVERRIDING

# method overloading => when we have 2 methods with same name but different no. of parameters
# METHOD OVERLOADING is not supported in python .. so we can use if elif else if we want to use that

class student:
    # def __init__(self,m1,m2) -> None:
    #     self.m1=m1
    #     self.m2=m2

    def sum(self,a=None,b=None,c=None,d=None): # will write 'none' else it will give error
        s=0 
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1=student()
print(s1.sum(9,8,7)) #no of para. = 3
print(s1.sum(9,8)) #no of para. = 2

# METHOD OVERRIDING => when child class also have same method as parent class
# if both have same method , child class will run its method
# if it doesnt have that same method, it will run method of parent class
# to run method of both class via child class, we can use "SUPER"

class A:
    def show(self):
        print("in show a")
class B(A):
    def show(self):
        super().show()
        print("in show b")

obj1=B()
obj1.show() 
