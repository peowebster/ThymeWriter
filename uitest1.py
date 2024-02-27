from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import matplotlib
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from planmaker import *

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
        self.usertab = Button(text="User Details", command=self.user_details_screen)
        self.usertab.pack(side="left", anchor="nw")

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

        self.currentuser = User()

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
            self.addwordsbutton.destroy()
            self.addwordsbox.destroy()
        elif self.state == "achievements":
            self.testach.destroy()


    def home_screen(self):
        self.clear_screen()

        self.state = "home"

        #draw logo
        self.logolabel = Label(image=self.logoimage)
        self.logolabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def get_todays_count(self, offset):
        today = self.findtoday(offset)

        return self.wordcount_data.setdefault(today, 0)
    
    def findtoday(self, offset):
        date = str(time.localtime().tm_mday - offset)
        month = str(time.localtime().tm_mon)
        year = str(time.localtime().tm_year)
        today = ""
        if len(date) == 1:
            today = today + "0" + date
        else:
            today = today + date

        today += "/"
        
        if len(month) == 1:
            today = today + "0" + month
        else:
            today = today + month
        
        today += "/"

        today = today + year[2] + year[3]
        return today
    
    def total_words(self):
        total = sum(self.wordcounts)
        return total
    
    def addwords(self, amount):
        try:
            addamount = int(amount)
        except:
            addamount = 0
        else:
            addamount = int(amount)

        print(addamount)
        today = self.findtoday(0)
        self.wordcount_data[today] += addamount

        self.updatewordcount()

    def updatewordcount(self):
        self.dates = self.wordcount_data.keys()
        self.wordcounts = self.wordcount_data.values()
        self.figure.canvas.draw()

    def wordcount_screen(self):
        self.clear_screen()

        self.state = "wordcount"
        
        self.wordstoday = Label(text="WORDS TODAY: " + str(self.get_todays_count(0)), font=("Arial", 45))
        self.wordstoday.place(relx=0.55, rely=0.1)
        self.pastwords = Label(text="Words yesterday: " + str(self.get_todays_count(1)), font=("Arial", 40))
        self.pastwords.place(relx=0.55, rely=0.2)

        self.paceselected = StringVar()
        self.r1 = Radiobutton(text="Randomised", value="randandom", variable=self.paceselected)
        self.r2 = Radiobutton(text="Increasing", value="ascending", variable=self.paceselected)
        self.r3 = Radiobutton(text="Decreasing", value="descending", variable=self.paceselected)
        self.r4 = Radiobutton(text="Steady", value="steady", variable=self.paceselected)
        self.r1.place(relx=0.05, rely=0.7)
        self.r2.place(relx=0.05, rely=0.73)
        self.r3.place(relx=0.05, rely=0.76)
        self.r4.place(relx=0.05, rely=0.79)

        self.totalwords = Label(text="Total Words: " + str(self.total_words()), font=("Arial", 40))
        self.totalwords.place(relx=0.55, rely=0.3)
        self.figure = Figure(figsize=(5.5, 4), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
        self.axes = self.figure.add_subplot()
        self.axes.plot(self.dates, self.wordcounts)
        self.figure_canvas.get_tk_widget().place(relx=0.05, rely=0.1)

        self.addwordsbox = Entry()
        self.addwordsbox.place(relx=0.55, rely=0.4)
        self.addwordsbutton = Button(text="Add Words", command=self.addwords(self.addwordsbox.get()))
        self.addwordsbutton.place(relx=0.72, rely=0.4)

    def user_details_screen(self):
        self.clear_screen()
        self.state = "user"

        self.usernamebox = Entry(text = self.currentuser.name)
        self.usernamebox.place(relx=0.05, rely=0.1)
        self.usernamebutton = Button(text="Set username")
        self.usernamebutton.place(relx=0.22, rely=0.1)

    def handle_ach_press(self):
        self.clear_screen()

        self.state = "achievements"

        self.testach = AchievementObject("test", 90, 0, self, "./assets/thymewriterlogo1.png")
        self.testach.achievementbox.pack()

    def handle_write_press(self):
        self.clear_screen()

    def handle_notes_press(self):
        self.clear_screen()

    def tag_search(self, notesarray, key):
        foundnotes = []
        for i in range(len(notesarray)):
            if key in notesarray[i].tags:
                foundnotes.append(notesarray[i])
        
        return foundnotes
    
    def title_search(self, notesarray, key):
        size = len(notesarray)
        middle = size/2
        start = 0
        end = size
        while size > 0:
            if notesarray[middle].name == key:
                return notesarray[middle]
            elif notesarray[middle].name > key:
                start = middle
                size = size/2
                middle = start + (size/2)
            elif notesarray[middle].name < key:
                end = middle
                size = size/2
                middle = start + (size/2)

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

    def destroy(self):
        self.achievementbox.name.destroy()
        self.achievementbox.progressmeter.destroy()
        self.achievementbox.icon.destroy()
        self.achievementbox.destroy()
        
class Note():
    def __init__(self, contents, tags, name):
        self.name = name
        self.contents = contents
        self.tags = tags

    def add_tag(self, tag):
        self.tags.append(str(tag))

class User():
    def __init__(self):
        self.projects = []
        self.name = "placeholder"
        self.currentproject = ""

    def setProject(project,self):
        if project not in self.projects:
            self.projects.append(project)
        
        self.currentproject = project

class Document():
    def __init__(self, title):
        self.title = title
        self.contents = ""
        self.path = "./documents/" + self.validtitle(self.title)

    def validtitle(self, title):
        modtitle = title
        for i in range(len(modtitle) - 1):
            if (modtitle[i] == ' ' or modtitle[i] == '/'):
                modtitle[i] = "_"
        return modtitle


class Project():
    def __init__(self, name):
        self.name = name
        self.wordcount = 0
        self.notes = []

    def add_note(self):
        self.notes.append(Note(self, "", []))
        self.sort_notes()

    def sort_notes(self):
        sortedlist = []
        for i in range(len(self.notes)):
            item = self.notes[i]
            if sortedlist == []:
                sortedlist.append(item)
            else:
                for j in range(len(sortedlist)):
                    if item.name >= sortedlist[j].name:
                        sortedlist.insert(j+1, item)
                        break
        
        self.notes = sortedlist

# Start the event loop.
window = Window()
window.mainloop()
