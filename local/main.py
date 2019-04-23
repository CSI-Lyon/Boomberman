from tkinter import *
from tkinter import messagebox
import winsound

fontSize = 25
fontName = "Bauhaus 93"
fontColor = "#f23933"

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
    print(event.x, event.y)


"""

Début des fonctions de sélection

"""

def bottom_bleu1(event):
    bottom1_1 = main_canvas.create_image(1280/1.3, 700/2.8, image = bottomImageSelection)
    text1_1 = main_canvas.create_text (1280/1.3, 700/2.8, font=(fontName, fontSize), text='Nouvelle Partie', fill=fontColor)
    main_canvas.tag_bind(bottom1_1, "<Leave>", bottom_remove_bleu1)
    main_canvas.tag_bind(text1_1, "<Leave>", bottom_remove_bleu1)

def bottom_bleu2(event):
    bottom2_1 = main_canvas.create_image(1280/1.3, 700/2, image = bottomImageSelection)
    text2_1 = main_canvas.create_text (1280/1.3, 700/2, font=(fontName, fontSize), text='Paramètres', fill=fontColor)
    main_canvas.tag_bind(bottom2_1, "<Leave>", bottom_remove_bleu2)
    main_canvas.tag_bind(text2_1, "<Leave>", bottom_remove_bleu2)

def bottom_bleu3(event):
    bottom3_1 = main_canvas.create_image(1280/1.3, 700/1.55556, image = bottomImageSelection)
    text3_1 = main_canvas.create_text (1280/1.3, 700/1.55556, font=(fontName, fontSize), text='Score', fill=fontColor)
    main_canvas.tag_bind(bottom3_1, "<Leave>", bottom_remove_bleu3)
    main_canvas.tag_bind(text3_1, "<Leave>", bottom_remove_bleu3)

def bottom_bleu4(event):
    bottom4_1 = main_canvas.create_image(1280/1.3, 700/1.17, image = bottomImageSelection2)
    text4_1 = main_canvas.create_text (1280/1.3, 700/1.17, font=(fontName, fontSize), text='Quitter', fill=fontColor)
    main_canvas.tag_bind(bottom4_1, "<Leave>", bottom_remove_bleu4)
    main_canvas.tag_bind(text4_1, "<Leave>", bottom_remove_bleu4)

    

def bottom_remove_bleu1(event):
    bottom1_2 = main_canvas.create_image(1280/1.3, 700/2.8, image = bottomImage)
    text1_2 = main_canvas.create_text (1280/1.3, 700/2.8, font=(fontName, fontSize), text='Nouvelle Partie', fill=fontColor)
    main_canvas.tag_bind(bottom1_2, "<Enter>", bottom_bleu1)
    main_canvas.tag_bind(text1_2, "<Enter>", bottom_bleu1)

def bottom_remove_bleu2(event):
    bottom2_2 = main_canvas.create_image(1280/1.3, 700/2, image = bottomImage)
    text2_2 = main_canvas.create_text (1280/1.3, 700/2, font=(fontName, fontSize), text='Paramètres', fill=fontColor)
    main_canvas.tag_bind(bottom2_2, "<Enter>", bottom_bleu2)
    main_canvas.tag_bind(text2_2, "<Enter>", bottom_bleu2)

def bottom_remove_bleu3(event):
    bottom3_2 = main_canvas.create_image(1280/1.3, 700/1.55556, image = bottomImage)
    text3_2 = main_canvas.create_text (1280/1.3, 700/1.55556, font=(fontName, fontSize), text='Score', fill=fontColor)
    main_canvas.tag_bind(bottom3_2, "<Enter>", bottom_bleu3)
    main_canvas.tag_bind(text3_2, "<Enter>", bottom_bleu3)

def bottom_remove_bleu4(event):
    bottom4_2 = main_canvas.create_image(1280/1.3, 700/1.17, image = bottomImage2)
    text4_2 = main_canvas.create_text (1280/1.3, 700/1.17, font=(fontName, fontSize), text='Quitter', fill=fontColor)
    main_canvas.tag_bind(bottom4_2, "<Enter>", bottom_bleu4)
    main_canvas.tag_bind(text4_2, "<Enter>", bottom_bleu4)

"""

Fin des fonctions de sélection

"""



def callback():
    if messagebox.askokcancel("Quit", "Voulez-vous vraiment quitter ?"):
        window.destroy()
        winsound.PlaySound(None, winsound.SND_ASYNC)

def main():
    global window, main_canvas
    global bottomImage, bottomImage2, bottomImageSelection, bottomImageSelection2
    
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

    main_canvas = Canvas(window, bg="white", width = 1280, height = 700)
    main_canvas.grid(row = 0, column = 0)

    #importation des images
    logo = PhotoImage(file = "images/Boomberman.png")
    imageBG = PhotoImage(file = "images/background.png")
    bottomImage = PhotoImage(file = "images/Bottom.png")
    bottomImage2 = PhotoImage (file = "images/Bottom_exit.png")
    bottomImageSelection = PhotoImage (file = "images/Bottom_selection.png")
    bottomImageSelection2 = PhotoImage (file = "images/Bottom_exit_selection.png")

    #insertion d'images
    main_canvas.create_image(1280/2, 700/2, image = imageBG)
    main_canvas.create_image(1280/3 + 50, 700/6, image = logo)
    bottom1 = main_canvas.create_image(1280/1.3, 700/2.8, image = bottomImage, tags = "bottom1")
    bottom2 = main_canvas.create_image(1280/1.3, 700/2, image = bottomImage)
    bottom3 = main_canvas.create_image(1280/1.3, 700/1.55556, image = bottomImage)
    bottom4 = main_canvas.create_image(1280/1.3, 700/1.17, image = bottomImage2)

    #insertion du texte
    main_canvas.create_text (1280/1.3, 700/2.8, font=(fontName, fontSize), text='Nouvelle Partie', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/2, font=(fontName, fontSize), text='Paramètres', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/1.55556, font=(fontName, fontSize), text='Score', fill=fontColor)
    main_canvas.create_text (1280/1.3, 700/1.17, font=(fontName, fontSize), text='Quitter', fill=fontColor)

    #Si la sourie rentre dans un des images -> animation de sélection
    main_canvas.tag_bind(bottom1, "<Enter>", bottom_bleu1)
    main_canvas.tag_bind(bottom2, "<Enter>", bottom_bleu2)
    main_canvas.tag_bind(bottom3, "<Enter>", bottom_bleu3)
    main_canvas.tag_bind(bottom4, "<Enter>", bottom_bleu4)
    
    window.mainloop()


winsound.PlaySound("son/01 Unleashed.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


main()

pers1 = Personnage("Mateusz", 1, 4)
