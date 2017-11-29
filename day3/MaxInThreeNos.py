#-----------------------------------------------------------#
#Define a function max_of_three() that takes three numbers as
# arguments and returns the largest of them.
#-----------------------------------------------------------#
def Max_Three(a,y,z):
    max_3 = 0
    if a > y:
        if a > z:
            max_3 = a
        else:
            max_3 = z
    else:
        if y > z:
            max_3 = y
        else:
            max_3 = z
    return max_3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number:"))

print("The largest number of three numbers is", Max_Three(num1, num2, num3))
