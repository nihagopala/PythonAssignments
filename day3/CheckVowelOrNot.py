#------------------------------------------------------------------#
#Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False otherwise.
#------------------------------------------------------------------#
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char ==  'O' or char == 'U':
        return True
    else:
        return False
char=input("Enter some letter: ")
if isVowel(char)==False:
    print("You have entered "+char+", which is not a vowel ")
else:
    print("You have entered "+char+", which is a vowel ")



