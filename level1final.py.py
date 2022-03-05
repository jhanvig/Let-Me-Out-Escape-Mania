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
Script1=('''Darkness surrounds.As your senses slowly come to you,
      consciousness awakens. You blink as light rushes into your eye,
      and jolt up with adrenaline.You have no memory of where you came from or who you were with.You take in your surroundings.
      Pale white walls surround you,and yet, amidst this plainess,something stands out to you.
      A small glint of metal shone bright against the bareness of the wall.
      You walk closer to inspect it, and find a rotary dial telephone engraved into the wall.
      A note placed next to it has a riddle scribbled onto it in order to open the secret door.''')
#level 1


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

#level 2

script2=('''The doors are thrown open and you step out of the room into a unfamiliar surroundings.
Whitewashed walls entirely devoid of any sign of life and activity.
You take a deep breath and run down the hall not knowing wether the way to escape.
For a few minutes all you see are just blank white painted halls as you're running
Your heart thumps loudly against your chest making it difficult to breath and to think.
Your legs give out not being able to take you any further so you stop after a while to find yourself
infront of a peculiar door left ajar on your right.
You slip in quietly through the cracked open door to find yourself in a strangely lit
room containing monitors. On closer inspection you see that the monitors are relaying
the footage of the security cameras within in this place.

You look around the desks and monitors untill a large pinboard catches your eye.You walk toards
it to get a closer look. On looking closely you find that the largest poster seemed to
be that of a map of this building.You trace the lines on the map to find the words 'you are here'
                                admin block
After discerning your whereabouts move to find an exit on the map.You find it within seconds but a
strange looking note is seen on right stuck next to the bold lettering of the word "EXIT" on the map.You squint at it to see:"
''')
note="So you think you can escape?Its laughable,but I would like to see you try anyways.You might not be able to escape being so naive but let me give you a 'helpful nudge'"
text=Label(root, text=note,font=("calibri"),bg="black",fg="white",width=40,height=10,wraplength=100)
text.pack() 

#room has map.player finds out where they are and the exit on map has a post it note near it.
#note has clue ig

