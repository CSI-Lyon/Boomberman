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
    case = -1
    imgJ1 = Image("skins/1", "down")
    canvas.itemconfig(player.IDimage, image = imgJ1)

    #si l'utilisateur appuie sur la touche de haut
    if key == "Up" and player.posY >= 1:
        case = map.get2(player.posX, player.posY-1)
        if int(case) == 0 or int(case) == 50:
            #s'il y a un fantome (ennemi), alors il perd une vie
            if int(case) == 50:
                player.vie-=1

            imgJ1 = Image("skins/1", "up")
            #on remplace l'image du joueur par une image d'un personnage allant en haut
            canvas.itemconfig(player.IDimage, image = imgJ1)
            #on le fait bouger
            canvas.move(player.IDimage, 0, -35)
            player.posY -= 1
            #on remplace les bons ID pour chaque case
            if map.get2(player.posX, player.posY+1) == 10:
                map.set2(player.posX, player.posY+1, 0)
            map.set2(player.posX, player.posY, 10)


    #
    #   Pour bas, droite et gauche, męme fonctinonement que celui de la touche en haut
    #
    
    elif key == "Down" and player.posY <= 9:
        case = map.get2(player.posX, player.posY+1)
        if int(case) == 0 or int(case) == 50:
            if int(case) == 50:
                player.vie-=1
                
            imgJ1 = Image("skins/1", "down")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, 0, +35)
            player.posY += 1
            if map.get2(player.posX, player.posY-1) == 10:
                map.set2(player.posX, player.posY-1, 0)
            map.set2(player.posX, player.posY, 10)
        
    elif key == "Right" and player.posX <= 17:
        case = map.get2(player.posX+1, player.posY)
        if int(case) == 0 or int(case) == 50:
            if int(case) == 50:
                player.vie-=1
                
            imgJ1 = Image("skins/1", "right")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, +35, 0)
            player.posX += 1
            if map.get2(player.posX-1, player.posY) == 10:
                map.set2(player.posX-1, player.posY, 0)
            map.set2(player.posX, player.posY, 10)
    
    elif key == "Left" and player.posX >= 1:
        case = map.get2(player.posX-1, player.posY)
        if int(case) == 0 or int(case) == 50:
            if int(case) == 50:
                player.vie-=1
                
            imgJ1 = Image("skins/1", "left")
            canvas.itemconfig(player.IDimage, image = imgJ1)
            canvas.move(player.IDimage, -35, 0)
            player.posX -= 1
            if map.get2(player.posX+1, player.posY) == 10:
                map.set2(player.posX+1, player.posY, 0)
            map.set2(player.posX, player.posY, 10)

#affiche les cases de la grille du jeu
def render(window, canvas):
    global player,imgJ1, imgG

    casesID = [[0] * 19 for i in range(11)]
    img = Image("blocks", "grass")
    #tableau d'ennemis
    ghosts = []
    #pour chaque case
    for y in range(11):
        for x in range(19):
            canvas.create_image(xGridMin + x*35 + 35/2 + 1, yGridMin + y*35 + 35/2 + 1, image = img)

            case = map.get(x, y)
            #attribuer la variable de l'image correspondante au modčle
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
    #pour chaque fantôme, on ajoute l'image du fantôme et on execute ses actions grâce ŕ un threat
    for i in ghosts:   
        i.imageID = canvas.create_image(xGridMin + i.posX*35 + 35/2 + 1, yGridMin + i.posY*35 + 35/2 + 1, image = imgG)
        i.canvas = canvas
        player.ennemisADetruire+=1
        i.start()

    #Touche éspace = poser une bombe
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

    #design de la grille du jeu
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

