from localsearch import *
from problem import *
from util import *
import time

p = problem()
scheduler = SA_Scheduler(tipe="eksponen")

start_time = time.time()

SimuatedAnnealing(p, scheduler)
# gen = GeneticAlgo(generations=1000)
# gen.genetic_algo()

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")