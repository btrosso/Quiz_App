from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        # window set up
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # canvas for questions
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)

        # buttons
        self.true_button = Button(image="images/true.png")
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image="images/false.png")
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()