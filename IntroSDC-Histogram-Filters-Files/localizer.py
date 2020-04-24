# import pdb
from helpers import normalize, blur
import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    for i in range(0, len(grid)):  # rows
        for j in range (0, len(grid[1])): # columns
            if grid[i][j] == color:
                new_beliefs.append(p_hit*beliefs[i][j])
            else:
                new_beliefs.append(p_miss*beliefs[i][j])

    #sum new beliefs
    new_beliefs_sum = sum(new_beliefs)

    #normalize and reshape to (3,3)
    new_beliefs = np.array(new_beliefs)/new_beliefs_sum
    new_beliefs = new_beliefs.reshape((len(grid), len(grid[1])))

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
