#create a 4 element list that consists of values that are all strings and assign it to a variable
list1 = ['aa', 'bb', 'cc', 'dd']

#create a 3 element list that consists of values that are all numbers and assign it to a variable
list2 = [1, 2, 3]

#create a 5 element list that contains at least 1 string, 1 number, and 1 Boolean value and assign it to a variable
list3 = ['aa', True, 1, 2, 3]

#Print the list you created in step 1
print(list1)

#Access by index and print the second element of the list you made in step 2
print(list2[1])

#Access by index and print the the boolean value from the list you made in step 3
print(list3[1])

#create a variable and assign it the list [1, 2, 3]
list4 = [1, 2, 3]

#reassign the first element in the list from step 1 the value 2
list4[0] = 2

#reassign the second element in the list from step 1 the value 3
list4[1] = 3

#reassign the third element in the list from step 1 the value 4
list4[2] = 4

#use .append() to add the value 6 to the end of the list from step 1
list4.append(6)

#print the resulting list
print(list4)

# create a 7 element list and assign it to a variable
list5 = [1, 2, 3, 4, 5, 6, 7]

#slice the list from its first element to its fourth element and print the resulting 4 element list
list6 = print(list5[:4])

#slice the list from its third element to its fifth element and print the resulting 3 element list
list7 = print(list5[2:5])

#slice the list from its second element to its last element and print the resulting 6 element list
list8 = print(list5[1:])

#1.create a variable and assign it the list ["Bob Dylan", "Like a", "Rolling Stone"]
list9 = ["Bob Dylan", "Like a", "Rolling Stone"]

#2.use the .index() function to find and print the index of the string "Rolling Stone" from the list in step 1
print(list9.index('Rolling Stone'))

# 3.use the .insert() function to insert the string 1965 at index 0 of the list from step 1
list9.insert(0, '1965')

#4.print the list that results from step 3
print(list9)

#1.create a variable and assign it the list ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
list10 = ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]

# 2.use .remove() to remove of the "Sutcliffe" from the list created in step 1.
list10.remove('Sutcliffe')

#print the new list
print(list10)

#.use .pop() to remove and print "Lennon" from the list
print(list10.pop(1))

#use .pop() to remove and print "Harrison" from the list
print(list10.pop())

#6.print the new list
print(list10)