#---------------------------------------------#
# Program to make Calculator with a below menu
#---------------------------------------------#

while True:
    print("************Menu************")
    print("----------------------------")
    print("1. To perform Addition")
    print("2. To perform Subtraction")
    print("3. To Perform Multiplication")
    print("4. To perform Division")
    print("5. To perform Modulus")
    print("6. To apply exponent/ power")
    print("7. Exit")
    print("----------------------------")
    choice = int(input("Please enter your choice: "))
    if (choice >= 1 and choice <= 6):
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())
        if choice == 1:
            res = num1 + num2
            print("Result = ", res)
        elif choice == 2:
            res = num1 - num2
            print("Result = ", res)
        elif choice == 3:
            res = num1 * num2
            print("Result = ", res)
        elif choice == 4:
            res = num1 / num2
            print("Result = ", res)
        elif choice == 5:
            res = num1 % num2
            print("Result = ", res)
        else:
            res = num1 ** num2
            print("Result = ", res)
    elif choice == 7:
        break
    else:
        print("The input you have entered is incorrect..!!")