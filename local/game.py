from tkinter import *

from Player import *
from Image import *

def render():
    global grid, canvas, xGridMin, yGridMin
    for y in range(11):
        for x in range(19):
            case = grid[y][x]
            img = Image("blocks", case)

            if case == 0:
                canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)
            elif case == 1:
                canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = grass)

def run(window, screenX, screenY, mode):
    # == Importation des images == #
    background = Image("", "background")
    left_band = Image("decor", "left_band")
    up_band = Image("decor", "up_band")
    
    #winsound.PlaySound(None, winsound.SND_ASYNC)
    #winsound.PlaySound("son/02 One Above All.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    global canvas
    canvas = Canvas(window, bg="white", width = screenX, height = screenY, cursor="none")
    canvas.grid(row = 0, column = 0)
    
    canvas.create_image(screenX/2, screenY/2, image = background)

    xMin = screenX/2 - screenX/3
    xMax = screenX/2 + screenX/3
    yMin = screenY/2 - screenY/3
    yMax = screenY/2 + screenY/3
    
    gameGrid = canvas.create_rectangle(xMin,yMin, xMax,yMax, width=2, fill='white')


    canvas.create_image( xMin + screenX/13, screenY/2 +1, image = left_band)
    canvas.create_image( screenX/2 -1, yMin + screenY/17.5, image = up_band)

    global xGridMin, yGridMin
    xGridMin = (screenX - (screenX - xMin)) + 187
    xGridMax = (screenX - (screenX - xMax))
    yGridMin = (screenY - (screenY - yMin)) + 80
    yGridMax = (screenY - (screenY - yMax))

    xLenGrid = xGridMax - xGridMin
    yLenGrid = yGridMax - yGridMin

    if mode == 1:
        # Décodage de la grille
        global grid
        grid = open("grids/1.txt", "r").read().split("\n")

        for y in range(11):
            grid[y] = grid[y].split(" ")

        for y in range(11):
            for x in range(19):
                grid[y][x] = int(grid[y][x])

        render()

    window.mainloop()

