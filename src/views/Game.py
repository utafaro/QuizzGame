import threading
import time
from tkinter import *
from store import store
from views.components.Questionnaire import Questionnaire
from views.theme import THEME
from views.components.Question import Question
from model.Timer import Timer


class Game:
    def __init__(self, document):

        self.document = document
        self.timer = 10 #take value of time in the creation of quizz
        self.finish = False
        self.score = 0



        self.__render()




    def exit(self):
        """Leave the Quizz at the end of it
        """
        # store.setScore(self.score)
        store.getApp().setCurrentFrame("score")
             
    def __render(self):

        def update_label(remaining):
            self.timer = remaining
            if remaining != 0:
                self.timer =remaining
                time.sleep(1)
                res = str(remaining)
                clock['text'] = f"Time left : {res} "
                t = threading.Thread(target=update_label, args=[remaining-1])
                t.start()
            else:
                self.timer = 1
                clock['text'] = "Time left : 1 "
                time.sleep(1)
                clock['text'] = "Time left : 0 "
                self.timer =0
                self.finish = True
                print(self.finish)
        # Il manque gestion des questions et points

        # questionnaire = Questionnaire(self.document,"test")
        # questionnaire.pack()
        points = 0
        bottomframe = Frame(self.document, bg=THEME["primary"])
        timeleft = self.timer
        clock = Label(bottomframe, text=f"Time left :{timeleft}     ", bg=THEME["primary"], font=('Inter', 40),
                      fg=THEME["blueTopbar"], borderwidth=1)
        score = Label(bottomframe, text=f"     Score : {points} points", bg=THEME["primary"], font=('Inter', 40),
                      fg=THEME["blueTopbar"])
        clock.grid(row=1, column=1)
        score.grid(row=1, column=5)
        bottomframe.grid(row=2, pady=230)
        update_label(self.timer)



        
