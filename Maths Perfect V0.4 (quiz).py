from tkinter import *

#this class creates the operator selection page or main page where the student selects which operator they want to be tested on
class OperatorSelection:
    def __init__(self, master):
        self.master = master
        height = 8
        width = 18
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
        #create widgets
        #assorted
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(self.master, text="Welcome to Maths Perfect! Please select a section to continue:", font="sample 14", bg="lightblue")
        button_settings = Button(self.master, text="SETTINGS", command=lambda: self.settings())
        #operator options
        button_add = Button(self.master, text="ADDITION", command=lambda: self.load_next(), height=height, width=width)
        button_sub = Button(self.master, text="SUBTRACTION", command=lambda: self.load_next(), height=height, width=width)
        button_mult = Button(self.master, text="MULTIPLICATION", command=lambda: self.load_next(), height=height, width=width)
        button_div = Button(self.master, text="DIVISION", command=lambda: self.load_next(), height=height, width=width)
        button_final = Button(self.master, text="FINAL TEST", command=lambda: self.load_next(), height=8, width=87)
        
        #add to buttons and labels to canvas
        #assorted widgets
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_text)
        self.canvas.create_window(34, 17, window=button_settings)
        #operator buttons
        self.canvas.create_window(90, 230, window=button_add)
        self.canvas.create_window(250, 230, window=button_sub)
        self.canvas.create_window(410, 230, window=button_mult)
        self.canvas.create_window(570, 230, window=button_div)
        self.canvas.create_window(330, 380, window=button_final)

    def load_next(self):
        self.canvas.destroy()
        TestSelection(self.master)

    def settings(self):
        self.newWindow = Toplevel(self.master)
        self.app = SettingsWindow(self.newWindow)


#this class creates the settings window where the saved data can be cleared and other information is given
class SettingsWindow:
    def __init__(self, master):
        #initialise new window
        self.master = master
        master.withdraw() #hides the new root created. This root is destroyed when the settings window is destroyed
        SettingsWindow = Toplevel(self.master)
        SettingsWindow.title("Settings")
        SettingsWindow.geometry("400x195")
        SettingsWindow.resizable(width=False, height=False)
        canvas = Canvas(SettingsWindow, width=400, height=195, bg="lightblue")
        canvas.grid()
        #create widgets
        #assorted
        label_title = Label(SettingsWindow, text="Settings", bg="lightblue", font="sample 11 bold")
        label_data_text = Label(SettingsWindow, text="Saved data is not recoverable if deleted", bg="lightblue")
        button_clear = Button(SettingsWindow, text="Clear data", command=self.clear_data)
        button_quit = Button(SettingsWindow, text="Back", command=self.quit)
        #additional information about program
        label_developer = Label(SettingsWindow, text="Program designed and developed by Jayden Houghton", bg="lightblue")
        label_supporter = Label(SettingsWindow, text="This program was proudly supported by Robinson House", bg="lightblue")
        label_r = Label(SettingsWindow, text="R", font=("Script MT Bold", 14, "bold"), bg="lightblue", fg="orange")
        label_version = Label(SettingsWindow, text="Program version: V0.4", bg="lightblue")
        #add all items to canvas
        canvas.create_window(200, 20, window=label_title)
        canvas.create_window(155, 50, window=label_data_text)
        canvas.create_window(305, 50, window=button_clear)
        canvas.create_window(200, 100, window=label_developer)
        canvas.create_window(185, 130, window=label_supporter)
        canvas.create_window(355, 130, window=label_r)
        canvas.create_window(200, 175, window=label_version)
        canvas.create_window(22, 17, window=button_quit)
        #divider lines
        canvas.create_line(20,75,380,75)
        canvas.create_line(20,155,380,155)
        
    def quit(self):
        self.master.destroy()

    def clear_data(self):
        print("clearing data")

        
#this class creates the test selection page where the student selects the level they want
class TestSelection:
    def __init__(self, master):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
        #create widgets
        #assorted
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(self.master, text="Please select a section to continue:", font="sample 14", bg="lightblue")
        button_back = Button(self.master, text="Back", command=self.back)
        #scores
        label_score_1 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        label_score_2 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        label_score_3 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        #test options
        button_t1 = Button(self.master, text="TEST 1", command=self.load_next, height=height, width=width)
        button_t2 = Button(self.master, text="TEST 2", command=self.load_next, height=height, width=width)
        button_t3 = Button(self.master, text="TEST 3", command=self.load_next, height=height, width=width)

        #add to canvas
        #assorted widgets
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_text)
        self.canvas.create_window(22, 17, window=button_back)
        #test buttons
        self.canvas.create_window(115, 310, window=button_t1)
        self.canvas.create_window(330, 310, window=button_t2)
        self.canvas.create_window(545, 310, window=button_t3)
        #operator scores
        self.canvas.create_window(115, 160, window=label_score_1)
        self.canvas.create_window(330, 160, window=label_score_2)
        self.canvas.create_window(545, 160, window=label_score_3)

    def load_next(self):
        self.canvas.destroy()
        Quiz(self.master)

    def back(self):
        self.canvas.destroy()
        OperatorSelection(self.master)

#this class creates the quiz page where the student answer various maths questions
class Quiz:
    def __init__(self, master):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()

        #create widgets
        #assorted
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_name = Label(self.master, text="Test Name", font="sample 14", bg="lightblue")
        button_back = Button(self.master, text="Back", command=self.back)
        #quiz
        self.canvas.create_rectangle(50,180,610,340) #create box for questions to go in
        label_question_num = Label(self.master, text="Question: {}/10", font="sample 12", bg="lightblue")
        label_question = Label(self.master, text="What is 5 times 4?", font="sample 18", bg="lightblue", width=20, anchor=W)
        label_score = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        entry = Entry(self.master, text="TEST 1")
        button_submit = Button(self.master, text="submit", command=self.process, height=2, width=10)

        #add to canvas
        #assorted widgets
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_name)
        self.canvas.create_window(22, 17, window=button_back)
        #quiz
        self.canvas.create_window(115, 160, window=label_question_num)
        self.canvas.create_window(545, 160, window=label_score)
        self.canvas.create_window(240, 225, window=label_question)
        self.canvas.create_window(500, 225, window=entry)
        self.canvas.create_window(330, 295, window=button_submit)

    def back(self):
        self.canvas.destroy()
        TestSelection(self.master)

    def process(self):
        print("u")
        #create widgets
        label_correct = Label(self.master, text="Correct!", font="sample 20", fg="green", bg="lightblue")
        label_example = Label(self.master, text="5 x 4 = 20", font="sample 14", bg="lightblue")
        button_next = Button(self.master, text="Next", command=self.next, height=2, width=10)
        #add to canvas
        self.canvas.create_window(160, 400, window=label_correct)
        self.canvas.create_window(330, 400, window=label_example)
        self.canvas.create_window(500, 400, window=button_next)

    def next(self):
        print("e")
        


def main():
    root = Tk()
    root.title("Maths Perfect")
    root.resizable(width=False, height=False)
    app = OperatorSelection(root)
    root.mainloop()

main()

