from tkinter import PhotoImage

class Image(PhotoImage):

    def __init__(self, directory, name):
        PhotoImage.__init__(self, file="images/{}/{}.png".format(directory, name))
