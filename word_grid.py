import random
def init():
    global grid_size
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)

def make_grid(grid_size):
    grid = []
    for _ in range(grid_size):
        line = []
        for _ in range(grid_size):
            line.append(random.randint(97, 122))
        grid.append(list(map(chr, line)))
    return grid

def print_grid(grid):
    for x in grid:
        print(','.join(x))

def main():
    init()
    print_grid(make_grid(grid_size))

main()