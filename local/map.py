from utils import *


grid = []
grid2 = []

def load():
    global grid
    file = open("grids/1.txt", "r")
    grid = file.read().split("\n")
    file.close()
    
    for y in range(11):
        grid[y] = grid[y].split(" ")

    for y in range(11):
        for x in range(19):
            grid[y][x] = decode(int(grid[y][x]))

def load2():
    global grid2
    grid2 = open("grids/1.txt", "r").read().split("\n")
    
    for y in range(11):
        grid2[y] = grid2[y].split(" ")

def get(x, y):
    return grid[y][x]

def get2(x, y):
    return grid2[y][x]

def set2(x, y, value):
    global grid2
    grid2[x][y] = value

def put(x, y, ID):
    global grid
    grid[y][x] = ID
