#!/usr/bin/python3
import string, random, statistics

bees = list(string.ascii_lowercase)[:10]
rate = 7
deltaR = rate * 0.05
bees_rate = {bee: rate for bee in bees}
mutant = random.choice(bees)

def generate20eggs(bees_rate=bees_rate, mutant=mutant, mutantRate=5):
    gen = 0
    new_eggs = []
    egg_population = 20
    while len(new_eggs) < egg_population:
        gen += 1
        current_run_new = 0
        for bee in bees:
            x = round(random.random()*100)
            if bees_rate[bee] >= x:
                current_run_new += 1
                new_eggs.append(bee)
                for bee in bees:
                    if bee == mutant:
                        bees_rate[bee] += mutantRate * 0.05
                    else:
                        bees_rate[bee] -= deltaR

                # if bee == mutant:
                #     bees_rate[bee] += mutantRate*0.05
                # else:
                #     bees_rate[bee] -= deltaR

    if len(new_eggs)> egg_population:
        endSelect = random.sample(new_eggs[-1*current_run_new:], len(new_eggs)-egg_population)
        finalSelectEggs = new_eggs[:egg_population-len(endSelect)] + endSelect
        new_eggs = finalSelectEggs
    
    if len(new_eggs) == egg_population:
        return gen, new_eggs
    else:
        raise RuntimeError('note egg length error')
        # return generate20eggs(bees_rate, mutant, mutantStartingRate)

def selectGenRuns(genAndNewEggs):
    return genAndNewEggs[0]

def listAvg(l):
    return sum(l)/float(len(l))

def pctMutant(eggs, mutant):
    matches = 0 
    for egg in eggs:
        if egg == mutant:
            matches += 1
    return (matches/len(eggs))*100

import matplotlib.pyplot as plt
checkRates = [x+1 for x in range(99)]
rateL, generationL, mutationRateL = [], [], []
# for rate in range(2,12):
for rate in [y*0.5+2.0 for y in range(0,48)]:
    rateL.append(rate)
    deltaR = rate * 0.05
    print('rate: ', rate, end='; ')
    for mutantRate in checkRates:
        lavg = []
        gens = []
        for _ in range(500):
            bees_rate = {bee: rate for bee in bees}
            bees_rate[mutant] = mutantRate
            generations, newEggs = generate20eggs(bees_rate, mutant, mutantRate)
            lavg.append(pctMutant(newEggs, mutant))
            gens.append(generations)
        if (sum(lavg)/len(lavg))>=50:
            print('avg gens: ', sum(gens)/len(gens), end='; ')
            print('mutant rate: ', round(mutantRate,2))
            generationL.append(sum(gens)/len(gens))
            mutationRateL.append(round(mutantRate,2))
            break
plt.plot(rateL, generationL)
plt.plot(rateL, mutationRateL)
plt.show()