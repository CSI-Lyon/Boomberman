from tkinter import *
from tkinter import messagebox
import winsound

class Personnage:
    def __init__(self, name, playerID, nbBombs):
        self.name = name
        self.playerID = playerID
        self.nbBombs = 4

def bouton_entree(event):
    #tr
    print("enter")

def bouton_up(event):
    print("up")

def bouton_down(event):
    print("down")

def bouton_right(event):
    print("right")

def bouton_left(event):
    print("left")

def callback():
    if messagebox.askokcancel("Quit", "Voulez-vous vraiment quitter ?"):
        window.destroy()
        winsound.PlaySound(None, winsound.SND_ASYNC)

def main():
    global window
    
    window = Tk()
    window.title("Boomberman")
    window.geometry("1280x700")
    window.resizable(False, False)

    window.protocol("WM_DELETE_WINDOW", callback)

    window.bind("<Return>", bouton_entree)
    window.bind("<Up>",bouton_up)
    window.bind("<Down>",bouton_down)
    window.bind("<Right>",bouton_right)
    window.bind("<Left>",bouton_left)
    window.mainloop()


winsound.PlaySound("01 Unleashed.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


main()

pers1 = Personnage("Mateusz", 1, 4)
