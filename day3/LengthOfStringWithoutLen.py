#--------------------------------------------------------------------#
#Define a function that computes the length of a given list or string.
#--------------------------------------------------------------------#
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count

str1=input("Enter the string to calculate it's length: ")
print(string_length(str1))