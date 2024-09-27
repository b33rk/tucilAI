from problem import *

def steepestHillCLimb(problem):
    current  = A(problem.current_state)
    while True:
        neighbor = problem.get_neighbor()
        print(neighbor.value)
        print(current.value)
        if neighbor.value <= current.value:
            return current.state
        current = neighbor