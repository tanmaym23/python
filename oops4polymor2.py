# OPERATOR OVERLOADING

class student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2

    def __add__(stud1,stud2):
        marks1=stud1.m1+stud2.m1
        marks2=stud1.m2+stud2.m2
        stud3=student(marks1,marks2) #these marks 1 and marks 2 are stored in m1 and m2 of "init" method
        return stud3
    
    def __str__(self):
        # return self.m1 ,self.m2 #RETURN 1
        return '{} {}'.format(self.m1,self.m2) #this will convert touple into string


tan=student(10,10)
may=student(9,9)

tanmay=tan+may
print(tanmay.m1)
# print(tan.__str__())# "statement 1" for "RETURN 1 "we need to call "str" here aldso as the value of marks are in touple .. to avoid this CHECK "RETURN 2" AND "STATEMENT 2"
print(tan)