#This program calls the adding_report() function which repeatedly takes positive integer input until the user quits and then sums the integers and prints a "report".

#"A" used as the argument to adding_report() results in printing of all of the input integers and the total
#"T" used as the argument results in printing only the total

print("Add an 'A' to see the input list and total or a 'T' to see just the total.")
    #checks for A or T
while True:    
    report_type = input("A/T: ").upper()
    if report_type not in ("A,T"):
      print("Invalid Entry")
    else:
        break
    
    #The adding_report() function has 1 string parameter which indicates the type of report:
def adding_report(report):
        #initialize total variable which will sum integer values entered
        #initialize items variable which will build a string of the integer inputs separated with a new line character
    items = ""
    total=0
    add_integer = ""     
        #inside the function build a forever loop (infinite while loop) and inside the loop complete the following    
    while True:
        #use a variable to gather input (integer or "Q")
        add_integer = input("Enter an integer of 'Q' to quit: ").upper()
        if add_integer.isdigit():
          #check if the input string is a digit (integer) and if it is...    
            items += '\n' + add_integer #if report type is "A" add the numeric character(s) to the item string seperated by a new lin
           #add input iteger to total
            total += int(add_integer)
        elif add_integer.upper() == "Q":#if not a digit, check if the input string is "Q"
            #if the report type is "A" print out all the integer items entered and the sum total
            if report_type.upper() == "A":
                print()
                print("items:",items)
                break
             #if report type is "T" then print out the sum total only    
            elif report_type.upper() == "T":
                break
        #if not a digit and if not a "Q" then print a message that the "input is invalid"
        else:
            print("Invalid Entry")
    print()
    print("total:")
    return total
print(adding_report(report_type))
