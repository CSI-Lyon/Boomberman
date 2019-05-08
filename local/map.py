from utils import *


grid = []
grid2 = []

#lit la grille du fichier texte
def load():
    global grid
    file = open("grids/1.txt", "r")
    grid = file.read().split("\n")
    file.close()

    #découpe le tout pour avoir une valeur par case
    for y in range(11):
        grid[y] = grid[y].split(" ")

    #décode pour faire correspondre le 0 pour la terre par exemple
    for y in range(11):
        for x in range(19):
            grid[y][x] = decode(int(grid[y][x]))

    return 0

def load2():
    global grid2
    file = open("grids/1.txt", "r")
    grid2 = file.read().split("\n")
    file.close()

    #découpe le tout pour avoir une valeur par case
    for y in range(11):
        grid2[y] = grid2[y].split(" ")

    return 0

#retourne la valeure contenue dans la grille1
def get(x, y):
    return grid[y][x]

#retourne la valeure contenue dans la grille2
def get2(x, y):
    return grid2[y][x]

#définie une valeur pour la case par exemple, on change du 0 ŕ 10 car le joueur va dans cette case
#0 terre, 10 joueur
def set2(x, y, value):
    global grid2
    grid2[y][x] = int(value)
    return 0

def put(x, y, ID):
    global grid
    grid[y][x] = ID
    return 0
