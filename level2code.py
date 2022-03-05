from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox

root = Tk()
root.title('Riddle')


my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

global newlist
newlist = []
riddle = ["wake up","you're","in a","fantasy","this","is life","get","back to","reality"]

def shuffler():

    entry_answer.delete(0, END)

    answer_label.config(text='')
    try: 
        global word
        word = choice(riddle)
    except:
        funct()

    break_apart_word = list(word)
    shuffle(break_apart_word)
        
    global shuffled_word
    shuffled_word =  ''
    for letter in break_apart_word:
        shuffled_word += letter
    try:
        my_label.config(text=shuffled_word)
    except:
        print()
        
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
        global riddle
        k = riddle.pop(riddle.index(word))
        newlist.append(k)
            
    else:
        answer_label.config(text="Incorrect!!")


def funct():
    messagebox.showinfo("GAME OVER!","You have successfully guessed all the words to solve the riddle, run towards the exit!")
    root.destroy()


entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="Next Word", command=shuffler)
my_button.grid(row=0, column=1, padx=10)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)

shuffler()
root.mainloop()

#level 3

#Script

root=Tk()
root.title("NOTE")
note = f"In order to escape the asylum, enter the correct key/password using the words from the previous level:{newlist}"
text=Label(root,text=note,font=("Ariel"),bg="black",fg="white",width=30,height=10,wraplength=250)
text.pack()
ent = Entry(root, width=30, borderwidth=5)
ent.pack()

def cond():
    if ent.get()== key:
        messagebox.showinfo("YOU WON!!","You have now unlocked the door, doom awaits :)")
        root.destroy()

key = "wake up you're in a fantasy this is life get back to reality"

myButton = Button(root, text="Enter Password", command=cond)
myButton.pack()

    



