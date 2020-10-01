maximum_order=10
minimum_order=2
price=2
order_amount=input("Enter Order Amount: ")
if int(order_amount)>maximum_order:
    print("Order Maximum is", maximum_order)
elif int(order_amount)<minimum_order:
    print("Order Minimum is",minimum_order)
else:
    print(int(order_amount)*price)