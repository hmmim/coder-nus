class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    def __init__(self,name:str,price:float,quantity:int):
        #Run validations to receive arguments
        #Dòng assert đảm bảo 2 GT (price,quantity) luôn có giá trị dương
        assert price >= 0 #f"Price {self.price} is greater or equal than zero"
        assert quantity >=1 #f"Quantity {self.quantity} is greater or equal than one"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price*self.quantity;
    def apply_discount(self):
         self.price *= self.pay_rate
    def show(self):
        print(f"This item is {self.name} costs {self.price} and there is only {self.quantity} in shop")
class Iphone(Item):
    def __init__(self,name,price,quantity,nationality):
        super().__init__(name,price,quantity)

        self.nationality = nationality
    def show(self):
        print(f"This item is {self.name} costs {self.price} and there is only {self.quantity} in shop and it come from {self.nationality}")
class Laptop(Item):
    pass
i = Iphone("15prm",65,2,"Britain")
i.show()
l = Laptop("Macbook",52,3)
l.show()
item1 = Item("Phone",45,3)
item2 = Item("Laptop",44,6)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
# In ra  tất cả các thuộc tính của đối tượng của Item và item1 dưới dạng một từ điển (dictionary).
print(Item.__dict__) #All the attributes for Class level
print(item1.__dict__) #All the attributes for Instance level
item1.apply_discount()
print(item1.price) #the result is 36:45*0.8
item2 = Item("Laptop",44,6)

item2.pay_rate = 0.6
item2.apply_discount()
print(item2.price)




