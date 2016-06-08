import random
import math
import InitMutFit as imf


def InitializeTemps(maxtemp, mintemp, nchains):
    # Uniform spacing here, but this can be done differently
    # Log spacing is another option. In my experience this
    # has led to overall higher swap acceptance rates.
    tempstep = float(maxtemp - mintemp) / float(nchains - 1)
    temps = [maxtemp - i * tempstep for i in range(nchains)]
    return temps


def TrySwap(hotFit, coldFit, hotTemp, coldTemp):
    # save computation and prevent overflow error
    if hotFit < coldFit:
        return True

    prob = math.exp((coldFit - hotFit) * (1 / coldTemp - 1 / hotTemp))
    if random.random() <= prob:
        return True
    else:
        return False


def MCMCMC(steps, nchains, distMat, seed):
    # hardcoded, but these can also be tuned!
    SWAPSTEPS = 20
    MAXTEMP = 5
    MINTEMP = .001

    random.seed(seed)
    stops = distMat.shape[0]

    # Initialize temperatures and chains
    temps = InitializeTemps(MAXTEMP, MINTEMP, nchains)
    chains = [imf.InitializeSol(stops) for x in range(nchains)]
    fits = [imf.Fitness(chain, distMat) for chain in chains]
    bestFit = min(fits)
    bestSol = chains[fits.index(bestFit)]
    fitHistory = []

    for i in range(steps):
        # swap chains
        if i % SWAPSTEPS == 0:
            for j in range(0, nchains - 1):
                flag = TrySwap(fits[j], fits[j + 1], temps[j], temps[j + 1])
                if flag:
                    chains[j], chains[j + 1] = chains[j + 1], chains[j]
                    fits[j], fits[j + 1] = fits[j + 1], fits[j]
        # let each chain take a step
        for j in range(nchains):
            trialSol = imf.Mutate(chains[j])
            trialFit = imf.Fitness(trialSol, distMat)
            if trialFit < fits[j]:
                # automatically accept to avoid overflow error
                probAccept = 1
            else:
                probAccept = math.exp((fits[j] - trialFit) / temps[j])
            if random.random() <= probAccept:
                fits[j] = trialFit
                chains[j] = trialSol
                # update best solution if appropriate
                if trialFit < bestFit:
                    bestFit = trialFit
                    bestSol = trialSol

        if i % 1000 == 0:
            print(bestFit)
            fitHistory.append(bestFit)

    return bestSol, fitHistory
