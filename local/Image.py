from tkinter import PhotoImage

class Image(PhotoImage):

    def __init__(self, directory, name):
        images[]PhotoImage.__init__(self, file="images/{}/{}.png".format(directory, name))
