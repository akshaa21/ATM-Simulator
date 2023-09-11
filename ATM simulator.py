import time

print("Insert your Card")

time.sleep(3)

password = 1234

pin = int(input("Enter your four digit pin : "))

balance = 100000.00

if pin == password:
    while True:
        print('''
        1 == balance
        2 == withdraw balance
        3 == deposit balance
        4 == exit      
              ''')
    
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Please enter the valid option: ")
 
        if option == 1:
            print(f"Your current balance is {balance}")
        elif option == 2:
            withdraw_amount = eval(input("Please enter withdraw_amount : "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is {balance}")
        elif option == 3:
            deposit_amount = eval(input("Please enter deposit_amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is debited from your account")
            print(f"your current balance is {balance}") 
        elif option == 4:
            break   
                
else:
    print("Invalid pin please try again")
