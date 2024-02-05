class grandparent:
    def __init__(self,name) -> None:
        self.parentname=name

    def func(self):
        print("i am patrent")

class parent(grandparent):
    def __init__(self, name,parent_name) -> None:
        # super().__init__(name)
        self.name=name
        # self.parentname=parent_name

        parent.__init__(self,parent_name)

    def other_func(self):
        print("i m child")

class child(parent):
    def __init__(self,name,parent_name,grandparent_name):
        self.name=name
        # self.parentname=parent_name

        parent.__init__(self,parent_name,grandparent_name)

    def other_func(self):
        print("i m child")

gp=grandparent("haha")
p=parent("meetu","hihi")
c=child("tanmay","meetu","hehe")

# c.func()
# c.other_func()
# print(c.name)
print(c.parentname)