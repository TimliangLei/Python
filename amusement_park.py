age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price =10
elif age >= 65:
    price = 5
print("Your admission cost is $"+str(price)+".")
        
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making  your pizza!")
else:
    print("Are you sure you want a plain pizza?")
