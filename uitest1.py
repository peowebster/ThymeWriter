from tkinter import Tk, Button


class StartWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter")
        self.geometry("1200x700")

        # tab buttons
        self.wordstab = Button(text="Wordcount", command=self.handle_words_press)
        self.wordstab.pack()
        self.achtab = Button(text="Achievements")
        self.achtab.pack()
        self.writetab = Button(text="Writer")
        self.writetab.pack()
        self.notetab = Button(text="Notes")
        self.notetab.pack()

    def handle_words_press(self):
        wordswindow = WordsWindow()
        wordswindow.mainloop()

class WordsWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("ThymeWriter")
        self.geometry("1200x700")

# Start the event loop.
window = StartWindow()
window.mainloop()
