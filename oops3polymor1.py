# Duck Typing

class VScode:
    def execute(self):
        print("compilke")
        print("run")

class PyCharm:
    def execute(self):
        print("error detection")
        print("error correction")
        print("compilke")
        print("run")

class laptop:
    def code(self,ide):
        ide.execute()

ide1=VScode()
ide2=PyCharm()

l1=laptop()
l1.code(ide2)
l1.code(ide1)