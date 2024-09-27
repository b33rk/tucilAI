import numpy as np

def Objective_Function(state, n=5):
    magic_number = (n * (n**3 + 1)) // 2
    fulfilled_properties = 0
    
    # baris
    for i in range(n):
        for k in range(n):
            if np.sum(state[i, :, k]) == magic_number:
                fulfilled_properties += 1
    # print("Baris", fulfilled_properties)
    # kolom
    for j in range(n):
        for k in range(n):
            if np.sum(state[:, j, k]) == magic_number:
                fulfilled_properties += 1
    # print("kolom", fulfilled_properties)
    # tiang
    for i in range(n):
        for j in range(n):
            if np.sum(state[i, j, :]) == magic_number:
                fulfilled_properties += 1
    # print("tiang", fulfilled_properties)
    # diagonal ruang
    if np.sum([state[i, i, i] for i in range(n)]) == magic_number:
        fulfilled_properties += 1
    if np.sum([state[i, i, n-i-1] for i in range(n)]) == magic_number:
        fulfilled_properties += 1
    if np.sum([state[i, n-i-1, i] for i in range(n)]) == magic_number:
        fulfilled_properties += 1
    if np.sum([state[i, n-i-1, n-i-1] for i in range(n)]) == magic_number:
        fulfilled_properties += 1
    # print("diagonal ruang", fulfilled_properties)
    # diagonal potongan bidang
    for i in range(n):
        # XY
        if np.sum([state[j, j, i] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
        if np.sum([state[j, n-j-1, i] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
        
        # XZ
        if np.sum([state[j, i, j] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
        if np.sum([state[n-j-1, i, j] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
        
        # YZ
        if np.sum([state[i, j, j] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
        if np.sum([state[i, n-j-1, j] for j in range(n)]) == magic_number:
            fulfilled_properties += 1
    # print("diagonal potongan bidang", fulfilled_properties)

    return fulfilled_properties

def randomize_initial_state(n=5):
    numbers = np.arange(1, n**3 + 1)
    np.random.shuffle(numbers)
    state = numbers.reshape((n, n, n))
    
    return state