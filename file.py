from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn, width=10, bg="green4", fg="white", font=("ariel", 16, "bold"), activebackground="green3", activeforeground="white", relief=FLAT)
        next_button.place(x=350, y=380)

        quit_button = Button(gui, text="Quit", command=gui.destroy, width=5, bg="firebrick2", fg="white", font=("ariel", 16, " bold"), activebackground="firebrick3", activeforeground="white", relief=FLAT)
        quit_button.place(x=700, y=50)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60, font=('ariel', 16, 'bold'), anchor='w', bg="SlateGray1")
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(gui, text="Quizzler", width=50, bg="ivory2",fg="ivory4", font=("ariel", 20, "bold"))
        title.place(x=-20, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected, value=len(q_list)+1, font=("ariel", 14), bg="SlateGray1",activebackground="SlateGray1")

            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list


gui = Tk()
gui.geometry("800x450")
gui.maxsize(800, 450)
gui.minsize(800, 450)
gui.title("Quizzler")
gui.configure(background='SlateGray1')

canvas = Canvas(gui, width=800, height=450, bg="SlateGray1")
canvas.pack()

title = Label(canvas, text="Quizzler", width=50, bg="ivory2",fg="ivory4", font=("ariel", 20, "bold"))
title.place(x=-18, y=2)

quit_button = Button(canvas, text="Quit", command=gui.destroy, width=5, bg="firebrick2", fg="white", font=("ariel", 16, " bold"), activebackground="firebrick3",activeforeground="white", relief=FLAT)
quit_button.place(x=700, y=50)

choose_difficulty = Label(canvas, text="Choose Difficulty", width=50, bg="SlateGray1", font=("ariel", 20, "bold"))
choose_difficulty.place(x=-20, y=130)

def easy_dificulty():
    global question
    global options
    global answer
    canvas.destroy()
    with open('EasyQues.json') as f:
        data = json.load(f)
        question = data['question']
        options = data['options']
        answer = data['answer']
    dificulty_label = Label(gui, text="Difficulty : Easy", width=50, bg="SlateGray1", font=("ariel", 15, "bold"))
    dificulty_label.place(x=-176, y=60)
    Quiz()

def medium_dificulty():
    global question
    global options
    global answer
    canvas.destroy()
    with open('MedQues.json') as f:
        data = json.load(f)
        question = data['question']
        options = data['options']
        answer = data['answer']
    dificulty_label = Label(gui, text="Difficulty : Medium", width=50, bg="SlateGray1", font=("ariel", 15, "bold"))
    dificulty_label.place(x=-176, y=60)
    Quiz()

def hard_dificulty():
    global question
    global options
    global answer
    canvas.destroy()
    with open('HardQues.json') as f:
        data = json.load(f)
        question = data['question']
        options = data['options']
        answer = data['answer']
    dificulty_label = Label(gui, text="Difficulty : Hard", width=50, bg="SlateGray1", font=("ariel", 15, "bold"))
    dificulty_label.place(x=-176, y=60)
    Quiz()


easyBtn = Button(canvas, text="Easy", command=easy_dificulty, width=10, bg="green4", fg="white", font=("ariel", 16, "bold"), activebackground="green3", activeforeground="white", relief=FLAT)
easyBtn.place(x=100, y=200)

mediumBtn = Button(canvas, text="Medium", command=medium_dificulty, width=10, bg="green4", fg="white", font=("ariel", 16, "bold"), activebackground="green3", activeforeground="white", relief=FLAT)
mediumBtn.place(x=350, y=200)

hardBtn = Button(canvas, text="Hard", command=hard_dificulty, width=10, bg="green4", fg="white", font=("ariel", 16, "bold"), activebackground="green3", activeforeground="white", relief=FLAT)
hardBtn.place(x=600, y=200)

gui.mainloop()