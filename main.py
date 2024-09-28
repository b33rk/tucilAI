from localsearch import *
from problem import *
from util import *

p = problem()
scheduler = SA_Scheduler(tipe="eksponen")
# SimuatedAnnealing(p, scheduler)
gen = GeneticAlgo(generations=20)
gen.genetic_algo()