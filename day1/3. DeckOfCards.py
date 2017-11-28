#-------------------------------------------#
#Program to print shuffle of cards in random
#-------------------------------------------#

import random

rank = random.choice( ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King') )
suit = random.choice( ('Clubs','Diamonds','Hearts','Spades') )
#card = rank + suit
#print (card) --> Just to print set of cards
print (rank+" of " +suit)
