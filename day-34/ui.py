from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15)
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Qeuestion here", font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=true_btn_img, highlightthickness=0, command=self.is_answer_true
        )
        self.true_btn.grid(row=2, column=1)

        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_btn_img, highlightthickness=0, command=self.is_answer_false
        )
        self.false_btn.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've finished the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_answer_true(self):
        is_correct = self.quiz_brain.check_answer(True)
        self.give_feedback(is_correct)

    def is_answer_false(self):
        is_correct = self.quiz_brain.check_answer(False)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
