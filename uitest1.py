from tkinter import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

matplotlib.use("TkAgg")

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.image_initialise()
        self.wordcount_data_initialise()

        self.title("ThymeWriter")
        self.geometry("1200x700")

        # search bar
        self.searchbar = Entry()
        self.searchbar.pack(side="right", anchor="ne")

        # tab buttons
        self.hometab = Button(text="Home", command=self.home_screen)
        self.hometab.pack(side="left", anchor="nw")
        self.wordstab = Button(text="Wordcount", command=self.wordcount_screen)
        self.wordstab.pack(side="left", anchor="nw")
        self.achtab = Button(text="Achievements", command=self.handle_ach_press)
        self.achtab.pack(side="left", anchor="nw")
        self.writetab = Button(text="Writer", command=self.handle_write_press)
        self.writetab.pack(side="left", anchor="nw")
        self.notetab = Button(text="Notes", command=self.handle_notes_press)
        self.notetab.pack(side="left", anchor="nw")

        # Menu Bar
        self.menubar = Menu()
        self.config(menu=self.menubar)

        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="New Project")
        self.filemenu.add_command(label="New Note")
        self.filemenu.add_command(label="Open Project")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save As")
        self.filemenu.add_command(label="Exit", command=self.destroy)
        self.menubar.add_cascade(label="File",menu=self.filemenu)

        self.editmenu = Menu(self.menubar)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_command(label="Redo")
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.editmenu.add_command(label="Search")
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)

        self.tabmenu = Menu(self.menubar)
        self.tabmenu.add_command(label="Home", command=self.home_screen)
        self.tabmenu.add_command(label="Wordcount", command=self.wordcount_screen)

        self.state = "clear"

        self.home_screen()
    
    def image_initialise(self):
        self.logoimage = PhotoImage(file='./assets/thymewriterlogo3.png')

    def wordcount_data_initialise(self):
        self.wordcount_data = {
            "12/12/23" : 120,
            "12/13/23" : 456,
            "12/14/23" : 34
        }
        self.dates = self.wordcount_data.keys()
        self.wordcounts = self.wordcount_data.values()

    def clear_screen(self):
        if self.state == "home":
            self.logolabel.destroy()
        elif self.state == "wordcount":
            self.wordstoday.destroy()
            self.pastwords.destroy()
            self.r1.destroy()
            self.r2.destroy()
            self.r3.destroy()
            self.r4.destroy()
            self.totalwords.destroy()
            self.figure_canvas.get_tk_widget().destroy()


    def home_screen(self):
        self.clear_screen()

        self.state = "home"

        #draw logo
        self.logolabel = Label(image=self.logoimage)
        self.logolabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def wordcount_screen(self):
        self.clear_screen()

        self.state = "wordcount"
        
        self.wordstoday = Label(text="WORDS TODAY")
        self.wordstoday.pack()
        self.pastwords = Label(text="Words yesterday\nWords the day before\nWords the day before")
        self.pastwords.pack()

        self.paceselected = StringVar()
        self.r1 = Radiobutton(text="Randomised", value="rand", variable=self.paceselected)
        self.r2 = Radiobutton(text="Increasing", value="inc", variable=self.paceselected)
        self.r3 = Radiobutton(text="Decreasing", value="dec", variable=self.paceselected)
        self.r4 = Radiobutton(text="Steady", value="st", variable=self.paceselected)
        self.r1.pack()
        self.r2.pack()
        self.r3.pack()
        self.r4.pack()

        self.totalwords = Label(text="TOTAL WORDS")
        self.totalwords.pack()
        self.figure = Figure(figsize=(4.5, 3), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.axes = self.figure.add_subplot()
        self.axes.plot(self.dates, self.wordcounts)
        self.figure_canvas.get_tk_widget().place(relx=0.05, rely=0.1)


    def handle_ach_press(self):
        self.clear_screen()

        self.state = "achievements"

        self.testach = AchievementObject("test", 90, 0, self, "./assets/thymewriterlogo1.png")
        self.testach.achievementbox.pack()

    def handle_write_press(self):
        self.clear_screen()

    def handle_notes_press(self):
        self.clear_screen()

class AchievementObject():
    def __init__(self, achname, goal, progress, homeframe, icon):
        self.achievementbox = Frame()
        self.achievementbox.name = Label(text=achname)
        self.achievementbox.name.pack()
        self.achievementbox.progressmeter = Label(text=str(progress) + "/" + str(goal))
        self.achievementbox.progressmeter.pack()

        self.icon = PhotoImage(file=icon)
        self.achievementbox.icon = Label(image=self.icon)
        self.achievementbox.icon.pack()
        

# Start the event loop.
window = Window()
window.mainloop()
