from tkinter import *

from Player import *
from Image import *

from utils import *

import map

def keyPressed(event):
    global player

    key = event.keysym # Récupération de la touche
    imgID = map.get(player.getPosX(), player.getPosY()).getID()
    canvas.delete(imgID)

    player.go(key) # Déplacement du joueur

    canvas.move(imgID, +35, 0)

def render():
    global grid, canvas, xGridMin, yGridMin
    print("OK")

    for y in range(11):
        for x in range(19):
            case = map.get(x, y)

            if case == "GRASS" or case == "BEDROCK":
                img = Image("blocks", case)
            else:
                img = Image("skins/1", "down")

            map.put(x, y, img)
            canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)

def run(window, screenX, screenY, mode):
    # == Importation des images == #
    background = Image("", "background")
    left_band = Image("decor", "left_band")
    up_band = Image("decor", "up_band")

    #window.bind("<Button-1>")
    #window.bind("<Return>", bouton_entree)
    window.bind("<Up>", lambda event: keyPressed(event))
    window.bind("<Right>", lambda event: keyPressed(event))
    window.bind("<Down>", lambda event: keyPressed(event))
    window.bind("<Left>", lambda event: keyPressed(event))

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

    map.load() # Chargement de la map

    global player
    player = Player(1, "Juan")

    render()

    window.mainloop()
