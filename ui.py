from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window set up
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # canvas for questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Text",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # button images
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # buttons
        self.true_button = Button(image=true_img, bg=THEME_COLOR, command=self.user_answered_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, bg=THEME_COLOR, command=self.user_answered_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_answered_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_answered_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
