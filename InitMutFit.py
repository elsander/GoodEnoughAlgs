import random
import copy


def InitializeSol(stops):
    '''Random starting solution for optimization algorithm.'''
    x = range(stops)
    random.shuffle(x)
    return x


def Mutate(solution):
    '''Mutate a solution by swapping the order of two locations.'''
    solcopy = copy.deepcopy(solution)
    stops = len(solcopy)
    swap1 = random.randint(0, stops - 1)
    swap2 = random.randint(0, stops - 1)
    solcopy[swap1], solcopy[swap2] = solcopy[swap2], solcopy[swap1]
    return solcopy


def Fitness(solution, distMat):
    '''Calculate the fitness of a travel path as the total Euclidean
    distance traveled.'''
    stops = len(solution)
    distance = 0.0
    for i in range(1, stops):
        distance += distMat[solution[i], solution[i - 1]]
    return distance


def Select(fits, tournamentsize):
    '''Choose an individual to reproduce by having them randomly
    compete in a given size tournament.'''
    stops = len(fits)
    competitors = random.sample(range(stops), tournamentsize)
    # who is the best of the competitors?
    compFits = [fits[i] for i in competitors]
    winner = competitors[compFits.index(min(compFits))]
    return winner
