from os import error
import numpy as np
import random as rand

N = int(input("Input the size of array (N): "))

arrayDice1 = [rand.randint(1,6) for i in range(N)]
arrayDice2 = [rand.randint(1,6) for i in range(N)]
dicesSum = []

def _sum(dice1, dice2):
    aux_count = 0
    for i in arrayDice1:
        try:
            dicesSum.append(arrayDice1[aux_count] + arrayDice2[aux_count])
            aux_count += 1
        except error:
            print("An error occurred: ", error)
    return np.array(dicesSum)
          
arraySum = _sum(arrayDice1, arrayDice2)

print(arrayDice1)
print(arrayDice2)
print(arraySum)