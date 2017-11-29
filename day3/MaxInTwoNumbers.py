
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print ('Enter the first number')
num1 = input()

print ('Enter the second number')
num2 = input()

print (str(max(num1 ,num2)) + ' is largest among '+num1+" and "+num2)