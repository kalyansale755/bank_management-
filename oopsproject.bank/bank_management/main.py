from customer import Customer
from account import BankAccount

customer = Customer()

while True:

    print("\n===== BANK MANAGEMENT SYSTEM ===== - main.py:8")
    print("1. Register - main.py:9")
    print("2. Login - main.py:10")
    print("3. Exit - main.py:11")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        phone = input("Enter Phone: ")

        customer.register(name, email, password, phone)


    elif choice == "2":

        email = input("Enter Email: ")
        password = input("Enter Password: ")

        user = customer.login(email, password)

        if user:

            customer_id = user[0]

            account = BankAccount(customer_id)

            while True:

                print("\n1. Deposit - main.py:40")
                print("2. Withdraw - main.py:41")
                print("3. Balance Check - main.py:42")
                print("4. Mini Statement - main.py:43")
                print("5. Logout - main.py:44")

                option = input("Enter Option: ")

                if option == "1":

                    amount = float(input("Enter Amount: "))
                    account.deposit(amount)

                elif option == "2":

                    amount = float(input("Enter Amount: "))
                    account.withdraw(amount)

                elif option == "3":

                    account.check_balance()

                elif option == "4":

                    account.mini_statement()

                elif option == "5":
                    break

                else:
                    print("Invalid Option - main.py:70")


    elif choice == "3":
        print("Thank You - main.py:74")
        break

    else:
        print("Invalid Choice - main.py:78")