from tkinter import *
import random

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
        button_add = Button(self.master, text="ADDITION", command=lambda: self.load_next("Addition"), height=height, width=width)
        button_sub = Button(self.master, text="SUBTRACTION", command=lambda: self.load_next("Subtraction"), height=height, width=width)
        button_mult = Button(self.master, text="MULTIPLICATION", command=lambda: self.load_next("Multiplication"), height=height, width=width)
        button_div = Button(self.master, text="DIVISION", command=lambda: self.load_next("Division"), height=height, width=width)
        button_final = Button(self.master, text="FINAL TEST", command=lambda: self.load_next("Final Test"), height=8, width=87)
        
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

    def load_next(self, operator):
        self.canvas.destroy()
        TestSelection(self.master, operator)

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
        label_version = Label(SettingsWindow, text="Program version: V0.5.1", bg="lightblue")

        #add to canvas
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
    def __init__(self, master, operator):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
        #carry accross operator chosen
        self.operator = operator

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
        button_t1 = Button(self.master, text="TEST 1", command=lambda: self.load_next("1"), height=height, width=width)
        button_t2 = Button(self.master, text="TEST 2", command=lambda: self.load_next("2"), height=height, width=width)
        button_t3 = Button(self.master, text="TEST 3", command=lambda: self.load_next("3"), height=height, width=width)

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

    def load_next(self, difficulty):
        self.canvas.destroy()
        Quiz(self.master, self.operator, difficulty)

    def back(self):
        self.canvas.destroy()
        OperatorSelection(self.master)

#this class creates the quiz page where the student answer various maths questions
class Quiz:
    def __init__(self, master, operator, difficulty):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
        self.operator = operator #store variable in case back button is pressed
        name = operator+" "+str(difficulty) #convert operator and difficulty chosen to string for display
        
        #create widgets
        #assorted
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_name = Label(self.master, text=name, font="sample 14", bg="lightblue")
        button_back = Button(self.master, text="Back", command=self.back)
        #quiz
        self.canvas.create_rectangle(50,180,610,340) #create box for questions to go in
        self.label_question_num = Label(self.master, text="Question: {}/10", font="sample 12", bg="lightblue")
        self.label_question = Label(self.master, text="Question", font="sample 18", bg="lightblue", width=20, anchor=W)
        label_score = Label(self.master, text="Score: {}/10", font="sample 12", bg="lightblue")
        entry = Entry(self.master, text="TEST 1")
        button_submit = Button(self.master, text="submit", command=self.process, height=2, width=10)

        #add to canvas
        #assorted widgets
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_name)
        self.canvas.create_window(22, 17, window=button_back)
        #quiz
        self.canvas.create_window(115, 160, window=self.label_question_num)
        self.canvas.create_window(545, 160, window=label_score)
        self.canvas.create_window(240, 225, window=self.label_question)
        self.canvas.create_window(500, 225, window=entry)
        self.canvas.create_window(330, 295, window=button_submit)

        self.question(difficulty)
    
    def question(self, difficulty):
        question_number = 1
        self.label_question_num.configure(text=(str(question_number),"/10"))

        #create question
        if self.operator == "Addition":
            self.q_add(difficulty)
        elif self.operator == "Subtraction":
            self.q_sub(difficulty)
        elif self.operator == "Multiplication":
            self.q_mult(difficulty)
        elif self.operator == "Division":
            self.q_div(difficulty)
        else:
            sym = random.randint(1,4)
            if sym == 1:
                self.q_add(difficulty)
            elif sym == 2:
                self.q_sub(difficulty)
            elif sym == 3:
                self.q_mult(difficulty)
            else:
                self.q_div(difficulty)
        #print(operator_symbol)
        #self.label_question.configure(text=("what is {} {} {} = ? ".format(var_1, operator_symbol, var_2)))
        #self.canvas.update()
        question_number+=1

    def q_add(self, difficulty):
        num_max = (10*(int(difficulty)*2)-15)
        num_min = (8*(int(difficulty))-7)
        var_1 = random.randint(num_min,num_max)
        var_2 = random.randint(num_min,num_max)
        operator_symbol = "+"
        self.label_question.configure(text=("What is {} + {} = ? ".format(var_1, var_2)))
        self.canvas.update()

        #calculate answer
        #return answer

    def q_sub(self, difficulty):
        answer = -1
        num_max = (5*(int(difficulty)*2))
        num_min = (4*(int(difficulty))-3)
        while answer < 0:
            var_1 = random.randint(2*num_min,num_max)
            var_2 = random.randint(num_min,num_max)
            answer = var_1 - var_2
        operator_symbol = "-"
        self.label_question.configure(text=("What is {} - {} = ? ".format(var_1, var_2)))
        self.canvas.update()
        
    def q_mult(self, difficulty):
        if difficulty == "1":
            num_max_1 = 8
            num_max_2 = 5
            num_min = 1
        elif difficulty == "2":
            num_max_1 = 10
            num_max_2 = 8
            num_min = 3
        else:
            num_max_1 = 15
            num_max_2 = 12
            num_min = 7
        var_1 = random.randint(num_min,num_max_1)
        var_2 = random.randint(num_min,num_max_2)
        print(num_min, num_max_1, num_max_2)
        operator_symbol = "*"
        self.label_question.configure(text=("What is {} x {} = ? ".format(var_1, var_2)))
        self.canvas.update()
        
    def q_div(self, difficulty):
        num_max = (3*(int(difficulty))+2)
        num_min = (2*(int(difficulty))-1)
        print("aga", num_min, num_max)
        var_1 = random.randint(num_min,num_max)
        var_2 = random.randint(num_min,num_max)
        var_3 = var_1*var_2
        #answer is var_2
        operator_symbol = "÷"
        self.label_question.configure(text=("What is {} ÷ {} = ? ".format(var_3, var_1)))
        self.canvas.update()
        
    def back(self):
        self.canvas.destroy()
        TestSelection(self.master, self.operator)

    def process(self):
        print("u")
        #create widgets
        label_correct = Label(self.master, text="Correct!", font="sample 20", fg="green", bg="lightblue")
        label_example = Label(self.master, text="5 x 4 = 20", font="sample 14", bg="lightblue")
        button_next = Button(self.master, text="Next", command=self.process, height=2, width=10)
        #add to canvas
        self.canvas.create_window(160, 400, window=label_correct)
        self.canvas.create_window(330, 400, window=label_example)
        self.canvas.create_window(500, 400, window=button_next)
        

def main():
    root = Tk()
    root.title("Maths Perfect")
    root.resizable(width=False, height=False)
    app = OperatorSelection(root)
    root.mainloop()

main()

