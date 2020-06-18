from random import randint

myList = list()
i = 0

while i < 50:
    num = randint(1, 10)
    print(num)
    myList.append(num) # add an item to the end of a list
    i += 1

print(myList)

myList.remove(3) # remove item from list
print(myList)
myList.sort() # sort list acs
print(myList)

print(min(myList))
print(max(myList))
