#------------------------------------------------------#
#Program to print sum of natual numbers using recursion
#------------------------------------------------------#

while True:
	print("Enter '0' for exit.")
	num = int(input("The number of terms to be added: "))
	if num == 0:
		break
	elif num < 1:
		print("Please enter a positive number")
	else:
		sum = 0
		while num > 0:
			sum += num
			num -= 1
		print("Sum = ", sum)