from tkinter import *
from views.theme import THEME

class Question(Frame):
    """IN: num : INT, parent: Frame, question : STRING, reponses : liste STRING,bonnereponse: STRING
    OUT: FRAME"""
    def __init__(self,parent,num,dico):
        self.parent = parent
        self.num=num
        self.question =dico["question"]
        self.reponses = dico["reponses"]
        self.bonneReponse=dico["bonneReponse"]
        self.__render()

    def __render(self):
        super().__init__(self.parent,bg = THEME["primary"],height = 720,
                         width=1080)
        
        
        but1  = Button(self, text=self.reponses[0],bg=THEME["lightBlue"], fg='white', 
                       activebackground='#052B71',  font=('Inter', 40),borderwidth=0,height = 1,width = 10)
        but2  = Button(self, text=self.reponses[1],bg=THEME["lightBlue"], fg='white', 
                       activebackground='#052B71',  font=('Inter', 40),borderwidth=0,height = 1,width = 10)
        but3  = Button(self, text=self.reponses[2],bg=THEME["lightBlue"], fg='white', 
                       activebackground='#052B71',  font=('Inter', 40),borderwidth=0,height = 1,width = 10)
        but4  = Button(self, text=self.reponses[3],bg=THEME["lightBlue"], fg='white', 
                       activebackground='#052B71',  font=('Inter', 40),borderwidth=0,height = 1,width = 10)
        
        but1.grid(row= 3, column=1,padx=5,pady=20)
        but2.grid(row= 3, column=4,padx=5,pady=20)
        but3.grid(row= 4, column=1,padx=5,pady=10)
        but4.grid(row= 4, column=4,padx=5,pady=10)
        
        lblNumQuestion = Label(self,text = f"Question {self.num}:",bg= THEME["blueTopbar"],fg= 'white',font=('Inter', 40))
        lblNumQuestion.grid(row=1,column=0)
        lblQuestion = Label(self,text = self.question,bg=THEME["primary"],fg=THEME["blueTopbar"],font=('Inter', 40))
        lblQuestion.grid(row=2,column=3)

      
    def pack(self):
        super().grid(row=1)