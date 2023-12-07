user_input = int(input("Enter your choice : 1 : Calculator and "
                       "2 : Email - Password verification :  "))

if user_input == 1:
    '''
    THIS IS A BASIC CALCULATOR FOR SOME MATHEMATICAL OPERATIONS 
    
    '''
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    operation = input("Enter the opertaion you want to perform from ( +,-,*,/,//) :  ")


    if operation == "+":
        print(f"This is the Addition of {num_1} and {num_2} = {num_1 + num_2} ")

    elif operation == "-":
        print(f"This is the Subtraction of {num_1} and {num_2} = {num_1 - num_2} ")

    elif operation == "*":
        print(f"This is the Multiplication of {num_1} and {num_2} = {num_1 * num_2} ")

    elif operation == "/":
        print(f"This is the Divide of {num_1} and {num_2} = {num_1 / num_2} ")

# THIS IS USED TO AVOID DECIMAL VALUES IT WILL ROUND DOWN THE RESULT TO NEAREST WHOLE NUMBER
    elif operation == "//":
        print(f"This is the Floor Divide of {num_1} and {num_2} = {num_1 // num_2} ")

    else:
        print("Invalid Input")


elif user_input == 2:
    '''
    THIS IS A DATA OF ANY COMPANY AND IT CONTAINING THE EMAIL ID AND THE PASSWORDS
    SO TO GET ACCESS USER NEED TO PROVIDE RIGHT EMAIL FOR THAT IF THE EMAIL IS NOT IN  COMPANY DATA
    THAN IT WILL SHOW THAT EMAIL DOES NOT EXISTS AND IF EMAIL IS IN COMPANY DATA THAN IT WILL ASK FOR 
    PASSWORD AND IF THE PASSWORD IS WRONG IT WILL PRINT THE MESSAGE OF INVALID PASSWORD AND IF 
    PASSWORD MATCHES IT WILL GIVE ACCESS AND PRINT THE MESSAGE THAT [ACCESS GRANTED]   
    '''

    My_Company = ["himjoshi@gmail.com","dev@gmail.com","happy@gmail.com","anju@gmail.com"]
    Password = ["22342","1234","4456","5678"]
    E_Mail = input("Enter your E-mail id here: ")

    if E_Mail.lower() in My_Company:
        passw = input("Enter your password : ")
        if Password[My_Company.index(E_Mail)] == passw:
            print("Access Granted")

        else:
            print("Invalid Password")

    else:
        print("Invalid  E-mail Id")





else:
    print("Invalid Input")
