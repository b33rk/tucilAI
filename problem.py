from util import *
import itertools
import random

class A:
    def __init__(self, state):
        self.state = state
        self.value = Objective_Function(state) 

class problem:
    def __init__(self, random_state=0):
        self.current_state = randomize_initial_state(random_state=random_state)
        coordinates = list(itertools.product(range(0, 5), repeat=3))
        self.all_pairs = [(coor1, coor2) for coor1, coor2 in itertools.combinations(coordinates, 2)]

    def action(self, coor1, coor2):
        next_state = self.current_state
        # print(coor1, coor2)
        next_state[coor1], next_state[coor2] = next_state[coor2], next_state[coor1]
        return next_state

    def get_neighbor(self):
        max_val = 0
        random.shuffle(self.all_pairs)
        for pair in self.all_pairs:
            next_state = self.action(pair[0], pair[1])
            value = Objective_Function(next_state)
            if (value > max_val):
                max_val = value
                neighbor = next_state
        print(pair[0])
        print(pair[1])
        self.current_state = neighbor
        return A(neighbor)

    def get_neighbor_random(self):
        random.shuffle(self.all_pairs)
        next_state = self.action(self.all_pairs[0], self.all_pairs[1])
        self.current_state = next_state
        return A(next_state)


state = randomize_initial_state()
perfect_magic_cube_3x3 = np.array([
    [[22, 11, 9], [2, 27, 13], [18, 4, 20]],
    [[12, 7, 23], [25, 14, 3], [5, 21, 16]],
    [[8, 24, 10], [15, 1, 26], [19, 17, 6]]
])