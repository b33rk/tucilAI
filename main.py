from localsearch import *
from problem import *
from util import *
import time

p = problem(random_state=0)
scheduler = SA_Scheduler(alpha=0.9999)

start_time = time.time()

StochasticHillCLimb(p, 1000000)
p.analyze_proba()
# HillCLimbSideways(p)
# steepestHillCLimb(p)
# SimuatedAnnealing(p,scheduler)
# RandomRestratHillClimb()
# gen = GeneticAlgo(generations=10000, crossover="cx")
# gen.genetic_algo()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")