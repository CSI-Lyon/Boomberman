from tkinter import *

from Player import *
from Image import *

from utils import *
import time

import map

def keyPressed(event, canvas):
    global player

    key = event.keysym # Récupération de la touche
    #imgID = map.get(player.getPosX(), player.getPosY()).getID()
    #canvas.delete(imgID)

    player.go(key) # Déplacement du joueur

    if key == "Up":
        canvas.move(player.IDimage, 0, -35)
        print("up")
    elif key == "Down":
        canvas.move(player.IDimage, 0, +35)

    elif key == "Right":
        canvas.move(player.IDimage, +35, 0)
    elif key == "Left":
        canvas.move(player.IDimage, -35, 0)


def render(canvas):
    global player
    print("OK")

    casesID = [[0] * 19 for i in range(11)]
    for y in range(11):
        for x in range(19):
            img = Image("blocks", "grass")
            canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)

            case = map.get(x, y)

            if case == "GRASS" or case == "BEDROCK":
                img = Image("blocks", case)
            elif case == "GRASS+PLAYER_1":
                img = Image("blocks", "GRASS")
                imgJ1 = Image("skins/1", "down")
                player = Player(1, "Mateusz", 0, x, y)

            map.put(x, y, img)
            casesID[y][x] = canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)


    player.IDimage = canvas.create_image(xGridMin + player.posX*35 + 35/2 + 1, yGridMin + player.posX*35 + 35/2 + 1, image = imgJ1)
    print(player.IDimage, player.posX, player.posY)

def run(canvas, screenX, screenY, mode):
    # == Importation des images == #
    background = Image("", "background")
    left_band = Image("decor", "left_band")
    up_band = Image("decor", "up_band")

    #window.bind("<Button-1>")
    #window.bind("<Return>", bouton_entree)


    #winsound.PlaySound(None, winsound.SND_ASYNC)
    #winsound.PlaySound("son/02 One Above All.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    canvas.create_image(screenX/2, screenY/2, image = background)

    #coordonnées des bords de la grille de jeu
    xMin = screenX/2 - screenX/3
    xMax = screenX/2 + screenX/3
    yMin = screenY/2 - screenY/3
    yMax = screenY/2 + screenY/3

    gameGrid = canvas.create_rectangle(xMin,yMin, xMax,yMax, width=2, fill='white')

    canvas.create_image( xMin + screenX/13, screenY/2 +1, image = left_band)
    canvas.create_image( screenX/2 -1, yMin + screenY/17.5, image = up_band)

    #coordonnées des bords de la grille de jeu jouable
    global xGridMin, yGridMin
    xGridMin = (screenX - (screenX - xMin)) + 187
    xGridMax = (screenX - (screenX - xMax))
    yGridMin = (screenY - (screenY - yMin)) + 80
    yGridMax = (screenY - (screenY - yMax))
    #taille de la grille
    xLenGrid = xGridMax - xGridMin
    yLenGrid = yGridMax - yGridMin

    map.load() # Chargement de la map

    render(canvas)
    pass
    #window.mainloop()
