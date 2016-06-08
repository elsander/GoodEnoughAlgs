# Good Enough Algorithms
## Evolutionary algorithms and other heuristic optimizers

This is code associated with talks, workshops, and a
[blog post](http://www.lizsander.com/programming/2015/08/04/Heuristic-Search-Algorithms.html)
I have written about heuristic optimization algorithms. This repository
contains the code needed to run four algorithms -- a hill climber,
simulated annealing, Metropolis-coupled MCMC, and a genetic
algorithm -- to find good solutions to the travelling salesperson
problem. The code is written in a modular way that is meant to make it
easy to adapt to other optimization problems. This code is written in
Python3; for a Python2 implementation, see
[this repository](https://github.com/esander91/RecurseCenter/tree/master/OptimWorkshop).

An overview of the directory:

- *InitMutFit.py* contains functions to initialize, mutate, select,
and calculate fitness for solutions.
- *HC.py*, *SA.py*, *MCMCMC.py*, and *GA.py* contain implementations
  of a hill climber, simulated annealing, MCMCMC, and a genetic
  algorithm, respectively.
- *TravelingSalesperson.py* is a wrapper for all of the specific
  implementations of the problem. This is a fairly generic wrapper
  that can be fitted to different optimization problems.
- *TSPcommandline.py* is a command line wrapper for
*TravelingSalesperson.py*.
- *Visualizations.py* provides some functions to display how the
  different algorithms performed. All `.txt` files in the
  `ExampleOutput` folder can be used in these visualizations.

This code requires the following modules:
- copy
- math
- os
- pylab
- random
- scipy
- sys

If you run into any problems, please submit an issue!
