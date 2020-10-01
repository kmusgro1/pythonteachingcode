# [ ] create, call and test the str_analysis() function  
statement = ""
def str_analysis(statement):
   
    while True:
        statement = input("enter a word or number: ")    
        if statement.isdigit():
            statement=int(statement)
            if statement > 99:
                print(statement,"is a big number")
                break
            else:
                print(statement,"is a small number")
                break
        else:
            if statement.isalpha():
                print(statement,"is all alpha")
                break
            else:
                print(statement,"is neither a number or alpha")
    return statement

str_analysis(statement)

