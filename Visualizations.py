import TravelingSalesperson as tsp
import scipy
import pylab as pl


def PlotMultipleRuns(Alg, nruns=20, fname=None):
    '''Plot "nruns" runs of a given algorithm to show performance
    and variability across runs.'''
    if fname:
        runs = scipy.genfromtxt(fname)
    else:
        runs = []
        for i in range(nruns):
            bestSol, fitHistory = tsp.TSP(200, Alg, 20000, 30, seed=None,
                                          coordfile='tmp.txt')
            runs.append(fitHistory)
        fname = 'MultRuns-' + str(Alg) + '.txt'
        runs = scipy.array(runs)
        scipy.savetxt(fname, runs)

    # plotting
    Xs = range(0, runs.shape[0] * 1000, 1000)
    for i in range(runs.shape[0]):
        pl.plot(Xs, runs[i, :])
    pl.show()


def LongMC3(fname=None):
    '''Plot a single long MC3 run to demonstrate high performance
    but slow convergence.'''
    if fname:
        run = scipy.genfromtxt(fname)
    else:
        bestSol, run = tsp.TSP(200, 'MC3', 200000, 10, seed=None,
                               coordfile='tmp.txt')
        fname = 'ExampleOutput/MC3-Long.txt'
        run = scipy.array(run)
        scipy.savetxt(fname, run)

    # plotting
    Xs = range(0, run.shape[0] * 1000, 1000)
    pl.plot(Xs, run)
    pl.show()


def LongSA(fname=None):
    '''Plot a single long SA run to demonstrate performance under slower
    cooling schedule.'''
    if fname:
        run = scipy.genfromtxt(fname)
    else:
        bestSol, run = tsp.TSP(200, 'SA', 200000, 'placeholder', seed=None,
                               coordfile='tmp.txt')
        fname = 'ExampleOutput/SA-Long.txt'
        run = scipy.array(run)
        scipy.savetxt(fname, run)

    # plotting
    Xs = range(0, run.shape[0] * 1000, 1000)
    pl.plot(Xs, run)
    pl.show()
