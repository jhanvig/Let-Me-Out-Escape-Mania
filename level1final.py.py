from tkinter import *
from tkinter import messagebox
import random
import csv

print("LET ME OUT: ESCAPE MANIA")

#csv file to store player data
name = input('''WELCOME, TO LET ME OUT: ESCAPE MANIA!!!

Please enter your credentials in order to save your stats and to compete with others from your country!

Player Name:''')

age = input("Age:")

country = input("Country:")

file1 = open("C:\\Users\\Jhan\\Desktop\\coding work\\cs project\\statistic.csv","a",newline="\r\n")

writobj= csv.writer(file1)

writobj.writerow([name,age,country])

file1.close()

#SCRIPT

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
