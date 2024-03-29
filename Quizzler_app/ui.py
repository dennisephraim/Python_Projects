from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='', font=('Arial', 20, 'italic'), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        
        self.score_label.grid(row=0, column=1)

        # Buttons
        self.t_img = PhotoImage(file= 'Quizzler_app/images/true.png')
        self.true_button = Button(image=self.t_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)

        self.f_img = PhotoImage(file= 'Quizzler_app/images/false.png')
        self.false_button = Button(image=self.f_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():            
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()        
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_clicked(self):        
        self.give_feedback(self.quiz.check_answer('True'))
        
    def false_clicked(self):        
        self.give_feedback(self.quiz.check_answer('False'))

    

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
        
        


