import random
import copy
import InitMutFit as imf


def GeneticAlgorithm(steps, popsize, distMat, seed):
    # hardcoded, but can be tuned to increase level of competition
    TOURNAMENTSIZE = 2

    random.seed(seed)
    stops = distMat.shape[0]

    # Initialize population
    parentSols = [imf.InitializeSol(stops) for x in range(popsize)]
    parentFits = [imf.Fitness(parent, distMat) for parent in parentSols]
    bestFit = min(parentFits)
    bestSol = parentSols[parentFits.index(bestFit)]
    childSols = [[] for x in range(popsize)]
    childFits = [[] for x in range(popsize)]
    fitHistory = []

    for i in range(steps):
        # allow population to reproduce
        for j in range(popsize):
            winner = imf.Select(parentFits, TOURNAMENTSIZE)
            childSols[j] = imf.Mutate(parentSols[winner])
            childFits[j] = imf.Fitness(childSols[j], distMat)
        # if we find a new best solution, save it
        if min(childFits) < bestFit:
            bestFit = min(childFits)
            bestSol = childSols[childFits.index(bestFit)]
        # children become parents for next generation
        parentSols = copy.deepcopy(childSols)
        parentFits = copy.deepcopy(childFits)
        if i % 1000 == 0:
            print(bestFit)
            fitHistory.append(bestFit)

    return bestSol, fitHistory
