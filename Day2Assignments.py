#--------------------------------------------------------------#
#1. Program to create a variable and assign it the string "Python"
#--------------------------------------------------------------#
technology="Python"
print(technology)
#--------------------------------------------------------------#
#2. Program to create a variable and assign it the length of the
#  string assigned to the variable in step 1
#--------------------------------------------------------------#
length_technology=len(technology)
print(length_technology)
#--------------------------------------------------------------#
#create a variable and use string slicing and len() to assign it
# the length of the slice "yth" from the string assigned to the
# variable from step 1
#--------------------------------------------------------------#
slice_technology=technology[1:4]
print(slice_technology)
#--------------------------------------------------------------#
#create a variable and assign it the float 1.32
#--------------------------------------------------------------#
float_test=float("1.32")
print(float_test)
#--------------------------------------------------------------#
#create a variable and assign it the string "2" from the float
# assigned to the variable from the last problem (use the str()
# string method for this)
#--------------------------------------------------------------#
String_test=str(float_test)
Python_Test=String_test[3]
print(Python_Test)
#--------------------------------------------------------------#
#create a variable and assign it the string "upper" changed to
# "UPPER" using .upper()
#--------------------------------------------------------------#
lower_string="upper"
print(lower_string.upper())
#--------------------------------------------------------------#
#create a variable and assign it the string "owe" from "LOWER"
# using string slicing and .lower() """
#--------------------------------------------------------------#
lower_string="LOWER"
print(lower_string[1:4].lower())
