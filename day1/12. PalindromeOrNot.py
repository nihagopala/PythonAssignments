#-----------------------------------------------------------#
#Program to check if the given number is a palindrome or not
#-----------------------------------------------------------#

while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		string = string.casefold()
		rev = reversed(string)
		if list(string) == list(rev):
			print(" It is a Palindrome \n")
		else:
			print(" It is not a Palindrome \n")