from tkinter import *


class StartWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter")
        self.geometry("1200x700")

        # search bar
        self.searchbar = Entry()
        self.searchbar.pack(side="right", anchor="ne")

        # tab buttons
        self.wordstab = Button(text="Wordcount", command=self.handle_words_press)
        self.wordstab.pack(side="left", anchor="nw")
        self.achtab = Button(text="Achievements")
        self.achtab.pack(side="left", anchor="nw")
        self.writetab = Button(text="Writer")
        self.writetab.pack(side="left", anchor="nw")
        self.notetab = Button(text="Notes")
        self.notetab.pack(side="left", anchor="nw")
        
        #logo
        self.logoimage = PhotoImage(file='./assets/thymewriterlogo3.png')
        self.logolabel = Label(image=self.logoimage)
        self.logolabel.pack()

    def handle_words_press(self):
        wordswindow = WordsWindow()
        self.destroy()
        wordswindow.mainloop()

class WordsWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter")
        self.geometry("1200x700")

        # search bar
        self.searchbar = Entry()
        self.searchbar.pack(side="right", anchor="ne")

        # tab buttons
        self.wordstab = Button(text="Home", command=self.handle_home_press)
        self.wordstab.pack(side="left", anchor="nw")
        self.achtab = Button(text="Achievements")
        self.achtab.pack(side="left", anchor="nw")
        self.writetab = Button(text="Writer")
        self.writetab.pack(side="left", anchor="nw")
        self.notetab = Button(text="Notes")
        self.notetab.pack(side="left", anchor="nw")
        
        #logo
        self.logoimage = PhotoImage(file='./assets/thymewriterlogo3.png')
        self.logolabel = Label(image=self.logoimage)
        self.logolabel.pack()

    def handle_home_press(self):
        window = StartWindow()
        self.destroy()
        window.mainloop()

# Start the event loop.
window = StartWindow()
window.mainloop()
