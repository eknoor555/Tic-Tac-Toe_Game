from tkinter import *
import random

def next_turn(row,col):
    global player#here we need to access the player so we use global player
    if buttons[row][col]['text']=="" and check_winner() is False:#if the place is empty and there is no winner
        if player==players[0]:
            buttons[row][col]['text']=player#we are checking if after placing text of our player on the button that we click
            if check_winner() is False:#if there is no winner we will give next chance to another player
                player=players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][col]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":#if one row is completed with same symbol it means somebody won
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True
    for col in range(3):
        if buttons[0][col]['text']==buttons[1][col]['text']==buttons[2][col]['text']!="":#if one column is completed with same symbol it means somebody won
            buttons[0][col].config(bg="red")
            buttons[1][col].config(bg="red")
            buttons[2][col].config(bg="red")
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":#here we are checking if diagonal
        buttons[0][0].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][2].config(bg="red")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":  # here we are checking if diagonal
        buttons[0][2].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][0].config(bg="red")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"
    else:
        return False

def empty_spaces():#to check if there if empty spaces left
    spaces=9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    player=random.choice(players)
    label.config(text=player+" turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="",bg="#F0F0F0")

window=Tk()
window.title("Tic-Tac-Toe")#it will give title to window
players=["x","o"]
player=random.choice(players)#it will begin randomly from anyone from players list
buttons=[[0,0,0],#Now we require to have Nine buttons so we are initializing it with zeros
         [0,0,0],
         [0,0,0]]
label=Label(text=player+ "turn",font=("Verdana",40))#we need label to see whose turn is this
label.pack(side="top")
reset_button=Button(text="restart",font=("Verdana",20),command=new_game)#everytime we click on restart button it will call the function new_game
reset_button.pack(side="top")
frame=Frame(window)
frame.pack()
for row in range(3):
    for col in range(3):
        buttons[row][col]=Button(frame,text="",font=("Verdana",40),width=5,height=2,command=lambda row=row,col=col:next_turn(row,col))
        buttons[row][col].grid(row=row,column=col)
window.mainloop()


