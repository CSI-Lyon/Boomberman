from tkinter import *
from tkinter import messagebox
import winsound

fontSize = 25
fontName = "Bauhaus 93"
fontColor = "#f23933"
etat = "menu principal"
tableauBottom = [0] * 10
tableauText = [0] * 10

"""
menu_principale
nouvelle_partie
paramètres
score
jeu
"""

class Personnage:
    def __init__(self, name, playerID, nbBombs):
        self.name = name
        self.playerID = playerID
        self.nbBombs = 4

def bouton_entree(event):
    print("enter")
    

def bouton_up(event):
    print("up")

def bouton_down(event):
    print("down")

def bouton_right(event):
    print("right")

def bouton_left(event):
    print("left")

def bottom(event):
    global etat
    if etat == "menu principal":
        if event.x > (1280/1.3 - 188) and event.x < (1280/1.3 + 188) and event.y > (700/2.8 - 33) and event.y < (700/2.8 + 33):
            etat = "nouvelle partie"
            nouvelle_partie()
    elif etat == "nouvelle partie":
        if event.x > 1280/4.5 - 188 and event.x < 1280/4.5 + 188 and event.y > 700/1.17 - 33 and event.y < 700/1.17 + 33:
            etat = "menu principal"
            menu_principal()
        
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



def callback():
    if messagebox.askokcancel("Quit", "Voulez-vous vraiment quitter le jeu?"):
        window.destroy()
        winsound.PlaySound(None, winsound.SND_ASYNC)

def nouvelle_partie():
    global nouvellePartieCanvas
    main_canvas.destroy()

    nouvellePartieCanvas = Canvas(window, bg="white", width = 1280, height = 700)
    nouvellePartieCanvas.grid(row = 0, column = 0)

    nouvellePartieCanvas.create_image(1280/2, 700/2, image = imageBG)
    nouvellePartieCanvas.create_image(1280/3, 700/6, image = logo)
    nouvellePartieCanvas.create_image (1280/2, 700/2.7, image = imageFondTitre)
    
    bottom5 = nouvellePartieCanvas.create_image(1280/2, 700/1.8, image = bottomImage)
    bottom6 = nouvellePartieCanvas.create_image(1280/2, 700/1.45, image = bottomImage)
    bottom7 = nouvellePartieCanvas.create_image(1280/4.5, 700/1.17, image = bottomImage2)

    nouvellePartieCanvas.create_text (1280/2, 700/2.7, font=(fontName, int(fontSize*1.5)), text='Nouvelle Partie', fill="white")
    nouvellePartieCanvas.create_text (1280/2, 700/1.8, font=(fontName, fontSize), text='Un joueur', fill=fontColor)
    nouvellePartieCanvas.create_text (1280/2, 700/1.45, font=(fontName, fontSize), text='Multijoueur', fill=fontColor)
    nouvellePartieCanvas.create_text (1280/4.5, 700/1.17, font=(fontName, fontSize), text='<---- Retour', fill=fontColor)

    nouvellePartieCanvas.tag_bind(bottom5, "<Enter>", lambda event: bottom_bleu2(event, text="Un joueur", x = 1280/2, y = 700/1.8, boutonID = 4, image = 0))
    nouvellePartieCanvas.tag_bind(bottom6, "<Enter>", lambda event: bottom_bleu2(event, text="Multijoueur", x = 1280/2, y = 700/1.45, boutonID = 5, image = 0))
    nouvellePartieCanvas.tag_bind(bottom7, "<Enter>", lambda event: bottom_bleu2(event, text="<---- Retour", x = 1280/4.5, y = 700/1.17, boutonID = 6, image = 1))
    

def menu_principal():
    try:
        nouvellePartieCanvas.destroy()
    except:
        print("ok")
    
    global main_canvas
    global logo, imageBG, imageFondTitre, bottomImage, bottomImage2, bottomImageSelection, bottomImageSelection2
    main_canvas = Canvas(window, bg="white", width = 1280, height = 700)
    main_canvas.grid(row = 0, column = 0)

    #importation des images 
    logo = PhotoImage(file = "images/Boomberman.png")
    imageBG = PhotoImage(file = "images/background.png")
    imageFondTitre = PhotoImage (file = "images/titre.png")
    bottomImage = PhotoImage(file = "images/Bottom.png")
    bottomImage2 = PhotoImage (file = "images/Bottom_exit.png")
    bottomImageSelection = PhotoImage (file = "images/Bottom_selection.png")
    bottomImageSelection2 = PhotoImage (file = "images/Bottom_exit_selection.png")

    #insertion d'images
    main_canvas.create_image(1280/2, 700/2, image = imageBG)
    main_canvas.create_image(1280/3, 700/6, image = logo)
    bottom1 = main_canvas.create_image(1280/1.3, 700/2.8, image = bottomImage)
    bottom2 = main_canvas.create_image(1280/1.3, 700/2, image = bottomImage)
    bottom3 = main_canvas.create_image(1280/1.3, 700/1.55556, image = bottomImage)
    bottom4 = main_canvas.create_image(1280/1.3, 700/1.17, image = bottomImage2)

    #insertion du texte
    main_canvas.create_text (1280/1.3, 700/2.8, font=(fontName, fontSize), text='Nouvelle Partie', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/2, font=(fontName, fontSize), text='Paramètres', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/1.55556, font=(fontName, fontSize), text='Score', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/1.17, font=(fontName, fontSize), text='Quitter', fill=fontColor)

    #Si la sourie rentre dans un des images -> animation de sélection
    main_canvas.tag_bind(bottom1, "<Enter>", lambda event: bottom_bleu1(event, text="Nouvelle Partie", x = 1280/1.3, y = 700/2.8, boutonID = 0, image = 0))
    main_canvas.tag_bind(bottom2, "<Enter>", lambda event: bottom_bleu1(event, text="Paramètres", x = 1280/1.3, y = 700/2, boutonID = 1, image = 0))
    main_canvas.tag_bind(bottom3, "<Enter>", lambda event: bottom_bleu1(event, text="Score", x = 1280/1.3, y = 700/1.55556, boutonID = 2, image = 0))
    main_canvas.tag_bind(bottom4, "<Enter>", lambda event: bottom_bleu1(event, text="Quitter", x = 1280/1.3, y = 700/1.17, boutonID = 3, image = 1))


def main():
    global window
    
    window = Tk()
    window.title("Boomberman")
    window.geometry("1280x700")
    window.resizable(False, False)
    window.iconbitmap('images/Bomberman-icon.ico')

    #Demande si on veut vraiment fermer la fenêtre
    window.protocol("WM_DELETE_WINDOW", callback)

    #Récupération des différentes touches
    window.bind("<Return>", bouton_entree)
    window.bind("<Up>",bouton_up)
    window.bind("<Down>",bouton_down)
    window.bind("<Right>",bouton_right)
    window.bind("<Left>",bouton_left)
    window.bind("<Button-1>", bottom)

    menu_principal()
    
    window.mainloop()


#winsound.PlaySound("son/01 Unleashed.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


main()

pers1 = Personnage("Mateusz", 1, 4)
