#-----------------------------------------------------------------#
#Write a python program which acts as a calculator (function based)
#-----------------------------------------------------------------#
def calculator():
    Mathoperation = input('''
-------------------------------------------------------------
Please type in the math operation you would like to complete:
-------------------------------------------------------------
+ for addition
- for subtraction
* for multiplication
/ for division
-------------------------------------------------------------
''')

    number1 = int(input('Please enter the first number: '))
    number2 = int(input('Please enter the second number: '))

    if Mathoperation == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif Mathoperation == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif Mathoperation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif Mathoperation == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculator()