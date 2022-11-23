print("------------------Humber Bank Terminal------------------")
print("<<Pin is 0291 for testing>>")
print("Hello!")
attempts = 1
pin = "0291"
balance = 200

def withdrawal(balance):
    w_menu = "1. $20\n2. $40\n3. $60\n4. $80\n5. $100\n6. Custom\nChoose an option (1/2/3/4/5/6): "
    w_c = int(input(w_menu))
    list_v = [20,40,60,80,100]

    while w_c < 1 or w_c > 6:
        w_c = int(input(w_menu))

    if w_c >= 1 and w_c <= 5:
        amount = list_v[w_c-1]
    elif w_c == 6:
        amount = float(input("Enter an amount to withdraw: "))
    
    if amount >= balance:
        print("Amount exceeds your balance. ${:.2f} will be returned".format(amount))
        amount = balance
        balance = 0

    else:
        balance -= amount
    print("Your current balance is ${:.2f}.".format(balance))
    return balance

def deposit(balance):
    try:
        amount = float(input("Enter an amount to deposit: "))
    except:
        print("Your value should be a number!")
        amount = float(input("Enter an amount to deposit: "))

    balance += amount
    print("Your current balance is ${:.2f}.".format(balance))
    return balance

enter_pin = input("Enter your four digit pin now: ")
while enter_pin != pin and attempts < 3:
    attempts += 1
    enter_pin = input("Enter your four digit pin now: ")

if enter_pin != pin:
    print("You have exceeded the number of attempts. Goodbye.")

else:
    loop = True
    while loop:
        main_menu = "1. Check Your Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Quit\nChoose your option: "
        choice = int(input(main_menu))
        if choice == 1:
            print("Your current balance is ${:.2f}.".format(balance))
        elif choice == 2:
            balance = withdrawal(balance)
        elif choice == 3:
            balance = deposit(balance)
        elif choice == 4:
            loop = False
        
        if choice != 4:
            loop_c = input("Would you like to perform another operation?(y/n): ")
            if loop_c.lower() == 'n':
                loop = False