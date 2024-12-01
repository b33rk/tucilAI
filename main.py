from localsearch import *
from problem import *
from util import *
import time

p = problem(random_state=0)
scheduler = SA_Scheduler(alpha=0.9999)

start_time = time.time()

# StochasticHillCLimb(p, 1000000)
# p.analyze_proba()
# HillCLimbSideways(p)
steepestHillCLimb(p)
# SimuatedAnnealing(p,scheduler)
# RandomRestratHillClimb()
# gen = GeneticAlgo(generations=10000, crossover="cx")
# gen.genetic_algo()
# perfect_magic_cube_3x3 = np.array([
#     [[22, 11, 9], [2, 27, 13], [18, 4, 20]],
#     [[12, 7, 23], [25, 14, 3], [5, 21, 16]],
#     [[8, 24, 10], [15, 1, 26], [19, 17, 6]]
# ])

# print(Objective_Function(perfect_cube))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")