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


class phone(item): #object PHONE is inherited from class ITEM
    
    all=[]

    def __init__(self, name:str, price:float, quantity:int, damaged=0): #data type and quantity can be specified here
        #call super function to have access to all attributes and method of main class
        super().__init__(
        name,price,quantity
       )

        # run validation to the received argument
        assert damaged>=0

        # assign to self object
        self.damaged=damaged

        #actions to execute
        phone.all.append(self)

phone1=phone("phone",100,5,1)
print(phone1.total_price())

for instance in phone.all:
    print(instance.name)
