from tkinter import *
from Player import *
from Image import *
from utils import *
import time
import bombe
import map
import getpass
import socket
import threading
import sys

#variables 
name = getpass.getuser()
print(name)
vie = 2
data = ""
ip = "192.168.0.12"
port = 12345

#taille de l'écran
screenX = 1280
screenY = 700

#taille du texte
fontSize = 25
fontName = "Arial Black"
fontColor = "#2A4B7C"

def connection(host, portEnvoi):
    global connReception, connEnvoi
    portReception = portEnvoi + 1
    connEnvoi = socket.socket()
    connReception = socket.socket()

    connEnvoi.connect((host, portEnvoi))
    connReception.connect((host, portReception))

def processMessages(connReception, connEnvoi):
    print("process start")
    while True:
        #try:
        data = connReception.recv(256)
        data = data.decode("utf-8")
        data = data.split(",")
        print(data)
        if data[0] == "Up" or data[0] == "Down" or data[0] == "Left" or data[0] == "Right":
            if int(data[1]) == 1:
                player.move(data[0])
            elif int(data[1]) == 2:
                player2.move(data[0])

        elif data[0] == "space":
            if int(data[1]) == 1:
                bombe.putBomb(player,player2, canvasGlobal, xGridMin, yGridMin, casesID, modeGlobal)
            elif int(data[1]) == 2:
                bombe.putBomb(player2,player, canvasGlobal, xGridMin, yGridMin, casesID, modeGlobal)
        #except:
            #pass
##            connEnvoi.close()
##            connReception.close()
##            print("Connection closed by")
##            # Quit the thread.
##            sys.exit()


#On récupčre le texte des champs des paramčtres du jeu
def getInfos():
    global ip, port, name, vie
    name = Nom.get()
    vie = Vie.get()
    ip = Ip.get()
    port = int(Port.get())
    print(name, vie, ip, port)

def parametres():
    settings = Tk()
    settings.title("Paramètres")
    settings.geometry("350x330+300+200")
    settings.resizable(False, False)

    global Nom, Ip, Vie, Port

    #Création d'élèments
    bienvenue = Label(settings, text='Paramètres du jeu\n', font = "-size 12 -weight bold")
    nom = Label(settings, text='Nom :\n', font = "-size 11")
    vie = Label(settings, text='Vie :', font = "-size 11")
    Nom = Entry(settings, width=15, font = "-size 11")
    Vie = Spinbox(settings, from_=1, to=10, width=3)
    #width, height
    titre = Label(settings, text='\n\nMutltijoueur\n', font = "-size 11 -weight bold")
    ip = Label(settings, text='Ip :', font = "-size 11")
    port = Label(settings, text='\nPort :\n', font = "-size 11")
    
    Ip = Entry(settings, width=14, font = "-size 11")
    Port = Spinbox(settings, from_=256, to=65536, width=5)
    appliquer = ttk.Button(settings, text= 'Appliquer', command = getInfos)
    confirmer = ttk.Button(settings, text = 'Confirmer', command = settings.destroy)
    
    
    #Répartition des différents élements
    bienvenue.grid(row = 0, column = 0, padx = 120, pady = 10, sticky = W, columnspan = 1)
    nom.grid(row = 2, column = 0, sticky = W, padx = 20)
    vie.grid(row = 3, column = 0, sticky = W, padx = 20)
    Nom.grid(row = 2, column = 0, padx = 120, sticky = W)
    Vie.grid(row = 3, column = 0, padx = 120, sticky = W)

    titre.grid(row = 5, column = 0, sticky = W, padx = 20, columnspan = 1)
    ip.grid(row = 7, column = 0, sticky = W, padx = 20)
    port.grid(row = 8, column = 0, sticky = W, padx = 20)
    Ip.grid(row=7, column = 0, padx = 100, sticky = W)
    Port.grid(row=8, column = 0, padx = 100, sticky = W)
    
    #Bouton de validation / confirmation
    appliquer.grid(row = 13, column = 0, padx = 150, sticky = W)
    confirmer.grid(row = 13, column = 0, padx = 250)
  
    settings.mainloop()


def keyPressed(event):
    key = event.keysym # Récupération de la touche
    if modeGlobal == "multijoueur":
        data = key + "," + str(ID)
        print(data)
        connEnvoi.sendall(bytes(data, "utf-8"))

    else:
        if key == "Up" or key == "Down" or key == "Left" or key == "Right":
            player.move(key)
        elif key == "space":
            bombe.putBomb(player,0, canvasGlobal, xGridMin, yGridMin, casesID, modeGlobal)


#affiche les cases de la grille du jeu
def render(window, canvas, xMax, yMin, mode):
    global player,player2, imgJ1,imgJ2, imgG, casesID

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
                if modeGlobal != "multijoueur":
                    player = Player(1, name, 0, x, y, 0, canvas,0, int(vie))
                else:
                    player = Player(1, namesSplited[0], 0, x, y, 0, canvas,0, int(vie))
                    
                canvas.create_text(xGridMin - screenX/13, yGridMin + screenY/20, \
                                   font=(fontName, int(fontSize/1.5)), text='Joueur 1', fill="white")
                canvas.create_text(xGridMin - screenX/13, yGridMin + screenY/10, \
                                   font=(fontName, int(fontSize)), text=player.name, fill="white")

                player.textVieID = canvas.create_text(xMax - screenX/17, yMin + screenY/20, \
                                   font=(fontName, int(fontSize)), text=player.vie, fill="white")

            elif case == "GRASS+PLAYER_2":
                img2 = Image("blocks", "GRASS")
                imgJ2 = Image("skins/2", "up")
                player2 = Player(2, namesSplited[1], 0, x, y, 0, canvas, 0, int(vie))
                
                canvas.create_text(xGridMin - screenX/13, yGridMin + screenY/7, \
                                   font=(fontName, int(fontSize/1.5)), text='Joueur 2', fill="white")
                canvas.create_text(xGridMin - screenX/13, yGridMin + screenY/5, \
                                   font=(fontName, int(fontSize)), text=player.name, fill="white")

            elif case == "GHOST":
                img2 = Image("blocks", "GRASS")
                imgG = Image("skins/ennemis", "ghost")
                ghost = Ennemi(0,canvas, x, y, True, player)
                ghosts.append(ghost)
            map.put(x, y, img2)
            
            casesID[y][x] = canvas.create_image(xGridMin + x*35 + 35/2 + 1, \
                                                yGridMin + y*35 + 35/2 + 1, image = img2)

    
    player.IDimage = canvas.create_image(xGridMin + player.posX*35 + 35/2 + 1, \
                                         yGridMin + player.posY*35 + 35/2 + 1, image = imgJ1)
    if modeGlobal == "multijoueur":
        player2.IDimage = canvas.create_image(xGridMin + player2.posX*35 + 35/2 + 1, \
                                              yGridMin + player2.posY*35 + 35/2 + 1, image = imgJ2)
    
    #pour chaque fantôme, on ajoute l'image du fantôme et on execute ses actions grâce ŕ un threat
    for i in ghosts:   
        i.imageID = canvas.create_image(xGridMin + i.posX*35 + 35/2 + 1, yGridMin + i.posY*35 + 35/2 + 1, image = imgG)
        i.canvas = canvas
        player.ennemisADetruire+=1
        i.start()

    
    #Touche éspace = poser une bombe
    window.bind("<space>", keyPressed)

    if modeGlobal == "multijoueur":
        listener = threading.Thread(target=processMessages, args=(connReception, connEnvoi))
        listener.start()
    
    window.mainloop()

def run(window, canvas, screenX, screenY, mode):
    global vie, namesSplited, ID, modeGlobal, canvasGlobal
    # == Importation des images == #
    background = Image("", "background")
    left_band = Image("decor", "left_band")
    up_band = Image("decor", "up_band")
    heart = Image("decor", "heart")

    modeGlobal = mode
    canvasGlobal = canvas

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
    canvas.create_image(xMax - screenX/10, yMin + screenY/20, image = heart)

    #coordonnées des bords de la grille de jeu jouable
    global xGridMin, yGridMin, xGridMax, yGridMax
    xGridMin = (screenX - (screenX - xMin)) + 187
    xGridMax = (screenX - (screenX - xMax))
    yGridMin = (screenY - (screenY - yMin)) + 80
    yGridMax = (screenY - (screenY - yMax))

    #taille de la grille
    xLenGrid = xGridMax - xGridMin
    yLenGrid = yGridMax - yGridMin

    if mode == "un joueur":
        map.load("1.txt") # Chargement de la map
        map.load2("1.txt") #2eme tableau de la map
    elif mode == "multijoueur":
        map.load("2.txt") # Chargement de la map
        map.load2("2.txt") #2eme tableau de la map
        vie = 2
        connection(ip, port)

        #on attend tant que le serveur ne nous a pas "dit ok"
        connEnvoi.sendall(bytes(name, "utf-8"))
        ID = connReception.recv(8)
        ID = int(ID.decode("utf-8"))
        names = connReception.recv(256)
        names = names.decode("utf-8")
        namesSplited = names.split(",")

    render(window, canvas, xMax, yMin, mode)

