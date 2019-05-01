from tkinter import *
from tkinter import messagebox
#import winsound
import time

import gamer

from Image import *


screenX = 1280
screenY = 700

fontSize = 25
fontName = "Bauhaus 93"
fontColor = "#2A4B7C"

etat = "menu principal"
tableauBottom = [0] * 10
tableauText = [0] * 10

x1, y1 = screenX/1.3, screenY/2.8
x4, y4 = screenX/1.3, screenY/1.17


window = Tk()

#importation des images 
logo = Image("", "logo")
imageBG = Image("", "background")
imageFondTitre = PhotoImage (file = "images/title.png")
bottomImage = PhotoImage(file = "images/button.png")
bottomImage2 = PhotoImage (file = "images/exit_button.png")
bottomImageSelection = PhotoImage (file = "images/selected_button.png")
bottomImageSelection2 = PhotoImage (file = "images/selected_exit_button.png")

def bottom(event):



    
    global etat
    if etat == "menu principal":
        if event.x > (screenX/1.3 - 188) and event.x < (screenX/1.3 + 188) and event.y > (screenY/2.8 - 33) and event.y < (screenY/2.8 + 33):
            etat = "nouvelle partie"
            nouvelle_partie()
        elif event.x > x4 - 188 and event.x < x4 + 188 and event.y > y4 - 33 and event.y < y4 + 33:
            callback()
            
    elif etat == "nouvelle partie":
        if event.x > screenX/2 - 188 and event.x < screenX/2 + 188 and event.y > screenY/1.8 - 33 and event.y < screenY/1.8 + 33:
            etat = "jeu"
            jeu("un joueur")
        elif event.x > screenX/4.5 - 188 and event.x < screenX/4.5 + 188 and event.y > screenY/1.17 - 33 and event.y < screenY/1.17 + 33:
            etat = "menu principal"
            menu_principal()

    elif etat == "jeu":
        #jeuCanvas.create_image(event.x, event.y, image = grass)
        pass
        
    print(event.x, event.y)


"""

Début des fonctions de sélection

"""

def bottom_bleu1(event, text, x, y, boutonID, image):
    if image == 0:
        tableauBottom[boutonID] = main_canvas.create_image(x, y, image = bottomImageSelection)
    elif image == 1:
        tableauBottom[boutonID] = main_canvas.create_image(x, y, image = bottomImageSelection2)
    tableauText[boutonID] = main_canvas.create_text (x, y, font=(fontName, fontSize), text=text, fill=fontColor)
    main_canvas.tag_bind(tableauBottom[boutonID], "<Leave>", lambda event: bottom_remove_bleu1(event, text=text, x = x, y = y, boutonID = boutonID, image = image))

def bottom_bleu2(event, text, x, y, boutonID, image):
    if image == 0:
        tableauBottom[boutonID] = nouvellePartieCanvas.create_image(x, y, image = bottomImageSelection)
    elif image == 1:
        tableauBottom[boutonID] = nouvellePartieCanvas.create_image(x, y, image = bottomImageSelection2)
    tableauText[boutonID] = nouvellePartieCanvas.create_text (x, y, font=(fontName, fontSize), text=text, fill=fontColor)
    nouvellePartieCanvas.tag_bind(tableauBottom[boutonID], "<Leave>", lambda event: bottom_remove_bleu2(event, text=text, x = x, y = y, boutonID = boutonID, image = image))

    

def bottom_remove_bleu1(event, text, x, y, boutonID, image):
    if image == 0:
        tableauBottom[boutonID] = main_canvas.create_image(x, y, image = bottomImage)
    elif image == 1:
        tableauBottom[boutonID] = main_canvas.create_image(x, y, image = bottomImage2)
    tableauText[boutonID] = main_canvas.create_text (x, y, font=(fontName, fontSize), text=text, fill=fontColor)
    main_canvas.tag_bind(tableauBottom[boutonID], "<Enter>", lambda event: bottom_bleu1(event, text=text, x = x, y = y, boutonID = boutonID, image = image))
    main_canvas.tag_bind(tableauText[boutonID], "<Enter>", lambda event: bottom_bleu1(event, text=text, x = x, y = y, boutonID = boutonID, image = image))

def bottom_remove_bleu2(event, text, x, y, boutonID, image):
    if image == 0:
        tableauBottom[boutonID] = nouvellePartieCanvas.create_image(x, y, image = bottomImage)
    elif image == 1:
        tableauBottom[boutonID] = nouvellePartieCanvas.create_image(x, y, image = bottomImage2)
    tableauText[boutonID] = nouvellePartieCanvas.create_text (x, y, font=(fontName, fontSize), text=text, fill=fontColor)
    nouvellePartieCanvas.tag_bind(tableauBottom[boutonID], "<Enter>", lambda event: bottom_bleu2(event, text=text, x = x, y = y, boutonID = boutonID, image = image))
    nouvellePartieCanvas.tag_bind(tableauText[boutonID], "<Enter>", lambda event: bottom_bleu2(event, text=text, x = x, y = y, boutonID = boutonID, image = image))



"""

Fin des fonctions de sélection

"""

def mode_developpeur(event):
    grilleJeu = jeuCanvas.create_rectangle(xMin,yMin, xMax,yMax, width =2, fill='white')
    window.title("Boomberman - Mode développeur")
    etat = "mode développeur"
    

def callback():
    if messagebox.askokcancel("Quit", "Voulez-vous vraiment quitter le jeu?"):
        window.destroy()
        #winsound.PlaySound(None, winsound.SND_ASYNC)
    else:
        try:
            bottom_remove_bleu1(1, text="Quitter", x = screenX/1.3, y = screenY/1.17, boutonID = 3, image = 1)
        except:
            print()

def jeu(mode):
    nouvellePartieCanvas.destroy()
    mode = 1
    
    #winsound.PlaySound(None, winsound.SND_ASYNC)
    #winsound.PlaySound("son/02 One Above All.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    gamer.run(window, screenX, screenY, mode)

def nouvelle_partie():
    global nouvellePartieCanvas
    main_canvas.destroy()

    nouvellePartieCanvas = Canvas(window, bg="white", width = screenX, height = screenY)
    nouvellePartieCanvas.grid(row = 0, column = 0)

    nouvellePartieCanvas.create_image(screenX/2, screenY/2, image = imageBG)
    nouvellePartieCanvas.create_image(screenX/3, screenY/6, image = logo)
    nouvellePartieCanvas.create_image (screenX/2, screenY/2.7, image = imageFondTitre)
    
    bottom5 = nouvellePartieCanvas.create_image(screenX/2, screenY/1.8, image = bottomImage)
    bottom6 = nouvellePartieCanvas.create_image(screenX/2, screenY/1.45, image = bottomImage)
    bottom7 = nouvellePartieCanvas.create_image(screenX/4.5, screenY/1.17, image = bottomImage2)

    nouvellePartieCanvas.create_text (screenX/2, screenY/2.7, font=(fontName, int(fontSize*1.5)), text='Nouvelle Partie', fill="white")
    nouvellePartieCanvas.create_text (screenX/2, screenY/1.8, font=(fontName, fontSize), text='Un joueur', fill=fontColor)
    nouvellePartieCanvas.create_text (screenX/2, screenY/1.45, font=(fontName, fontSize), text='Multijoueur', fill=fontColor)
    nouvellePartieCanvas.create_text (screenX/4.5, screenY/1.17, font=(fontName, fontSize), text='<---- Retour', fill=fontColor)

    nouvellePartieCanvas.tag_bind(bottom5, "<Enter>", lambda event: bottom_bleu2(event, text="Un joueur", x = screenX/2, y = screenY/1.8, boutonID = 4, image = 0))
    nouvellePartieCanvas.tag_bind(bottom6, "<Enter>", lambda event: bottom_bleu2(event, text="Multijoueur", x = screenX/2, y = screenY/1.45, boutonID = 5, image = 0))
    nouvellePartieCanvas.tag_bind(bottom7, "<Enter>", lambda event: bottom_bleu2(event, text="<---- Retour", x = screenX/4.5, y = screenY/1.17, boutonID = 6, image = 1))
    

def menu_principal():
    try:
        nouvellePartieCanvas.destroy()
    except:
        pass
    
    global main_canvas
    main_canvas = Canvas(window, bg="white", width = screenX, height = screenY)
    main_canvas.grid(row = 0, column = 0)
    #main_canvas.pack()

    #insertion d'images
    main_canvas.create_image(screenX/2, screenY/2, image = imageBG)
    main_canvas.create_image(screenX/3, screenY/6, image = logo)
    bottom1 = main_canvas.create_image(x1, y1, image = bottomImage)
    bottom2 = main_canvas.create_image(screenX/1.3, screenY/2, image = bottomImage)
    bottom3 = main_canvas.create_image(screenX/1.3, screenY/1.55556, image = bottomImage)
    bottom4 = main_canvas.create_image(x4, y4, image = bottomImage2)

    #insertion du texte
    main_canvas.create_text (screenX/1.3, screenY/2.8, font=(fontName, fontSize), text='Nouvelle Partie', fill=fontColor)
    main_canvas.create_text (screenX/1.3, screenY/2, font=(fontName, fontSize), text='Paramètres', fill=fontColor)
    main_canvas.create_text (screenX/1.3, screenY/1.55556, font=(fontName, fontSize), text='Score', fill=fontColor)
    main_canvas.create_text (screenX/1.3, screenY/1.17, font=(fontName, fontSize), text='Quitter', fill=fontColor)

    #Si la sourie rentre dans un des images -> animation de sélection
    #stackoverflow, event not defined. Sinon rentre
    main_canvas.tag_bind(bottom1, "<Enter>", lambda event: bottom_bleu1(event, text="Nouvelle Partie", x = screenX/1.3, y = screenY/2.8, boutonID = 0, image = 0))
    main_canvas.tag_bind(bottom2, "<Enter>", lambda event: bottom_bleu1(event, text="Paramètres", x = screenX/1.3, y = screenY/2, boutonID = 1, image = 0))
    main_canvas.tag_bind(bottom3, "<Enter>", lambda event: bottom_bleu1(event, text="Score", x = screenX/1.3, y = screenY/1.55556, boutonID = 2, image = 0))
    main_canvas.tag_bind(bottom4, "<Enter>", lambda event: bottom_bleu1(event, text="Quitter", x = screenX/1.3, y = screenY/1.17, boutonID = 3, image = 1))


def main():
    #Plein écran :
    #window.attributes('-fullscreen', True)
    resolution = str(screenX)+"x"+str(screenY)
    
    window.title("Boomberman")
    window.geometry(resolution)
    window.resizable(False, False)
    window.iconbitmap('images/Bomberman-icon.ico')

    #Demande si on veut vraiment fermer la fenêtre
    window.protocol("WM_DELETE_WINDOW", callback)

    #Récupération des différentes touches
    window.bind("<Button-1>", bottom)

    menu_principal()
    window.mainloop()


#winsound.PlaySound("son/01 Unleashed.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


main()
