import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = tk.Tk()
        self.window.title = "Quiz App"
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(
            text="Score: 0", font=("Arial", 12, "italic"), bg=THEME_COLOR, fg="#FFFFFF"
        )
        self.score_label.grid(column=1, row=0, sticky="ne")

        self.canvas = tk.Canvas(
            width=300, height=250, bg="#FFFFFF", highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Placeholder Text",
            fill=THEME_COLOR,
            width=290,
            font=("Arial", 14, "italic"),
        )
        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=(20, 20),
        )

        self.check_mark = tk.PhotoImage(file="images/true.png")
        self.cross_mark = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(
            image=self.check_mark,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_check,
        )
        self.false_button = tk.Button(
            image=self.cross_mark,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_check,
        )
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="#FFFFFF")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(
                text=f"Score: {self.quiz.score} / {len(self.quiz.question_list)}"
            )
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(
                self.question_text, text="There are no more questions in the quiz!"
            )

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#29B677")
        else:
            self.canvas.config(bg="#EE665D")
        self.window.after(500, self.get_next_q)
