#-----------------------------------------------------------------------------#
#Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".
#-----------------------------------------------------------------------------#
def reverse(inputString):
    return inputString[::-1]

print ("Enter the string to reverse")
stringToReverse = input()
print("The reversal of "+stringToReverse+" is "+reverse(stringToReverse))

