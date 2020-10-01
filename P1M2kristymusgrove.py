def fishstore(fish,price):
    fishstore_statement="The price for " + fish + " is $" + price +"."
    return fishstore_statement
#fish_entry="1"
#price_entry="2"
fish_entry=input("Fish Type: ")
price_entry=input("Fish Price: ")

print(fishstore(fish_entry,price_entry))
