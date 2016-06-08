import os
import random
import scipy
import math
import HC as hc
import SA as sa
import MCMCMC as mc3
import GA as ga


def DistanceMatrix(coords):
    '''Take a set of coordinates and calculate a matrix of
    Euclidean distances between the points.'''

    # we can assume that xs and ys are the same length
    stops = coords.shape[1]
    distMat = scipy.zeros((stops, stops))

    # this will be symmetric, so we only need to calculate
    # the upper triangular
    for i in range(stops):
        for j in range(i + 1, stops):
            xdist = coords[0, i] - coords[0, j]
            ydist = coords[1, i] - coords[1, j]
            distMat[i, j] = math.sqrt(xdist**2 + ydist**2)
    # add the transpose to make it symmetric
    distMat = distMat + distMat.transpose()
    return distMat


def GenerateMap(stops, fname=None, seed=None):
    '''Generate a map with "stops" stops for the salesman
    to traverse. Write coordinates to file if "fname" is
    specified. Return the distance matrix for all coordinates.'''
    random.seed(seed)
    # randomly place stop coordinates in the unit square
    xs = [random.uniform(0, 1) for x in range(stops)]
    ys = [random.uniform(0, 1) for x in range(stops)]
    coords = scipy.array([xs, ys])
    # calculate matrix of distances
    distMat = DistanceMatrix(coords)
    if fname is not None:
        scipy.savetxt(fname, coords)

    return distMat


def TSP(stops, Alg, steps, param, seed=None,
        coordfile='xycoords.txt'):
    '''A wrapper function that attempts to optimize the traveling
    salesperson problem using a specified algorithm. If coordfile
    exists, a preexisting set of coordinates will be used. Otherwise,
    a new set of "stops" coordinates will be generated for the person to
    traverse, and will be written to the specified file.'''

    # Create the distance matrix, which will be used to calculate
    # the fitness of a given path
    if os.path.isfile(coordfile):
        coords = scipy.genfromtxt(coordfile)
        distMat = DistanceMatrix(coords)
    else:
        distMat = GenerateMap(stops, fname=coordfile, seed=seed)

    if Alg == 'HC':
        # param is the number of solutions to try per step
        bestSol, fitHistory = hc.HillClimber(steps, param, distMat, seed)
    elif Alg == 'SA':
        # param is a placeholder
        bestSol, fitHistory = sa.SimulatedAnnealing(
            steps, param, distMat, seed)
    elif Alg == 'MC3':
        # param is the number of chains
        bestSol, fitHistory = mc3.MCMCMC(steps, param, distMat, seed)
    elif Alg == 'GA':
        # param is the population size
        bestSol, fitHistory = ga.GeneticAlgorithm(steps, param, distMat, seed)
    else:
        raise ValueError('Algorithm must be "HC", "SA", "MC3", or "GA".')

    outfname = coordfile + '-' + Alg + '-' + \
        str(steps) + '-' + str(param) + '.txt'
    scipy.savetxt(outfname, scipy.array(bestSol), fmt='%i')
    return bestSol, fitHistory
