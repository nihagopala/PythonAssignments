#---------------------------------------------------------------#
#Creating Dictionaries, Accessing by Key, Adding to Dictionaries,
#  and Length of a Dictionary:
#---------------------------------------------------------------#

#1.create a 3 key: value pair dictionary and assign it to a variable
a = {'Name': 'Niharika', 'Age': 23, 'Batch': 'Trainee'}

#2.access and print a value from the list in step 1 by key
print(a['Name'])

#3.add a fourth key: value pair to the dictionary from step 1
a['city'] = "Chennai"

# 4.print the dictionary from step 3
print(a)

#5.print the length of the dictionary from step 3
print(len(a))


#Reassignment by Key and Del:

#1.create a 2 key: value pair dictionary and assign it to a variable
my_dict = {'Name': 'Niharika', 'Age': 23}

# 2.print the dictionary from step 1
print(my_dict)

# 3.reassign a key from the dictionary in step 1 a different value than its original value
my_dict['address'] = 'MIPL chennai'

# 4.print the dictionary from step 3
print(my_dict)

# remove a key: value pair from the dictionary from step 3 using del
del my_dict['Age']

#6.print the new dictionary
print(my_dict)