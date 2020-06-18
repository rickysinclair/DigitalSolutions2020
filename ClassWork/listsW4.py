from random import randint

myList = list()
i = 0
while i < 50:
    num = randint(1, 100)
    print(num)
    myList.append(num)
    i += 1

print(myList)
