from tkinter import *
from tkinter import messagebox
import random
from random import choice
from random import shuffle
import csv

print("LET ME OUT: ESCAPE MANIA")

#csv file to store player data
name = input('''WELCOME, TO LET ME OUT: ESCAPE MANIA!!!

Please enter your credentials in order to save your stats and to compete with others from your country!

Player Name:''')

age = input("Age:")

country = input("Country:")

file1 = open("C:\\Users\\Jhan\\Desktop\\coding work\\cs project\\statistics.csv","a",newline="\r\n")

writobj= csv.writer(file1)

writobj.writerow([name,age,country])

file1.close()

#SCRIPT
def level1():
    level_1= input("Click enter to proceed....")
    if level_1 == "":
        #Instructions for level1
        print('''
    Instructions for level 1:

    The code to be entered in the rotary dial telephone in order to escape this room is a four digit code
    consisting of the numbers 1-8.

    The code must be written without any spaces (i.e: xyaz). You shall be provided with four chances to input the code correctly,
    or the level shall restart. Good luck!!\n''')
        
        action=input("Enter <pick> to pick up the phone:\n")

    #Initializing tkinter root
    root=Tk()
    root.title("Escape door")

    for i in range(0,3):
        a=int(random.randrange(2,5))
        firstnum='c'*a
        b=str(a)
        c=str(a*2)
        d=str(a-1)
        code=str(a)+b+c+d
        life=4


    clue = f"I am a code, hard to decipher. My first number is hidden in this ({firstnum}) clue. My second number is a copycat, and favours the first. My third number always likes his pride to be twice higher than the second. And the fourth number always falls a step below the first.What is the code? You have 4 lives."
        
     
    text=Label(root, text=clue,font=("Calibri"),bg="black",fg="white",width=100,height=20,wraplength=500)
    text.pack()
          
    ent = Entry(root, width=30, borderwidth=5)
    ent.pack()

    #check if input = to the code
    def Tru(x):
        if x == code:
            return True
        
    #display
    def myClick():
        if Tru(ent.get()) and life==4:
            retry="You have successfully entered the code, you have 4 lives"
        else:
            retry="Try again, you have "+str(life-1)+" lives left"
        myLabel = Label(root,text=retry)
        myLabel.pack()
        funct(ent.get())

    #to loop till life = 0
    def funct(x):
        global life
        if x == code: 
            messagebox.showinfo("GAME OVER","The doors are now open, run as fast as you can!")
            root.destroy()
            print("You have successfully entered the code.")
            print("The doors are now open, run as fast as you can!")
        else:
            life-=1
            if life>0:
                myButton = Button(root, text="Click to confirm", command = myClick)
                myButton.pack()

            else:
                messagebox.showinfo("Game over!!","Restart the game to begin!")
                root.destroy()

    #Button  
    myButton = Button(root, text="Click to confirm", command = myClick)
    myButton.pack()

    root.mainloop()

level1()

#LEVEL2
def level2():
    root = Tk()
    root.title('Riddle')


    my_label = Label(root, text="", font=("Helvetica", 48))
    my_label.pack(pady=20)

    global newlist
    newlist = []
    global riddle
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

level2()
#LEVEL3

#Script
def level3():
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
    root.mainloop()
level3()
