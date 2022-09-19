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

        #get score values from file
        self.data_list = read_file()

        #all values are strings so need to be individually converted to integers
        self.add_scores = self.data_list[0]
        self.sub_scores = self.data_list[1]
        self.mult_scores = self.data_list[2]
        self.div_scores = self.data_list[3]
        self.final_scores = self.data_list[4]

        total_add_score = int(self.add_scores[0])+int(self.add_scores[1])+int(self.add_scores[2])
        total_sub_score = int(self.sub_scores[0])+int(self.sub_scores[1])+int(self.sub_scores[2])
        total_mult_score = int(self.mult_scores[0])+int(self.mult_scores[1])+int(self.mult_scores[2])
        total_div_score = int(self.div_scores[0])+int(self.div_scores[1])+int(self.div_scores[2])
        total_final_score = int(self.final_scores[0])+int(self.final_scores[1])+int(self.final_scores[2])

        #create widgets
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(self.master, text="Welcome to Maths Perfect! Please select a section to continue:", font="sample 14", bg="lightblue")
        button_settings = Button(self.master, text="SETTINGS", command=lambda: self.settings())
        button_add = Button(self.master, text="ADDITION \n{}/30".format(total_add_score), command=lambda: self.load_next("Addition"), height=height, width=width)
        button_sub = Button(self.master, text="SUBTRACTION \n{}/30".format(total_sub_score), command=lambda: self.load_next("Subtraction"), height=height, width=width)
        button_mult = Button(self.master, text="MULTIPLICATION \n{}/30".format(total_mult_score), command=lambda: self.load_next("Multiplication"), height=height, width=width)
        button_div = Button(self.master, text="DIVISION \n{}/30".format(total_div_score), command=lambda: self.load_next("Division"), height=height, width=width)
        button_final = Button(self.master, text="FINAL TEST \n{}/30".format(total_final_score), command=lambda: self.load_next("Final Test"), height=8, width=87)
        
        #add to buttons and labels to canvas
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_text)
        self.canvas.create_window(34, 17, window=button_settings)
        self.canvas.create_window(90, 230, window=button_add)
        self.canvas.create_window(250, 230, window=button_sub)
        self.canvas.create_window(410, 230, window=button_mult)
        self.canvas.create_window(570, 230, window=button_div)
        self.canvas.create_window(330, 380, window=button_final)

    def load_next(self, operator):
        self.canvas.destroy()
        TestSelection(self.master, operator, self.add_scores, self.sub_scores, self.mult_scores, self.div_scores, self.final_scores, self.data_list)

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
        SettingsWindow.geometry("400x220")
        SettingsWindow.resizable(width=False, height=False)
        canvas = Canvas(SettingsWindow, width=400, height=220, bg="lightblue")
        canvas.grid()

        #create widgets
        label_title = Label(SettingsWindow, text="Settings", bg="lightblue", font="sample 11 bold")
        label_data_text = Label(SettingsWindow, text="Saved data is not recoverable if deleted", bg="lightblue")
        button_clear = Button(SettingsWindow, text="Clear data", command=self.clear_data)
        label_restart = Label(SettingsWindow, text="PLEASE RESTART PROGRAM AFTER DATA RESET", bg="lightblue", font="sample 9 bold")
        button_quit = Button(SettingsWindow, text="Back", command=self.quit)
        label_developer = Label(SettingsWindow, text="Program designed and developed by Jayden Houghton", bg="lightblue")
        label_supporter = Label(SettingsWindow, text="This program was proudly supported by Robinson House", bg="lightblue")
        label_r = Label(SettingsWindow, text="R", font=("Script MT Bold", 14, "bold"), bg="lightblue", fg="orange")
        label_version = Label(SettingsWindow, text="Program version: V1.0", bg="lightblue")

        #add to canvas
        canvas.create_window(200, 20, window=label_title)
        canvas.create_window(155, 50, window=label_data_text)
        canvas.create_window(305, 50, window=button_clear)
        canvas.create_window(200, 75, window=label_restart)
        canvas.create_window(200, 125, window=label_developer)
        canvas.create_window(185, 155, window=label_supporter)
        canvas.create_window(355, 155, window=label_r)
        canvas.create_window(200, 200, window=label_version)
        canvas.create_window(22, 17, window=button_quit)
        #divider lines
        canvas.create_line(20,100,380,100)
        canvas.create_line(20,180,380,180)
        
    def quit(self):
        self.master.destroy()

    def clear_data(self):
        clear_file()

        
#this class creates the test selection page where the student selects the level they want
class TestSelection:
    def __init__(self, master, operator, add_scores, sub_scores, mult_scores, div_scores, final_scores, data_list):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()

        #initiate variables
        self.operator = operator
        self.add_scores = add_scores
        self.sub_scores = sub_scores
        self.mult_scores = mult_scores
        self.div_scores = div_scores
        self.final_scores = final_scores
        self.data_list = data_list

        #create score_list
        if self.operator == "Addition":
            score_list = add_scores
        elif self.operator == "Subtraction":
            score_list = sub_scores
        elif self.operator == "Multiplication":
            score_list = mult_scores
        elif self.operator == "Division":
            score_list = div_scores
        else:
            score_list = final_scores
        self.score_list = score_list

        #create widgets
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(self.master, text="Please select a section to continue:", font="sample 14", bg="lightblue")
        button_back = Button(self.master, text="Back", command=self.back)
        label_score_1 = Label(self.master, text="Score: {}/10".format(score_list[0]), font="sample 12", bg="lightblue")
        label_score_2 = Label(self.master, text="Score: {}/10".format(score_list[1]), font="sample 12", bg="lightblue")
        label_score_3 = Label(self.master, text="Score: {}/10".format(score_list[2]), font="sample 12", bg="lightblue")
        button_t1 = Button(self.master, text="TEST 1", command=lambda: self.load_next("1"), height=height, width=width)
        button_t2 = Button(self.master, text="TEST 2", command=lambda: self.load_next("2"), height=height, width=width)
        button_t3 = Button(self.master, text="TEST 3", command=lambda: self.load_next("3"), height=height, width=width)

        #add to canvas
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_text)
        self.canvas.create_window(22, 17, window=button_back)
        self.canvas.create_window(115, 310, window=button_t1)
        self.canvas.create_window(330, 310, window=button_t2)
        self.canvas.create_window(545, 310, window=button_t3)
        self.canvas.create_window(115, 160, window=label_score_1)
        self.canvas.create_window(330, 160, window=label_score_2)
        self.canvas.create_window(545, 160, window=label_score_3)

    def load_next(self, difficulty):
        self.canvas.destroy()
        Quiz(self.master, self.operator, difficulty, self.add_scores, self.sub_scores, self.mult_scores, self.div_scores, self.final_scores, self.data_list, self.score_list)

    def back(self):
        self.canvas.destroy()
        OperatorSelection(self.master)

#this class creates the quiz page where the student answer various maths questions
class Quiz:
    def __init__(self, master, operator, difficulty, add_scores, sub_scores, mult_scores, div_scores, final_scores, data_list, score_list):
        #initialise new window
        self.master = master
        height = 17
        width = 25
        self.canvas = Canvas(self.master, width=660, height=460, bg="lightblue")
        self.canvas.grid()
                
        #initialise variables
        self.q_answer = 0
        self.q_question = "question"
        self.score = 0
        self.question_number = 0
        name = operator+" "+str(difficulty) #convert operator and difficulty chosen to string for display
        self.var = IntVar() #creates variable to hold an integer        
        self.old_score = score_list[int(difficulty)-1]
        self.ready_next = False
        self.submitted = False
        validation = master.register(self.only_numbers)
        self.NUMBER_OF_QUESTIONS = 10 #choose how many questions should be in each test

        #store variable in case back button is pressed or test is repeated
        self.operator = operator 
        self.difficulty = difficulty
        self.operator = operator
        self.add_scores = add_scores
        self.sub_scores = sub_scores
        self.mult_scores = mult_scores
        self.div_scores = div_scores
        self.final_scores = final_scores
        self.data_list = data_list
        self.score_list = score_list
        
        #create widgets
        label_title = Label(self.master, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_name = Label(self.master, text=name, font="sample 14", bg="lightblue")
        button_back = Button(self.master, text="Back", command=self.back)
        self.canvas.create_rectangle(50,180,610,340) #create box for questions to go in
        self.label_question_num = Label(self.master, text="Question: {}/10", font="sample 12", bg="lightblue")
        self.label_question = Label(self.master, text="Question", font="sample 18", bg="lightblue", width=20, anchor=W)
        self.label_score = Label(self.master, text="Score: {}/10".format(self.score), font="sample 12", bg="lightblue")
        self.ans_entry = Entry(self.master, text="TEST 1", validate="key", validatecommand=(validation,'%S'))
        self.button_submit = Button(self.master, text="submit", command=self.process, height=2, width=10)

        #add to canvas
        self.canvas.create_window(330, 41, window=label_title)
        self.canvas.create_window(330, 105, window=label_name)
        self.canvas.create_window(22, 17, window=button_back)
        self.canvas.create_window(115, 160, window=self.label_question_num)
        self.canvas.create_window(545, 160, window=self.label_score)
        self.canvas.create_window(240, 225, window=self.label_question)
        self.canvas.create_window(500, 225, window=self.ans_entry)
        self.canvas.create_window(330, 295, window=self.button_submit)
        self.button_next = Button(self.master, text="Next", command=self.next, height=2, width=10)
        self.canvas.create_window(500, 400, window=self.button_next)
        
        self.quiz(int(difficulty))

    #main function for running the quiz    
    def quiz(self, difficulty):
        question_number = 1
        while self.question_number < self.NUMBER_OF_QUESTIONS:
            self.question_number += 1
            self.label_question_num.configure(text=(str(self.question_number),"/10"))
            self.canvas.update()
            self.question(difficulty) #create question
            self.button_next.wait_variable(self.var) #wait for a change in variable value to continue
        self.end_page()

    #create question    
    def question(self, difficulty):
        if self.operator == "Addition":
            self.q_add(difficulty)
        elif self.operator == "Subtraction":
            self.q_sub(difficulty)
        elif self.operator == "Multiplication":
            self.q_mult(difficulty)
        elif self.operator == "Division":
            self.q_div(difficulty)
        else:
            symbol = random.randint(1,4)
            if symbol == 1:
                self.q_add(difficulty)
            elif symbol == 2:
                self.q_sub(difficulty)
            elif symbol == 3:
                self.q_mult(difficulty)
            else:
                self.q_div(difficulty)

    #create addition question
    def q_add(self, difficulty):
        num_max = (10*(int(difficulty)*2)-15)
        num_min = (8*(int(difficulty))-7)
        var_1 = random.randint(num_min,num_max)
        var_2 = random.randint(num_min,num_max)
        operator_symbol = "+"
        self.label_question.configure(text=("What is {} + {} = ? ".format(var_1, var_2)))
        self.canvas.update()
        self.q_answer = var_1 + var_2
        self.q_question = "{} + {} = {} ".format(var_1, var_2, self.q_answer)

    #create subtraction question
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
        self.q_answer = var_1 - var_2
        self.q_question = "{} - {} = {} ".format(var_1, var_2, self.q_answer)
        
    #create multiplication question
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
        operator_symbol = "*"
        self.label_question.configure(text=("What is {} x {} = ? ".format(var_1, var_2)))
        self.canvas.update()
        self.q_answer = var_1 * var_2
        self.q_question = "{} x {} = {} ".format(var_1, var_2, self.q_answer)

    #create division question       
    def q_div(self, difficulty):
        num_max = (3*(int(difficulty))+2)
        num_min = (2*(int(difficulty))-1)
        var_1 = random.randint(num_min,num_max)
        var_2 = random.randint(num_min,num_max)
        var_3 = var_1*var_2
        operator_symbol = "÷"
        self.label_question.configure(text=("What is {} ÷ {} = ? ".format(var_3, var_1)))
        self.canvas.update()
        self.q_answer = var_2
        self.q_question = "{} ÷ {} = {} ".format(var_3, var_1, var_2)

    #process the inputted answer
    def process(self):
        if self.submitted == False:
            self.submitted = True
            answer = self.ans_entry.get()
            if answer != '':
                if str(answer) == str(self.q_answer):
                    #if correct
                    self.label_correct = Label(self.master, text="Correct!", font="sample 20", fg="green", bg="lightblue")
                    self.canvas.create_window(160, 400, window=self.label_correct)
                    self.label_example = Label(self.master, text=self.q_question, font="sample 14", bg="lightblue")
                    self.canvas.create_window(330, 400, window=self.label_example)
                    self.button_next = Button(self.master, text="Next", command=self.next, height=2, width=10)
                    self.canvas.create_window(500, 400, window=self.button_next)
                    self.score += 1
                    self.label_score.configure(text="Score: {}/10".format(self.score)) #update score
                    self.canvas.update()
                else:
                    #if incorrect
                    self.label_correct = Label(self.master, text="Incorrect", font="sample 20", fg="red", bg="lightblue")
                    self.canvas.create_window(160, 400, window=self.label_correct)
                         
                    self.label_example = Label(self.master, text=self.q_question, font="sample 14", bg="lightblue")
                    self.canvas.create_window(330, 400, window=self.label_example)
                    self.button_next = Button(self.master, text="Next", command=self.next, height=2, width=10)
                    self.canvas.create_window(500, 400, window=self.button_next)
                self.ready_next = True
            else:
                self.submitted = False                

    #next question
    def next(self):
        if self.ready_next:
            #clear bottom of page for next question
            self.label_example.destroy()
            self.label_correct.destroy()
            self.button_next.destroy()
            self.ans_entry.delete(0, 'end')
            self.var.set(1)
            self.ready_next = False
            self.submitted = False

    #this page is displayed when the quiz is completed
    def end_page(self):
        score = self.score
        self.record_score(score)
        self.canvas.delete("all")
        label_complete = Label(self.master, text="Test Compete!", font="sample 20 bold", bg="lightblue")
        label_score = Label(self.master, text=("You scored {}/10!".format(score)), font="sample 18", bg="lightblue")
        #give suggestion message depending on score
        if score < 5:
            label_suggestion = Label(self.master, text=("Uh oh. Play this test a few more times to practice your skills."), font="sample 16", bg="lightblue")
        elif score < 8:
            label_suggestion = Label(self.master, text=("Nice! We recommend trying this test again to improve your skills."), font="sample 16", bg="lightblue")
        elif score < 10:
            label_suggestion = Label(self.master, text=("Great job! You're ready to try a harder test!"), font="sample 16", bg="lightblue")
        else:
            label_suggestion = Label(self.master, text=("Perfect! You're ready to try a harder test!"), font="sample 16", bg="lightblue")

        button_done = Button(self.master, text="Done", command=self.done, height=3, width=15)
        button_repeat = Button(self.master, text="Play again", command=self.repeat, height=3, width=15)

        #add widgets to canvas
        self.canvas.create_window(330, 70, window=label_complete)
        self.canvas.create_window(330, 175, window=label_score)
        self.canvas.create_window(330, 265, window=label_suggestion)
        self.canvas.create_window(430, 390, window=button_done)
        self.canvas.create_window(230, 390, window=button_repeat)
        
    def done(self):
        self.canvas.destroy()
        OperatorSelection(self.master)

    def repeat(self):
        self.canvas.destroy()
        Quiz(self.master, self.operator, self.difficulty, self.add_scores, self.sub_scores, self.mult_scores, self.div_scores, self.final_scores, self.data_list, self.score_list)

    def back(self):
        self.canvas.destroy()
        TestSelection(self.master, self.operator, self.add_scores, self.sub_scores, self.mult_scores, self.div_scores, self.final_scores, self.data_list)

    #validate characters being inputted into entry
    def only_numbers(self, char):
        return char.isdigit()

    def record_score(self, score):
        if score > int(self.old_score):
            operator = self.operator
            difficulty = self.difficulty
            data = self.data_list
            if operator == "Addition":
                if difficulty == "1":
                    data[0][0] = score
                elif difficulty == "2":
                    data[0][1] = score
                else:
                    data[0][2] = score                   
            elif operator == "Subtraction":
                if difficulty == "1":
                    data[1][0] = score
                elif difficulty == "2":
                    data[1][1] = score
                else:
                    data[1][2] = score
            elif operator == "Multiplication":
                if difficulty == "1":
                    data[2][0] = score
                elif difficulty == "2":
                    data[2][1] = score
                else:
                    data[2][2] = score
            elif operator == "Division":
                if difficulty == "1":
                    data[3][0] = score
                elif difficulty == "2":
                    data[3][1] = score
                else:
                    data[3][2] = score
            else:
                if difficulty == "1":
                    data[4][0] = score
                elif difficulty == "2":
                    data[4][1] = score
                else:
                    data[4][2] = score
            write_file(data)

def read_file():
    data = [] #this will be used to store all of the file data in the program
    f = open("Score_Log.txt", "r")
    num_lines = sum(1 for line in open("Score_Log.txt", "r"))
    count = 0
    while count < num_lines:
        line = f.readline()
        line = line.strip()
        values = line.split(",") #values are now in a list
        data.append(values)
        count += 1
    f.close()
    #each row of the file is stored as a list inside this list
    #this will make it easier for me to work out which value corresponds to what instead of listing
    #the values from 0 to 15
    return data

def write_file(data):
    f = open("Score_Log.txt", "w")
    f.write(str(data[0][0])+","+str(data[0][1])+","+str(data[0][2])+"\n")
    f.write(str(data[1][0])+","+str(data[1][1])+","+str(data[1][2])+"\n")
    f.write(str(data[2][0])+","+str(data[2][1])+","+str(data[2][2])+"\n")
    f.write(str(data[3][0])+","+str(data[3][1])+","+str(data[3][2])+"\n")
    f.write(str(data[4][0])+","+str(data[4][1])+","+str(data[4][2])+"\n")
    f.close()
    read_file()

def clear_file():
    f = open("Score_Log.txt", "w")
    f.write("0,0,0\n")
    f.write("0,0,0\n")
    f.write("0,0,0\n")
    f.write("0,0,0\n")
    f.write("0,0,0\n")
    f.close()

def main():
    root = Tk()
    root.title("Maths Perfect")
    root.resizable(width=False, height=False)
    app = OperatorSelection(root)
    root.mainloop()
    
main()

