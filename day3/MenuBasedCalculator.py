#---------------------------------------------------------------#
#Write a python program which acts as a calculator. (menu based)
#---------------------------------------------------------------#
Math_operation = input('''
-------------------------------------------------------------
Please type in the math operation you would like to complete:
-------------------------------------------------------------
+ for addition
- for subtraction
* for multiplication
/ for division
-------------------------------------------------------------
''')

number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))

if Math_operation == '+':
    print('{} + {} = '.format(number1, number2))
    print(number1 + number2)

elif Math_operation == '-':
    print('{} - {} = '.format(number1, number2))
    print(number1 - number2)

elif Math_operation == '*':
    print('{} * {} = '.format(number1, number2))
    print(number1 * number2)

elif Math_operation == '/':
    print('{} / {} = '.format(number1, number2))
    print(number1 / number2)

else:
    print('You have not typed a valid operator, please run the program again.')

