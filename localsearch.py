from problem import *

# Steepest Ascent Hill-climbing
# Hill-climbing with Sideways Move
# Random Restart Hill-climbing
# Stochastic Hill-climbing
# Simulated Annealing
# Genetic Algorithm

def steepestHillCLimb(problem):
    current  = A(problem.current_state)
    while True:
        neighbor = problem.get_neighbor()
        print(neighbor.value)
        print(current.value)
        if neighbor.value <= current.value:
            return current.state
        current = neighbor

def HillCLimbSideways(problem):
    current  = A(problem.current_state)
    while True:
        neighbor = problem.get_neighbor()
        print(neighbor.value)
        print(current.value)
        if neighbor.value < current.value:
            return current.state
        current = neighbor

def HillCLimbSideways(problem):
    current  = A(problem.current_state)
    while True:
        neighbor = problem.get_neighbor()
        print(neighbor.value)
        print(current.value)
        if neighbor.value < current.value:
            return current.state
        current = neighbor

def RandomRestratHillClimb():
    random_state = 0
    print("a")
    p = problem(random_state)
    current  = A(p.current_state)
    while current.value < 10:
        p = problem(random_state)
        random_state += 1
        current  = A(p.current_state)
        while True:
            neighbor = p.get_neighbor()
            print(neighbor.value)
            print(current.value)
            if neighbor.value <= current.value:
                return current.state
            current = neighbor
    print(current.state)