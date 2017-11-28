#-------------------------------------#
# Program to print factors of a number
#-------------------------------------#

#while True:
while True:
    print("Enter 'x' for exit.")
    num = input("Enter a number: ")
    #Whenever the input is given as "X", then it will exit the loop
    if num == 'x':
        break
    else:
        number = int(num)
#The below statement will intialise i to "0" and range is taken from 1 to the number entered by user
        for i in range(1, number):
            if number % i == 0:
                print(i)
                i += 1