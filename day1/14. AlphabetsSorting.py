#----------------------------------------------------------------#
#Program to sort alphabets in uppercase and lowercase in a string
#----------------------------------------------------------------#

String_sort = input("Enter a string: ")

words = String_sort.split()

words.sort()

print("The sorted words are:")
for word in words:
   print(word)