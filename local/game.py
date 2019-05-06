from tkinter import *

from Player import *
from Image import *

from utils import *
import time
import bombe
import map



def keyPressed(event, canvas):
    global player,imgJ1

    key = event.keysym # Récupération de la touche
    #imgID = map.get(player.getPosX(), player.getPosY()).getID()
    #canvas.delete(imgID)
    case = -1
    imgJ1 = Image("skins/1", "down")
    canvas.itemconfig(player.IDimage, image = imgJ1)
    
    if key == "Up" and player.posY >= 1:
        case = map.get2(player.posX, player.posY-1)
        if int(case) == 0 or int(case) == 10:
            imgJ1 = Image("skins/1", "up")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, 0, -35)
            player.posY -= 1
            map.set2(player.posX, player.posY+1, 0)
            map.set2(player.posX, player.posY, 10)

    elif key == "Down" and player.posY <= 9:
        case = map.get2(player.posX, player.posY+1)
        if int(case) == 0 or int(case) == 10:
            imgJ1 = Image("skins/1", "down")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, 0, +35)
            player.posY += 1
            map.set2(player.posX, player.posY-1, 0)
            map.set2(player.posX, player.posY, 10)
        
    elif key == "Right" and player.posX <= 17:
        case = map.get2(player.posX+1, player.posY)
        if int(case) == 0 or int(case) == 10:
            imgJ1 = Image("skins/1", "right")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, +35, 0)
            player.posX += 1
            map.set2(player.posX-1, player.posY, 0)
            map.set2(player.posX, player.posY, 10)
    
    elif key == "Left" and player.posX >= 1:
        case = map.get2(player.posX-1, player.posY)
        if int(case) == 0 or int(case) == 10:
            imgJ1 = Image("skins/1", "left")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, -35, 0)
            player.posX -= 1
            map.set2(player.posX+1, player.posY, 0)
            map.set2(player.posX, player.posY, 10)
    print(player.IDimage, case)

def render(window, canvas):
    global player,imgJ1, imgG

    casesID = [[0] * 19 for i in range(11)]
    img = Image("blocks", "grass")
    ghosts = []
    for y in range(11):
        for x in range(19):
            canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)

            case = map.get(x, y)

            if case == "GRASS" or case == "bedrock" or case == "stone":
                img2 = Image("blocks", case)
            elif case == "GRASS+PLAYER_1":
                img2 = Image("blocks", "GRASS")
                imgJ1 = Image("skins/1", "down")
                player = Player(1, "Mateusz", 0, x, y, 0, canvas)
            elif case == "GHOST":
                img2 = Image("blocks", "GRASS")
                imgG = Image("skins/ennemis", "ghost")
                ghost = Ennemi(0,canvas, x, y, True, player)
                ghosts.append(ghost)
            map.put(x, y, img2)
            
            casesID[y][x] = canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img2)

    
    player.IDimage = canvas.create_image(xGridMin + player.posX*35 + 35/2 + 1, yGridMin + player.posY*35 + 35/2 + 1, image = imgJ1)
   
    for i in ghosts:   
        i.imageID = canvas.create_image(xGridMin + i.posX*35 + 35/2 + 1, yGridMin + i.posY*35 + 35/2 + 1, image = imgG)
        i.canvas = canvas
        player.ennemisADetruire+=1
        i.start()

        
    window.bind("<space>", lambda event: bombe.putBomb(event, player, canvas, xGridMin, yGridMin, casesID))
    
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
