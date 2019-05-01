from tkinter import *

from Player import *
from Image import *

from utils import *
import time
import bombe
import map

def keyPressed(event, canvas):
    global player

    key = event.keysym # Récupération de la touche
    #imgID = map.get(player.getPosX(), player.getPosY()).getID()
    #canvas.delete(imgID)

    player.go(key, canvas) # Déplacement du joueur
    
    #if key == "Up" and yGridMin <= canvas.coords(player.IDimage)[1] - 35:
    #    print(player.posX, player.posY-1, map.get2(player.posX, player.posY-1))
    #    if map.get2(player.posX, player.posY-1) == 0:
            
    #elif key == "Down" and yGridMax >= canvas.coords(player.IDimage)[1] + 35:
        
    #elif key == "Right" and xGridMax >= canvas.coords(player.IDimage)[0] + 35:
       
    #elif key == "Left" and xGridMin <= canvas.coords(player.IDimage)[0] -35:
        


def render(window, canvas):
    global player

    casesID = [[0] * 19 for i in range(11)]
    for y in range(11):
        for x in range(19):
            img = Image("blocks", "grass")
            canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)

            case = map.get(x, y)

            if case == "GRASS" or case == "bedrock" or case == "stone":
                img = Image("blocks", case)
            elif case == "GRASS+PLAYER_1":
                img = Image("blocks", "GRASS")
                imgJ1 = Image("skins/1", "down")
                player = Player(1, "Mateusz", 0, x, y)

            map.put(x, y, img)
            casesID[y][x] = canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)


    player.IDimage = canvas.create_image(xGridMin + player.posX*35 + 35/2 + 1, yGridMin + player.posX*35 + 35/2 + 1, image = imgJ1)
    window.bind("<space>", lambda event: bombe.putBomb(event, player, canvas, xGridMin, yGridMin))

    window.mainloop()

def run(window, canvas, screenX, screenY, mode):
    # == Importation des images == #
    background = Image("", "background")
    left_band = Image("decor", "left_band")
    up_band = Image("decor", "up_band")

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
    global xGridMin, yGridMin, xGridMax, yGridMax
    xGridMin = (screenX - (screenX - xMin)) + 187
    xGridMax = (screenX - (screenX - xMax))
    yGridMin = (screenY - (screenY - yMin)) + 80
    yGridMax = (screenY - (screenY - yMax))

    #taille de la grille
    xLenGrid = xGridMax - xGridMin
    yLenGrid = yGridMax - yGridMin

    map.load() # Chargement de la map
    map.load2() #2eme tableau de la map

    render(window, canvas)
