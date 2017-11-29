#-------------------------------------------------------------------------#
#Define a function sum() and a function multiply() that sums and multiplies
# (respectively) all the numbers in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and
# multiply([1, 2, 3, 4]) should return 24
#-------------------------------------------------------------------------#
def addListMembers(List):
    totalSum = 0
    for i in List:
        totalSum = int(totalSum) + int(List[i - 1])

    return totalSum


def multiplyListMembers(List):
    totalMultipliedAmount = 1
    for i in List:
        totalMultipliedAmount = totalMultipliedAmount * int(List[i - 1])

    return totalMultipliedAmount


List1 = [1, 2, 3, 4]

print("The initial list is: " + str(List1[:]))

print("Sum of the members of the list is: " + str(addListMembers(List1)))

print("Multiplied value of the members of the list is: " + str(multiplyListMembers(List1)))

