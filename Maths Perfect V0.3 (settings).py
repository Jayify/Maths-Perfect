from tkinter import *

#this class creates the operator selection page or main page where the student selects which operator they want to be tested on
class OperatorSelection():
    def __init__(self, master):
        self.master = master
        height = 8
        width = 18

        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(self.master, text="Welcome to Maths Perfect! Please select a section to continue:", font="sample 14", bg="lightblue")
        button_add = Button(self.master, text="ADDITION", command=lambda: self.load_next(), height=height, width=width)
        button_sub = Button(self.master, text="SUBTRACTION", command=lambda: self.load_next(), height=height, width=width)
        button_mult = Button(self.master, text="MULTIPLICATION", command=lambda: self.load_next(), height=height, width=width)
        button_div = Button(self.master, text="DIVISION", command=lambda: self.load_next(), height=height, width=width)
        button_final = Button(self.master, text="FINAL TEST", command=lambda: self.load_next(), height=8, width=87)
        button_settings = Button(self.master, text="SETTINGS", command=lambda: self.settings())
        

        #add to buttons and labels to canvas
        #labels
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_text)
        #operator buttons
        self.canvas.create_window(90, 230, window=button_add)
        self.canvas.create_window(250, 230, window=button_sub)
        self.canvas.create_window(410, 230, window=button_mult)
        self.canvas.create_window(570, 230, window=button_div)
        self.canvas.create_window(330, 380, window=button_final)

        self.canvas.create_window(34, 17, window=button_settings)

    def load_next(self):
        self.canvas.destroy()
        TestSelection(self.master)

    def settings(self):
        self.newWindow = Toplevel(self.master)
        self.app = SettingsWindow(self.newWindow)

#this class creates the settings window where the saved data can be cleared and other information is given
class SettingsWindow():
    def __init__(self, master):
        self.master = master
        master.withdraw() #hides the new root created. This root is destroyed when the settings window is destroyed

        canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        canvas.grid()
        #initialise new window
        SettingsWindow = Toplevel(self.master)
        SettingsWindow.title("Settings")
        SettingsWindow.geometry("400x195")
        SettingsWindow.resizable(width=False, height=False)
        #initialise canvas
        canvas = Canvas(SettingsWindow, width=400, height=195, bg="lightblue")
        canvas.grid()
        #add labels and buttons to settings window
        label_title = Label(SettingsWindow, text="Settings", bg="lightblue", font="sample 11 bold")
        label_data_text = Label(SettingsWindow, text="Saved data is not recoverable if deleted", bg="lightblue")
        button_clear = Button(SettingsWindow, text="Clear data", command=self.clear_data)
        button_quit = Button(SettingsWindow, text="Back", command=self.quit)
        #additional information about program
        label_developer = Label(SettingsWindow, text="Program designed and developed by Jayden Houghton", bg="lightblue")
        label_supporter = Label(SettingsWindow, text="This program was proudly supported by Robinson House", bg="lightblue")
        label_r = Label(SettingsWindow, text="R", font=("Script MT Bold", 14, "bold"), bg="lightblue", fg="orange")
        label_version = Label(SettingsWindow, text="Program version: V0.3", bg="lightblue")
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
class TestSelection():
    def __init__(self, master):
        self.master = master
        height = 17
        width = 25

        canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        canvas.grid()
        title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        text = Label(self.master, text="Please select a section to continue:", font="sample 14", bg="lightblue")

        score_1 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        score_2 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        score_3 = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")

        button_t1 = Button(self.master, text="TEST 1", command=self.print_e, height=height, width=width)
        button_t2 = Button(self.master, text="TEST 1", command=self.print_e, height=height, width=width)
        button_t3 = Button(self.master, text="TEST 1", command=self.print_e, height=height, width=width)
        
        canvas.create_window(330, 41, window=title) #title
        canvas.create_window(330, 105, window=text) #text
        #test buttons
        canvas.create_window(115, 310, window=button_t1)
        canvas.create_window(330, 310, window=button_t2)
        canvas.create_window(545, 310, window=button_t3)
        #operator scores
        canvas.create_window(115, 160, window=score_1)
        canvas.create_window(330, 160, window=score_2)
        canvas.create_window(545, 160, window=score_3)

    def print_e(self):
        print("e")

def main():
    root = Tk()
    root.title("Maths Perfect")
    root.resizable(width=False, height=False)
    app = OperatorSelection(root)
    root.mainloop()

main()



#https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter

