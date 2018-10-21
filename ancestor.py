#!/usr/bin/python3
import random as rand
maleA, maleB = "A", "B"
femaleA, femaleB = "A", "B"
males = [maleA, maleB]
females = [femaleA, femaleB]

def nextGenFemales(females):
    mom1 = rand.choice(females)
    females.remove(mom1)
    mom2 = rand.choice(females)
    return [mom1, mom1, mom2, mom2]

def nextGenMales(males):
    num = rand.choice([0,1,2,3,4])
    dad1 = rand.choice(males)
    males.remove(dad1)
    dad2 = rand.choice(males)
    nextGen = []
    for _ in range(num):
        nextGen.append(dad1)
    for _ in range(4-num):
        nextGen.append(dad2)
    return nextGen

def runUntilMono(population, nextGenGen):
    i = 0
    while True:
        i += 1
        population = nextGenGen(population)
        ele, mono = population[0], True
        for individ in population:
            if ele != individ:
                mono = False
                break
        if mono == True:
            return i

def listAvg(l):
    return sum(l)/float(len(l))

def increaseRunsUntil(delta):
    runs = 100
    results1, results2 = [], []
    difference = delta*2
    while difference > delta:
        runs += 10
        for _ in range(runs):
            females = [femaleA, femaleB]
            results1.append(runUntilMono(females, nextGenFemales))            
            females = [femaleA, femaleB]
            results2.append(runUntilMono(females, nextGenFemales))
        avg1, avg2 = list(map(listAvg, [results1, results2]))
        difference = abs(avg1-avg2)
    return runs, round((avg1+avg2)/2,2)

def nRuns(x):
    results = []
    for _ in range(x):
        males = [maleA, maleB]
        results.append(runUntilMono(males, nextGenMales))
    return listAvg(results)


print('female run: ', increaseRunsUntil(0.01)[1])            
print('male run: ', nRuns(100_000))
