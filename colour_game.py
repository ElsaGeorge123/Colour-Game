import tkinter
import random
colours=["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple","Brown"]
score=0
timeleft=30

def startgame(event):
    if timeleft==30:
        countdown()
    nextcolour()
def nextcolour():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text="Score:" + str(score))
                     
                     

#works
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timelabel.config(text="Time Left:"+str(timeleft))
        timelabel.after(1000, countdown)
        
root=tkinter.Tk()
root.title("COLOUR GAME")
root.geometry("375x200")
instructions=tkinter.Label(root, text="Type in the colour"
                           "of the words and not the text", font=('Helvetica',12))
instructions.pack()
scorelabel=tkinter.Label(root, text="Press enter to start", font=("Helvetica",12))
scorelabel.pack()

timelabel=tkinter.Label(root, text="Time Left:" + str(timeleft), font=("Helvetica",12))
timelabel.pack()

label=tkinter.Label(root, font=("Helvetica", 60))
label.pack()

e=tkinter.Entry(root)
root.bind('<Return>', startgame)
e.pack()
e.focus_set()
root.mainloop()
