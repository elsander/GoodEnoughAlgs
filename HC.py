import random
import InitMutFit as imf


def HillClimber(steps, tryPerStep, distMat, seed):
    random.seed(seed)
    stops = distMat.shape[0]
    # Randomly generate our starting point
    bestSol = imf.InitializeSol(stops)
    bestFit = imf.Fitness(bestSol, distMat)

    # Initialize data structure for trial solutions and fitnesses
    trialSols = [[] for x in range(tryPerStep)]
    trialFits = [[] for x in range(tryPerStep)]
    fitHistory = []

    for i in range(steps):
        # try several steps
        for j in range(tryPerStep):
            trialSols[j] = imf.Mutate(bestSol)
            trialFits[j] = imf.Fitness(trialSols[j], distMat)
        # is the best trial solution better than our current best?
        # If so, replace. Otherwise, move to next step
        # Note that we are minimizing here
        if min(trialFits) < bestFit:
            bestFit = min(trialFits)
            bestSol = trialSols[trialFits.index(bestFit)]
        if i % 1000 == 0:
            print(bestFit)
            fitHistory.append(bestFit)
    return bestSol, fitHistory
