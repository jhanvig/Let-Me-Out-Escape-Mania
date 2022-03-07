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

level_1= input("Click enter to proceed....")
if level_1 == "":
      
    script1=('''Darkness surrounds. As your senses slowly come to you,
    consciousness awakens. You blink as light rushes into your eye,
    and jolt up with adrenaline.You have no memory of where you came from or who you were with.You take in your surroundings.
    Pale white walls surround you,and yet, amidst this plainess,something stands out to you.
    A small glint of metal shone bright against the bareness of the wall.
    You walk closer to inspect it, and find a rotary dial telephone engraved into the wall.
    A note placed next to it has a riddle scribbled onto it in order to open the secret door.\n''')

print(script1)
      
#Instructions for level1
print('''Instructions for level 1:

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
    
def level1():
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
            print("The doors are now open, run as fast as you can!\n")
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

def level2():
    root = Tk()
    root.title('Riddle')


    my_label = Label(root, text="", font=("Helvetica", 48))
    my_label.pack(pady=20)

    global newlist
    newlist = []
    global riddle
    riddle = ["wake","you're","fantasy","this","life","get","back","reality"]

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
        messagebox.showinfo("GAME OVER!","You have successfully guessed all the words to solve the riddle, run towards the exit!\n")
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

level1()
if life>0:
    #LEVEL2
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
                    be that of a map of this building.You trace the lines on the map to find the words
                                                  ' you are here '
                                                   ' admin block '
                    After discerning your whereabouts move to find an exit on the map.You find it within seconds but a
                    strange looking note is seen on right stuck next to the bold lettering of the word "EXIT" on the map.
                    You squint at it to see: ekwaup uo'rey ni a tansfay hits flieis gte bckot reliaty\n''')
    print("INSTRUCTIONS FOR LEVEL 2: Find the word amongst the scrambled letters to get the sentence password required\n")
    print(script2)
    enter = input("Click Enter to continue:\n")
    #instructions for level 2
    # LEVEL2 CALL
    level2()
else:
    level1()

#LEVEL3
#Script
script3='''
You bore these words into your brain as you move out of the room towards the exit using the directions from the map as a guide.
You mutter these words to yourself so as to not forget and eventually you reach the exit passage way.\n'''

print(script3)
print('''The words guessed from the previous word puzzle are a part of the passcode to your freedom from the second level.
Some extra words have been added to complete the sentence:''')
enter = input("Click Enter to continue:\n")
    
def level3():
    root=Tk()
    root.title("NOTE")

    exlist = ["up","in","a","is","to"]
    newlist.extend(exlist)

    note = f'''In order to escape the asylum, enter the correct key/password using the words from the previous level:{newlist}
the sentence is: wake __ __ in __ fantasy. this __ life __ back to __'''
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
