#Problems on Tuples

#1.create a 4 element tuple that consists of a float, an integer, a Boolean value, and a string.  Assingn this tuple to a  variable
Tuples_test = ('CITI', True, 1, 10.5)

#2.print the tuple from step
print(Tuples_test)

# 3.print the the second element from the tuple you made in step 1
print(Tuples_test[1])

# 4.print the first element from the tuple you made in step 1
print(Tuples_test[0])

# 5.slice and print the first 3 elements of the tuple from step 1
print(Tuples_test[:3])

# slice and print the last 3 elements of the tuple from step 1
print(Tuples_test[-3:])

# 7.slice and print the middle 2 elements of the tuple from step 1
print(Tuples_test[1:-1])


#Problems related to For Loop

# 1.create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
Loop = ("Bohr", "Leibniz", "Einstein")

#2.create a variable and assign it an empty list
List = []

# create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
ListValue = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4.use a for loop to go through and print each of the elements from the tuple in step 1 individually
for i in Tuples_test:
    print (i)

# use a for loop and .append() to add the middle 6 elements to the empty list from step 2
for i in range(2, 8):
    List.append(ListValue[i])

#print the new list
print(List)