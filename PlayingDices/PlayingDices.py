from os import error
import numpy as np
import random as rand
import matplotlib.pyplot as plt

#N = int(input("Input the size of array (N): "))
N = 1000

arrayDice1 = [rand.randint(1,6) for i in range(N)]
arrayDice2 = [rand.randint(1,6) for i in range(N)]

def _sum(dice1, dice2):
    aux_list = []
    aux_count = 0
    for i in arrayDice1:
        try:
            aux_list.append(arrayDice1[aux_count] + arrayDice2[aux_count])
            aux_count += 1
        except error:
            print("An error occurred: ", error)
    return np.array(aux_list)

def _mean(diceSumArray, N):
    mean = np.sum(diceSumArray) / N
    return mean

def _stdDev(array, mean , N):
    aux_list = []
    for i in array:
        aux_list.append((i - mean) ** 2)
    std_sum = np.sum(aux_list)
    std_division = std_sum / N
    std_squareRoot = np.sqrt(std_division)
    return std_squareRoot

def _histogram(arraySum):
    x = np.arange(2, 13, 1)
    hist = np.zeros(11)

    for i in arraySum:
        hist[i-2] = hist[i-2] + 1
        
    fig, ax = plt.subplots()
        
    ax.bar(x, hist, color = 'gray', edgecolor = 'black')
    
    ax.set_title('Playing Dices')
    ax.set_ylabel('Frequency')
    
    plt.savefig('dicesHistogram.png')
    plt.show()
          
arraySum = _sum(arrayDice1, arrayDice2)
mean = _mean(arraySum, N)
stdDev = _stdDev(arraySum, mean, N)

print(arraySum)
print(f"Mean ==> Def Mean: {mean}, Numpy Mean: {np.mean(arraySum)}.  Diff = {mean - np.mean(arraySum)}")
print(f"Standart Deviation ==> Def stdDev: {stdDev}, Numpy stdDev: {np.std(arraySum)}.  Diff = {stdDev - np.std(arraySum)}")

boolShowHistogram = bool(input("Input any character to show and save histogram."))

if (boolShowHistogram == True):
    _histogram(arraySum)