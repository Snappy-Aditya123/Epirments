import time

#for .py files simulation an example print simulation in one line 
"""
def simulate():
    for i in range(10):
        step = ''.join("*" * j for j in range(i))
        print(f"Simulation step {i} {step}")
        time.sleep(3)  # Simulate some process or change
        # Clear the screen before printing the next step
        print("\033[H\033[J", end='')  # ANSI escape sequence to clear the screen
simulate()""" 

''' 
Thsi generstes s rsndom grid 
import time
import random

def initialize_grid(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(' '.join(['*' if cell else ' ' for cell in row]))
    print('\n')

def game_of_life(size, steps):
    grid = initialize_grid(size)
    for _ in range(steps):
        print_grid(grid)
        new_grid = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                live_neighbors = sum(grid[(i + x) % size][(j + y) % size] for x in (-1, 0, 1) for y in (-1, 0, 1) if (x != 0 or y != 0))
                if grid[i][j] == 1 and live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                elif grid[i][j] == 0 and live_neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = grid[i][j]
        grid = new_grid
        time.sleep(0.5)


game_of_life(100,10)
'''
"""
this simulates a car parkinglot
import time

def simulate_car_movement():
    parking_lot_size = 10
    parking_lot = ['.'] * parking_lot_size

    for i in range(parking_lot_size * 2):
        print(' '.join(parking_lot),end='\r')
        time.sleep(0.5)

        if i < parking_lot_size:
            parking_lot[i] = '*'
        else:
            parking_lot[i - parking_lot_size] = '.'

# Call the function to simulate car movement within the parking lot
simulate_car_movement()
"""









""" 
for .ipynb simulation
for i in range(1000):
    print(f"my name is {i}",end="\r")
    time.sleep(0)"""


