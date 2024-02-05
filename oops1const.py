class item:
    pay_disc=0.8 # assign attribute at class level, works for all the objects [IMP--first attributenis checked at instance level, then here at class level]
    all=[]

    def __init__(self,name:str,price:float,quantity=0): #data type and quantity can be specified here
        # print(f"an instance created: {name} ")

        # run validation to the received argument
        assert price>=0 , f"price should be greather than or equal to 0!" #we can specify the assertion error
        assert quantity>=0 #assertion erroe not specified

        # assign to self object
        self.name = name
        self.price=price
        self.quantity=quantity

        #actions to execute
        item.all.append(self)
    
    def total_price(self):
        return self.price * self.quantity

    def apply_disc(self):
        self.price=self.price * self.pay_disc


item1=item("phone",100,2)
# item1.name="phone"
# item1.price=100
item1.apply_disc()
# print(item1.price)
# print(item1.total_price())


item2=item("laptop",200,3) 
item2.has_numpad=False #we can also assign attribute to a specific item
# item2.name="laptop"
# item2.price=200

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)

# print(item1.total_price())
# print(item2.total_price())
for instance in item.all:
    print(instance.name)