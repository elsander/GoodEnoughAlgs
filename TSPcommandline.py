import sys
import TravelingSalesperson as tsp

if __name__ == "__main__":
    stops = int(sys.argv[1])
    Alg = sys.argv[2]
    steps = int(sys.argv[3])
    param = int(sys.argv[4])
    seed = int(sys.argv[5])
    coordfile = sys.argv[6]
    tsp.TSP(stops, Alg, steps, param, seed, coordfile)
