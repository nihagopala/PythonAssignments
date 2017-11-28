#---------------------------------------------------------#
#Program to print Decimal to binary values using recursion
#---------------------------------------------------------#

while True:
    print("Enter 'x' for exit.")
    dec = input("Enter number in Decimal Format: ")
    if dec == 'x':
        break
    else:
        decimal = int(dec)
        print(decimal, "in Binary =", bin(decimal), "\n")