class admin:

    toiletries = {"toilet paper":30,"hand soap":25,"face wash":165,"body wash":220,"shampoo":280}
    food = {"chips":20,"cold drinks":40,"cakes":30,"protein bars":45,"milkshakes":35,"juices":110}
    electronics = {"trimmer":800,"table lamp":450,"pen drive":400,"charger":290,"watch":800}
    sports = {"cricket bat":1000,"baseball bat":700,"football":450,"badminton racquet":750,"table tennis kit":600}
    
    types = ["toiletries",'food','electronics','sports']
    discounts = {"toiletries":0.1,"food":0.05,"electronics":0.2,"sports":0.25}

    def __init__(self,type_of_item,name,discount):
        self.name = name
        self.discount = discount
        self.type_of_item = type_of_item

    def change_discount(self,discount):
        admin.discounts[self.type_of_item] = discount
        
class customer():

    cart = {}
    discounted_items = {}

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def add_to_cart(self):
        customer.cart[self.name] = self.quantity

    def remove_from_cart(self):
        del customer.cart[self.name]

print("hi, welcome to Akshay stores!")
print("please enter your id")
id = input()
print("please enter your name")
name = input()

print("please enter if you are a customer or an admin")
type = input()

print()
print("the stock currently present in the store is: ")
print()
print("toiletries include-->")
print()
for key, value in admin.toiletries.items():
    print(key, ' : ', value)
print("food items include-->")
print()
for key, value in admin.food.items():
    print(key, ' : ', value)
print("electronics include-->")
print()
for key, value in admin.electronics.items():
    print(key, ' : ', value)
print("sports items include-->")
print()
for key, value in admin.sports.items():
    print(key, ' : ', value)

print()
print("the discounts on the items are--> ")
print()
for key, value in admin.discounts.items():
    print(key, ' : ', value*100,"%")
print()

if type == "admin":

    print()
    print("hey you can change the discounts any of the items in the store")

    while 1==1:
        print()
        yn = input("if you want to make any changes to the items type 'yes' if not enter any other key: ")
        print()

        if yn == "yes":
            ch = int(input("enter 1 to change discount of any article: "))

            if ch==1:
                print()
                s1=input("enter the type of item: ")
                s2=input("enter the name of the item: ")
                s3=input("enter the changed discount(as a decimal): ")
                s = admin(s1,s2,s3).change_discount(s3)

        else:
            break

    print()
    print("the store looks like -->")
    print()
    print("toiletries include-->")
    print()
    for key, value in admin.toiletries.items():
        print(key, ' : ', value)
    print("food items include-->")
    print()
    for key, value in admin.food.items():
        print(key, ' : ', value)
    print("electronics include-->")
    print()
    for key, value in admin.electronics.items():
        print(key, ' : ', value)
    print("sports items include-->")
    print()
    for key, value in admin.sports.items():
        print(key, ' : ', value)
    print()
    print("the discounts as per the item types are-->")
    for key, value in admin.discounts.items():
        print(key, ' : ', float(value)*100,"%")
    print()
    print("The profits earned per item are-->")
    print()
    print("the profits earned per item are as follows-->")
    print()
    profit = {"toiletries":0.25,"food":0.15,"electronics":0.30,"sports":0.35}
    print("profit structure of toiletries: ")
    print()
    for key,value in admin.toiletries.items():
            print (key,":",value*profit["toiletries"])
    print()
    print("profit structure of food: ")
    print()
    for key,value in admin.food.items():
            print (key,":",value*profit["food"])
    print()
    print("profit structure of electronics: ")
    print()
    for key,value in admin.electronics.items():
            print (key,":",value*profit["electronics"])
    print()
    print("profit structure of sports: ")
    print()
    for key,value in admin.sports.items():
            print (key,":",value*profit["sports"])
    print()

elif type == "customer":

    print()
    print("hey you can buy any item in the store")

    while 1==1:
        print()
        yn = input("if you want to make any changes to the cart type 'yes' if not enter any other key: ")
        print()

        if yn == "yes":
            ch = int(input("enter 1 to add an item to the cart or 2 to remove any item from the cart: "))

            if ch==1:
                print()
                s1=input("enter the name of the item: ")
                s2=input("enter the quantity of the item: ")
                s = customer(s1,s2).add_to_cart()

            elif ch==2:
                print()
                s1=input("enter the name of the item: ")
                s2=input("enter the quantity of the item: ")
                s = customer(s1,s2).remove_from_cart()

        else:
            break

    print()
    print("your cart looks like-->")
    for key, value in customer.cart.items():
        print(key, ' : ', value)
    print()
    pt = 0
    for key, value in customer.cart.items():
        if key in admin.toiletries:
            pt += float(value)*float(admin.toiletries[key])*float((1-admin.discounts["toiletries"]))
        elif key in admin.electronics:
            pt += float(value)*float(admin.electronics[key])*float((1-admin.discounts["electronics"]))
        elif key in admin.food:
            pt += float(value)*float(admin.food[key])*float((1-admin.discounts["food"]))
        elif key in admin.sports:
            pt += float(value)*float(admin.sports[key])*float((1-admin.discounts["sports"])) 
        else:
            print(key,"is not in stock so you can't buy it")  
            print()
        print("the total price of your purchase after discounts is: ₹",pt)
    print()
    
    pr=0
    for key, value in customer.cart.items():
        if key in admin.toiletries:
            pr += float(value)*float(admin.toiletries[key])*float(admin.discounts["toiletries"])
        elif key in admin.electronics:
            pr += float(value)*float(admin.electronics[key])*float(admin.discounts["electronics"])
        elif key in admin.food:
            pr += float(value)*float(admin.food[key])*float(admin.discounts["food"])
        elif key in admin.sports:
            pr += float(value)*float(admin.sports[key])*float(admin.discounts["sports"])
        else:
            print(key,"was not in stock")  
            print()
        print("the total money that you saved after discounts is: ₹",pr)

    print()
    print("thank you for shopping at Akshay stores!")



    














