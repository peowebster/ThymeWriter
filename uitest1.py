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
        self.achtab = Button(text="Achievements", command=self.handle_ach_press)
        self.achtab.pack(side="left", anchor="nw")
        self.writetab = Button(text="Writer", command=self.handle_write_press)
        self.writetab.pack(side="left", anchor="nw")
        self.notetab = Button(text="Notes", command=self.handle_notes_press)
        self.notetab.pack(side="left", anchor="nw")
        
        #logo
        self.logoimage = PhotoImage(file='./assets/thymewriterlogo3.png')
        self.logolabel = Label(image=self.logoimage)
        self.logolabel.pack()

    def handle_words_press(self):
        wordswindow = WordsWindow()
        self.destroy()
        wordswindow.mainloop()
    
    def handle_ach_press(self):
        achwindow = AchWindow()
        self.destroy()
        achwindow.mainloop()

    def handle_write_press(self):
        writewindow = WriteWindow()
        self.destroy()
        writewindow.mainloop()

    def handle_notes_press(self):
        noteswindow = NotesWindow()
        self.destroy()
        noteswindow.mainloop()

class WordsWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter Wordcount")
        self.geometry("1200x700")

class AchWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter Achievements")
        self.geometry("1200x700")

class WriteWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter Text Editor")
        self.geometry("1200x700")

class NotesWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter Worldbuilding Notes")
        self.geometry("1200x700")

# Start the event loop.
window = StartWindow()
window.mainloop()
