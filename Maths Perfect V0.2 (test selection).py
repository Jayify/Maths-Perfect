from tkinter import *

#this class creates the operator selection page or main page where the student selects which operator they want to be tested on
class operator_selection():
    def __init__(self):
        height = 8
        width = 18
        label_title = Label(main_window, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        label_text = Label(main_window, text="Welcome to Maths Perfect! Please select a section to continue:", font="sample 14", bg="lightblue")
        button_add = Button(main_window, text="ADDITION", command=lambda: self.load_next(), height=height, width=width)
        button_sub = Button(main_window, text="SUBTRACTION", command=lambda: self.load_next(), height=height, width=width)
        button_mult = Button(main_window, text="MULTIPLICATION", command=lambda: self.load_next(), height=height, width=width)
        button_div = Button(main_window, text="DIVISION", command=lambda: self.load_next(), height=height, width=width)
        button_final = Button(main_window, text="FINAL TEST", command=lambda: self.load_next(), height=8, width=87)

        #add to buttons and labels to canvas
        #labels
        canvas.create_window(330, 41, window=label_title)
        canvas.create_window(330, 105, window=label_text)
        #operator buttons
        canvas.create_window(90, 230, window=button_add)
        canvas.create_window(250, 230, window=button_sub)
        canvas.create_window(410, 230, window=button_mult)
        canvas.create_window(570, 230, window=button_div)
        canvas.create_window(330, 380, window=button_final)

    def load_next(self):
        canvas.delete("all")
        print("a")
        test_selection()
      
#this class creates the test selection page where the student selects the level they want
class test_selection():
    def __init__(self):
        height = 17
        width = 25
        title = Label(main_window, text="Maths Perfect", font=("Script MT Bold", 46, "bold"), bg="lightblue")
        text = Label(main_window, text="Please select a section to continue:", font="sample 14", bg="lightblue")

        score_1 = Label(main_window, text="Score: {}/10", font="sample 12", bg="lightblue")
        score_2 = Label(main_window, text="Score: {}/10", font="sample 12", bg="lightblue")
        score_3 = Label(main_window, text="Score: {}/10", font="sample 12", bg="lightblue")

        button_t1 = Button(main_window, text="TEST 1", command=self.print_e, height=height, width=width)
        button_t2 = Button(main_window, text="TEST 1", command=self.print_e, height=height, width=width)
        button_t3 = Button(main_window, text="TEST 1", command=self.print_e, height=height, width=width)
        
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


main_window = Tk()
main_window.title("Maths Perfect")
canvas = Canvas(main_window, width=660, height=460, bg="lightblue")
canvas.grid()
operator_selection()

