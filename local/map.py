from utils import *

grid = []

def load():
    global grid
    grid = open("grids/1.txt", "r").read().split("\n")

    for y in range(11):
        grid[y] = grid[y].split(" ")

    for y in range(11):
        for x in range(19):
            grid[y][x] = decode(int(grid[y][x]))

def get(x, y):
    global grid
    return grid[y][x]

def put(x, y, id):
    global grid
    grid[y][x] = id
