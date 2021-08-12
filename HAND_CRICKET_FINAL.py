from tkinter import *
from PIL import Image,ImageTk
import random

window = Tk()
window.title("HAND CRICKET")
window.geometry("499x500")
window.configure(bg='#fbd87f') 


img1 = r'1.png'
img2 = r'2.png'
img3 = r'3.png'
img4 = r'4.png'
img5 = r'5.png'
img6 = r'6.png'

images = [img1,img2,img3,img4,img5,img6]

img1 = ImageTk.PhotoImage(Image.open(images[0]))
img2 = ImageTk.PhotoImage(Image.open(images[1]))
img3 = ImageTk.PhotoImage(Image.open(images[2]))
img4 = ImageTk.PhotoImage(Image.open(images[3]))
img5 = ImageTk.PhotoImage(Image.open(images[4]))
img6 = ImageTk.PhotoImage(Image.open(images[5]))

IMAGES = [img1,img2,img3,img4,img5,img6]

lbl1 = Label(window,image=img1,bg='#fbd87f')
lbl2 = Label(window,image=img2,bg='#fbd87f')
lbl3 = Label(window,image=img3,bg='#fbd87f')
lbl4 = Label(window,image=img4,bg='#fbd87f')
lbl5 = Label(window,image=img5,bg='#fbd87f')
lbl6 = Label(window,image=img6,bg='#fbd87f')

MyCh = Label(window)
CompCh = Label(window)

global Score,runs,Runs,innings
runs = 0
Runs = 0
innings=0
Score = Label(window)

title = Label(window,text="HAND CRICKET",font=("Cambria",28),bg='#4CED69',relief=RIDGE,padx=123,pady=2).grid(row=0,column=0,columnspan=4) ##42f548 #4CED69

btn = Button(window)

def CompScore(IMAGES,Rand_img):
    return IMAGES.index(Rand_img)+1

def disable():
    Btn1['state'] = DISABLED
    Btn2['state'] = DISABLED
    Btn3['state'] = DISABLED
    Btn4['state'] = DISABLED
    Btn5['state'] = DISABLED
    Btn6['state'] = DISABLED


def Out_me():
    global out
    out = Label(window,text="YOU ARE OUT & YOUR TOTAL SCORE IS : {}".format(runs),bg='red',fg='white',font=("Cambria",16),padx=47,pady=2,relief=GROOVE)
    out.grid(row=5,column=0,columnspan=4)

def Out_Comp():
    global out
    out = Label(window,text="COMPUTER IS OUT & IT'S TOTAL SCORE IS : {}".format(runs),bg='red',fg='white',font=("Cambria",16),padx=30,pady=2,relief=GROOVE)
    out.grid(row=5,column=0,columnspan=4)

def _2nd_inn_bowl():
    global _2nd_Inn
    _2nd_Inn = Button(window,text="LET'S BOWL",bg='#d2dae2',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:Game('BOWL'))
    _2nd_Inn.grid(row=6,column=0,columnspan=4,ipady=4,ipadx=62)

def _2nd_inn_bat():
    global _2nd_Inn
    _2nd_Inn = Button(window,text="LET'S BAT",bg='#d2dae2',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:Game('BAT'))
    _2nd_Inn.grid(row=6,column=0,columnspan=4,ipady=4,ipadx=62)

def compTarget():
    global Target
    Target = Label(window,text="COMPUTER'S TARGET IS {}".format(runs+1),bg='#f9ff40',fg='#000',font=("Cambria",16),padx=120,pady=2,relief=GROOVE)
    Target.grid(row=5,column=0,columnspan=4)

def compScore_1():
    global Score
    Score = Label(window,text="COMPUTER IS BATTING, IT'S SCORE : {}".format(runs),bg='#6a9cfd',font=("Cambria",16),padx=64,pady=2,relief=GROOVE)
    Score.grid(row=5,column=0,columnspan=4)

def compScore_2():
    global Score
    Score = Label(window,text="COMPUTER IS BATTING, IT'S SCORE : {}".format(Runs),bg='#6a9cfd',font=("Cambria",16),padx=64,pady=2,relief=GROOVE)
    Score.grid(row=6,column=0,columnspan=4)

def myTarget():
    global Target
    Target = Label(window,text="YOUR TARGET IS {}".format(runs+1),bg='#f9ff40',fg='#000',font=("Cambria",16),padx=153,pady=2,relief=GROOVE)
    Target.grid(row=5,column=0,columnspan=4)

def myScore_1():
    global Score
    Score = Label(window,text='YOU ARE BATTING, YOUR SCORE : {}'.format(runs),bg='#6a9cfd',font=("Cambria",16),padx=77,pady=2,relief=GROOVE)
    Score.grid(row=5,column=0,columnspan=4)

def myScore_2():
    global Score
    Score = Label(window,text='YOU ARE BATTING, YOUR SCORE : {}'.format(Runs),bg='#6a9cfd',font=("Cambria",16),padx=77,pady=2,relief=GROOVE)
    Score.grid(row=6,column=0,columnspan=4)

def DRAW():
    global draw
    draw = Label(window,text="MATCH DRAWN",bg='red',fg='white',font=("Cambria",16),pady=2,relief=GROOVE)
    draw.grid(row=7,column=0,columnspan=4)

def youWon():
    global youwon
    youwon = Label(window,text="YOU WON, COMPUTER LOST THE GAME",bg='#4dff5b',fg='#000',font=("Cambria",16),padx=65,pady=2,relief=GROOVE)
    youwon.grid(row=7,column=0,columnspan=4)

def youLose():
    global youlose
    youlose = Label(window,text="YOU LOST, COMPUTER WON THE GAME",bg='red',fg='white',font=("Cambria",16),padx=65,pady=2,relief=GROOVE)
    youlose.grid(row=7,column=0,columnspan=4)

def RAND_IMG():
    global CompCh,Rand_img
    Rand_img = random.choice(IMAGES)
    Lbl1 = Label(window,image=Rand_img,bg='#fbd87f')

    CompCh.grid_forget()
    CompCh = Lbl1
    CompCh.grid(row=3,column=3,rowspan=2)

    score.grid_forget()

def Game(Res):
    global bTn1
    score.grid_forget()

    Btn1.grid_forget()
    Btn2.grid_forget()
    Btn3.grid_forget()
    Btn4.grid_forget()
    Btn5.grid_forget()
    Btn6.grid_forget()

    yc.grid_forget()
    cc.grid_forget()

    out.grid_forget()
    _2nd_Inn.grid_forget()

    score.grid_forget()
    Score.grid_forget()

    MyCh.grid_forget()
    CompCh.grid_forget()
    

    if Res == 'BOWL':
        bTn1 = Button(window,text="OKAY LET'S {}".format(Res),bg='#fea698',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:GAME('BOWL'))
    else:
        bTn1 = Button(window,text="OKAY LET'S {}".format(Res),bg='#fea698',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:GAME('BAT'))
    bTn1.grid(row=2,column=0,columnspan=4,ipady=4,ipadx=62)

    

def BTN1(CH):
    global MyCh,runs,Runs,innings,Rand_img

    MyCh.grid_forget()
    MyCh = lbl1
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img1:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()

        else:
            runs+=1
            Score.grid_forget()
            myScore_1()
            

    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img1:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()

        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()
            

    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img1:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon()
            elif runs == Runs:
                DRAW()
            
            disable()


        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()

    else:
        Target.grid_forget()

        if Rand_img == img1:
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose()
            elif runs == Runs:
                DRAW()

            disable()

        else:
            Runs+=1
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()

def BTN2(CH):

    global MyCh,CompCh,runs,_2nd_Inn,innings,Runs

    MyCh.grid_forget()
    MyCh = lbl2
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img2:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()

        else:
            runs+=2
            Score.grid_forget()
            myScore_1()

    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img2:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()

        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()

    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img2:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon()
            elif runs == Runs:
                DRAW()
            
            disable()

        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()

    else:
        Target.grid_forget()
        if Rand_img == img2:
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose()     
            elif runs == Runs:
                DRAW()

            disable()

        else:
            Runs+=2
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()
       

def BTN3(CH):

    global MyCh,CompCh,runs,_2nd_Inn,innings,Runs

    MyCh.grid_forget()
    MyCh = lbl3
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img3:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()
        else:
            runs+=3
            Score.grid_forget()
            myScore_1()

    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img3:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()
        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()

    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img3:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon()
            elif runs == Runs:
                DRAW()
            
            disable()


        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()

    else:
        Target.grid_forget()

        if Rand_img == img3:
            Score.grid_forget()   
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose()
            elif runs == Runs:
                DRAW()

            disable()

        else:
            Runs+=3
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()


def BTN4(CH):

    global MyCh,CompCh,runs,_2nd_Inn,innings,Runs

    MyCh.grid_forget()
    MyCh = lbl4
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img4:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()
        else:
            runs+=4
            Score.grid_forget()
            myScore_1()


    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img4:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()
        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()


    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img4:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon()
            elif runs == Runs:
                DRAW()
            
            disable()
        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()


    else:
        Target.grid_forget()

        if Rand_img == img4:
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose() 
            elif runs == Runs:
                DRAW()

            disable()
        else:
            Runs+=4
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()
        

def BTN5(CH):

    global MyCh,CompCh,runs,innings,Runs

    MyCh.grid_forget()
    MyCh = lbl5
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img5:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()
        else:
            runs+=5
            Score.grid_forget()
            myScore_1()


    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img5:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()
        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()


    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img5:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon()   
            elif runs == Runs:
                DRAW()
            
            disable()

        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()


    else:
        Target.grid_forget()

        if Rand_img == img5:
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose()
            elif runs == Runs:
                DRAW()

            disable()

        else:
            Runs+=5
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()
        

def BTN6(CH):

    global MyCh,CompCh,runs,_2nd_Inn,innings,Runs

    MyCh.grid_forget()
    MyCh = lbl6
    MyCh.grid(row=3,column=2,rowspan=2)

    RAND_IMG()

    if CH == 'BAT' and innings%2 == 1:
        if Rand_img == img6:
            Score.grid_forget()
            Out_me()
            _2nd_inn_bowl()
            disable()
        else:
            runs+=6
            Score.grid_forget()
            myScore_1()

    elif CH == 'BOWL' and innings%2 == 1:
        if Rand_img == img6:
            Score.grid_forget()
            Out_Comp()
            _2nd_inn_bat()
            disable()
        else:
            runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compScore_1()


    elif CH == 'BOWL' and innings%2 == 0:
        Target.grid_forget()

        if Rand_img == img6:
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs > Runs:
                youWon() 
            elif runs == Runs:
                DRAW()

            disable()

        else:
            Runs+=CompScore(IMAGES,Rand_img)
            Score.grid_forget()
            compTarget()
            compScore_2()

            if runs+1 <= Runs:
                youLose()
                disable()

    else:
        Target.grid_forget()

        if Rand_img == img6:
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs > Runs:
                youLose() 
            elif runs == Runs:
                DRAW()

            disable()


        else:
            Runs+=6
            Score.grid_forget()
            myTarget()
            myScore_2()

            if runs+1 <= Runs:
                youWon()
                disable()



def GAME(choice):
    global score,Btn1,Btn2,Btn3,Btn4,Btn5,Btn6,yc,cc,innings,Target
    innings += 1
    Choice = choice
    btn1.grid_forget()

    Btn1 = Button(window,text='1',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN1(Choice))
    Btn1.grid(row=2,column=0,ipadx=38,ipady=9)
    Btn2 = Button(window,text='2',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN2(Choice))
    Btn2.grid(row=2,column=1,ipadx=38,ipady=9)
    Btn3 = Button(window,text='3',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN3(Choice))
    Btn3.grid(row=3,column=0,ipadx=38,ipady=9)
    Btn4 = Button(window,text='4',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN4(Choice))
    Btn4.grid(row=3,column=1,ipadx=38,ipady=9)
    Btn5 = Button(window,text='5',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN5(Choice))
    Btn5.grid(row=4,column=0,ipadx=38,ipady=9)
    Btn6 = Button(window,text='6',font=('Cambria',16),bg='#fea698', activebackground='#fea698',relief=GROOVE,borderwidth=4,command=lambda:BTN6(Choice))
    Btn6.grid(row=4,column=1,ipadx=38,ipady=9)

    yc = Label(window,text='YOUR\nCHOICE',font=('Cambria',14),relief=GROOVE,bg='lightgrey')#lightgrey
    yc.grid(row=2,column=2,ipady=7,ipadx=26)
    cc = Label(window,text='COMPUTER\nCHOICE',font=('Cambria',14),relief=GROOVE,bg='lightgrey')
    cc.grid(row=2,column=3,ipady=7,ipadx=26)

    if choice == 'BAT' and innings == 1:
        score = Label(window,text='YOU ARE BATTING, YOUR SCORE : {}'.format(0),bg='#6a9cfd',font=("Cambria",16),pady=2,padx=80,relief=GROOVE)
    elif choice == 'BOWL' and innings == 1:
        score = Label(window,text="COMPUTER IS BATTING , IT'S SCORE : {}".format(0),bg='#6a9cfd',font=("Cambria",16),padx=67,pady=2,relief=GROOVE)
    elif choice == 'BOWL' and innings == 2:
        score = Label(window,text="COMPUTER IS BATTING , IT'S SCORE : {}".format(0),bg='#6a9cfd',font=("Cambria",16),padx=67,pady=2,relief=GROOVE)
        Target = Label(window,text="COMPUTER'S TARGET IS {}".format(runs+1),bg='#f9ff40',fg='#000',font=("Cambria",16),padx=120,pady=2,relief=GROOVE)
        Target.grid(row=5,column=0,columnspan=4)
    else:
        score = Label(window,text='YOU ARE BATTING, YOUR SCORE : {}'.format(0),bg='#6a9cfd',font=("Cambria",16),pady=2,padx=80,relief=GROOVE)
        Target = Label(window,text="YOUR TARGET IS {}".format(runs+1),bg='#f9ff40',fg='#000',font=("Cambria",16),padx=153,pady=2,relief=GROOVE)
        Target.grid(row=5,column=0,columnspan=4)
        
    score.grid(row=6,column=0,columnspan=4)
    

def BAT_BALL(RES):
    global btn1
    lbl.grid_forget()
    bat_btn.grid_forget()
    bowl_btn.grid_forget()

    lbl3 = Label(window,text="YOU WON THE TOSS & DECIDED TO {}".format(RES),bg='#6a9cfd',font=("Cambria",16),pady=2,relief=GROOVE)
    
    if RES == 'BAT':
        lbl3.grid(row=1,column=0,columnspan=4,ipady=4,ipadx=62)
    else:
        lbl3.grid(row=1,column=0,columnspan=4,ipady=4,ipadx=52)

    btn1 = Button(window,text="OKAY LET'S {}".format(RES),bg='#fea698', activebackground='#fea698',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:GAME(RES))
    btn1.grid(row=2,column=0,columnspan=4,ipady=4,ipadx=62)


def TOSS(res):
    global lbl,bat_btn,bowl_btn,btn1
    Toss.grid_forget()
    even_btn.grid_forget()
    odd_btn.grid_forget()

    c = ['ODD','EVEN']
    ch = ['BAT','BOWL']
    choice = random.choice(c)
    choice1 = random.choice(ch)

    if res==choice:
        
        lbl = Label(window,text="YOU WON THE TOSS. YOUR CHOICE : ",bg='#6a9cfd',font=("Cambria",16),pady=2)
        lbl.grid(row=1,column=0,columnspan=2,ipady=4)

        bat_btn = Button(window,text='BAT',font=('Cambria',15),bg='#6a9cfd',activebackground='#6a9cfd',relief=GROOVE,command=lambda:BAT_BALL(ch[0]))
        bat_btn.grid(row=1,column=2,ipadx=8,ipady=1)

        bowl_btn = Button(window,text='BOWL',font=('Cambria',15),bg='#6a9cfd',activebackground='#6a9cfd',relief=GROOVE,command=lambda:BAT_BALL(ch[1]))
        bowl_btn.grid(row=1,column=3,ipadx=6,ipady=1)

    else:

        lbl = Label(window,text="YOU LOST THE TOSS & COMPUTER DECIDED TO {}".format(choice1),bg='#6a9cfd',font=("Cambria",15),relief=GROOVE)
        
        if choice1 == 'BAT':
            lbl.grid(row=1,column=0,columnspan=4,ipady=3,ipadx=19)
            btn1 = Button(window,text="OKAY LET'S BOWL",bg='#fea698', activebackground='#fea698',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:GAME('BOWL'))
        else:
            lbl.grid(row=1,column=0,columnspan=4,ipady=3,ipadx=10)
            btn1 = Button(window,text="OKAY LET'S BAT",bg='#fea698', activebackground='#fea698',font=("Cambria",16),pady=2,relief=GROOVE,command=lambda:GAME('BAT'))

        btn1.grid(row=2,column=0,columnspan=4,ipady=4,ipadx=62)



Toss = Label(window,text='EVEN OR ODD    ---> ',bg='#6a9cfd',font=("Cambria",20),pady=3,padx=33,relief=GROOVE)
Toss.grid(row=1,column=0,columnspan=2,ipady=3)

even_btn = Button(window,text='EVEN',font=('Cambria',16),bg='#6a9cfd',activebackground='#6a9cfd',relief=GROOVE,command=lambda:TOSS('EVEN')) #0DB4F0 #4287f5
even_btn.grid(row=1,column=2,ipadx=14,ipady=2)

odd_btn = Button(window,text='ODD',font=('Cambria',16),bg='#6a9cfd',activebackground='#6a9cfd',relief=GROOVE,command=lambda:TOSS('ODD'))
odd_btn.grid(row=1,column=3,ipadx=16,ipady=2)

window.mainloop()