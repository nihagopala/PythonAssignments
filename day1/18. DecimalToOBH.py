#-----------------------------------------------------------------------#
#Program to convert to Decimal into Binary, Octal and hexaDecimal values
#-----------------------------------------------------------------------#
dec = input("Enter number in Decimal Format: ")
decimal=int(dec)
print("The decimal value of",decimal,"is:")
print(bin(decimal),"in binary.")
print(oct(decimal),"in octal.")
print(hex(decimal),"in hexadecimal.")