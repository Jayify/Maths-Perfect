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


main_window = Tk()
main_window.title("Maths Perfect")
canvas = Canvas(main_window, width=660, height=460, bg="lightblue")
canvas.grid()
operator_selection()

