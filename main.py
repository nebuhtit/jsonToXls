import random


d = {1: "lol", 2: "sdf", 345: "c"}

def randFromDict(Dictt):
    dl = list(Dictt.keys())
    # print(dl)
    rand_key = random.choices(dl)[0]
    # print(rand_key)
    rand_value = d[rand_key]
    # print(rand_value)
    return rand_key, rand_value
rk, rv = randFromDict(d)
print(rk)
print(rv)
list = list(d.values())

list.remove(rv)

dop0 = (random.choices(list))[0]
print("dop0", dop0)
dop1 = str(dop0)
while dop1 == dop0:
    dop1 = random.choices(list)[0]
print("dop1", dop1)

listOfChoices = [rv, dop0, dop1]
print(listOfChoices)

listOfChoicesRand = listOfChoices
while listOfChoices == listOfChoicesRand:
    listOfChoicesRand = random.sample(listOfChoices, len(listOfChoices))
print(listOfChoicesRand)





i = input("write your answer:")
if i == rv:
    print('right!')
else:
    print("sorry? but it is ", rv)
print(rv)
