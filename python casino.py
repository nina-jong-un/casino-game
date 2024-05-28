from tkinter import *
import pygame
import time
import random

root = Tk()
root.title("scientificoders")
root.geometry("1000x500")
root.configure(background="black")

balance = 1000
#################################################################################################
def destroy_rl_main():
    e_choose.destroy()
    Choose.destroy()
    Congratulations.destroy()
    num_label.destroy()
    Current_balance_rl.destroy()
    Current_balance_rl1.destroy()
    Start_Btn.destroy()
    Choose1.destroy()
    Choose2.destroy()
    e.destroy()
    Bet.destroy()
    Try.destroy()
    Start_Btn1.destroy()
    Start_Btn_rl.destroy()
    my_entry.destroy()
    Back_Btn.destroy()
    main()

def bet_try_rl():
    global e_choose,bet_guess,Choose,Start_Btn

    try:
        bet_guess = int(e.get())
    except ValueError:
        bet_guess = 100

    if(bet_guess<=balance):
        Choose = Label(root,text="On How Many No. Do You Want To Bet [1-36] :- ",bg="black",fg="green")
        Choose_Tuple = ("Arial",20,"bold")
        Choose.configure(font=Choose_Tuple)
        Choose.grid(row=6,column=1,pady=5,columnspan=10)

        e_choose = Entry(root,width=10,bg="light blue",fg="blue")
        e_choose.grid(row=6,column=13,pady=5,columnspan=5)

        Start_Tuple = ("Arial",10,"bold")

        Start_Btn = Button(root,text="Done",background="yellow",foreground="red",font= Start_Tuple,command=bet_input)
        Start_Btn.grid(column=19,row=6,columnspan=5)

def bet_input():
    global my_entry,choosen_num,Choose2,Choose1,Start_Btn_rl,moneynum
    try:
        choosen_num = int(e_choose.get())
    except ValueError:
        choosen_num = 0

    moneynum = int(bet_guess/choosen_num)
    Choose1 = Label(root,text=f"Bet on Each Number :- ${moneynum}",bg="black",fg="light blue")
    Choose_Tuple = ("Arial",20,"bold")
    Choose1.configure(font=Choose_Tuple)
    Choose1.grid(row=7,column=1,padx=0,pady=5,columnspan=10)

    Choose2 = Label(root,text="Enter No's Separated by Comma :-             ",bg="black",fg="green")
    Choose_Tuple = ("Arial",20,"bold")
    Choose2.configure(font=Choose_Tuple)
    Choose2.grid(row=8,column=1,padx=0,pady=5,columnspan=10)

    my_entry = Entry(root,width=15,bg="light blue",fg="blue")
    my_entry.grid(row=8,column=10,padx=5,pady=10)

    Start_Tuple = ("Arial",11,"bold")
    Start_Btn_rl = Button(root,text="Done",background="yellow",foreground="red",font=Start_Tuple,command=final_check)
    Start_Btn_rl.grid(column=12,row=8,columnspan=5,padx=5,pady=10)

def final_check():

    global num_label,Congratulations,Current_balance_rl1,balance,Current_balance_rl
    my_entry_rl = (my_entry.get())
    rl_list = my_entry_rl.split(",")
    try:
        for i in range(0,len(rl_list)):
            rl_list[i] = int(rl_list[i])
    except:
        print("")

    num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    num_rl = random.choice(num_list)
    num_label = Label(root,text=f"Computer choosed :- {num_rl}",background="black",foreground="light blue")
    num_tuple = ("Arial",30,"bold")
    num_label.configure(font=num_tuple)
    num_label.grid(row=9,column=2,columnspan=10)

    for i in range(choosen_num):
        if (rl_list[i] == num_rl):
            Congratulations = Label(root,text=f"CONGO YOU WON :- ${moneynum*20}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=10,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.init()
            pygame.mixer.music.load("./C:\\Users\\prefe\\Downloads\\sounds\\Winning.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_rl.destroy()
            balance = (balance -bet_guess)+moneynum*20
            Current_balance_rl1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_rl1.configure(font=Balance_tuple)
            Current_balance_rl1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)
            break

        elif((i == choosen_num-1) and rl_list[i] != num_rl):
            Congratulations = Label(root,text=f"OOPS ! You Lost :- ${bet_guess}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=10,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.init()
            pygame.mixer.music.load("./C:\\Users\\prefe\\Downloads\\sounds\\Lost.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_rl.destroy()
            balance = balance - bet_guess
            Current_balance_rl1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_rl1.configure(font=Balance_tuple)
            Current_balance_rl1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)
            break





def ROULETTE():

    global Current_balance_rl,e,Bet,Back_Btn,Try,Start_Btn1

    rules_btn.destroy()
    guess_btn.destroy()
    seven_btn.destroy()
    Welcome.destroy()
    Current_balance_main.destroy()
    roulette_btn.destroy()

    Back_Btn = Button(root,text="Back",background="yellow",foreground="red",bd=5,height=1,width=4,command=destroy_rl_main)
    Back_Tuple = ("Arial",15)
    Back_Btn.configure(font=Back_Tuple)
    Back_Btn.grid(row=0,column=0,padx=10,pady=10)

    Current_balance_rl= Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_rl.configure(font=Balance_tuple)
    Current_balance_rl.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=5)

    Try = Label(root,text="Let's Try Your Luck !!",bg="black",fg="yellow")
    Try_Tuple = ("Arial",50,"bold")
    Try.configure(font=Try_Tuple)
    Try.grid(row=3,column=1,padx=60,pady=5,columnspan=30,rowspan=2)

    Bet = Label(root,text="Place Your Bet :-- ",bg="black",fg="green")
    Bet_tuple = ("Arial",20,"bold")
    Bet.configure(font=Bet_tuple)
    Bet.grid(row=5,column=1,pady=5,columnspan=10)

    e = Entry(root,width=20,bg="light blue",fg="blue")
    e.grid(row=5,column=5,pady=5,columnspan=10)

    Start_Tuple = ("Arial",10,"bold")
    Start_Btn1 = Button(root,text="Place",background="yellow",foreground="red",font=Start_Tuple,bd=3,command=bet_try_rl)
    Start_Btn1.grid(column=12,row=5,columnspan=5)






##########################################################################################
def destroy_call_seven():
    num_label.destroy()
    Congratulations.destroy()
    Play_again_btn.destroy()
    Current_balance_seven.destroy()
    Current_balance_seven1.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Back_Btn.destroy()
    Start_Btn.destroy()
    SEVEN()

def destroy_to_main_seven():
    num_label.destroy()
    Congratulations.destroy()
    Play_again_btn.destroy()
    Current_balance_seven.destroy()
    Current_balance_seven1.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Back_Btn.destroy()
    Start_Btn.destroy()
    main()

def bet_try_seven():
    global balance,num_label,Congratulations,Play_again_btn,Current_balance_seven1
    time.sleep(2)
    try:
        bet_guess = int(e.get())
    except ValueError:
        bet_guess = 100

    if(bet_guess<=balance):
        num_list = [0,1,2,3,4,5,6,7,8,9]
        num1 = random.choice(num_list)
        num2 = random.choice(num_list)
        num3 = random.choice(num_list)


        num_label = Label(root,text=f"{num1}    {num2}    {num3}",background="black",foreground="yellow")
        num_tuple = ("Arial",55,"bold")
        num_label.configure(font=num_tuple)
        num_label.grid(row=6,column=4,padx=10,pady=10,columnspan=10)

        if(num1==7 and num2==7 and num3==7):
            Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*10}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.music.load("Songs/Winning.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_seven.destroy()
            balance = balance + bet_guess*9
            Current_balance_seven1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_seven1.configure(font=Balance_tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

        elif (num1==num2 and num2==num3 and num3==num1):
            Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*5}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.music.load("Songs/Winning.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_seven.destroy()
            balance = balance + bet_guess*4
            Current_balance_seven1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_seven1.configure(font=Balance_tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

        elif (num1%2 == 0 and num2%2==0 and num3%2 ==0):
            Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*2}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.music.load("Songs/Winning.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_seven.destroy()
            balance = balance + bet_guess
            Current_balance_seven1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_seven1.configure(font=Balance_tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

        elif (num1%2 != 0 and num2%2!=0 and num3%2 !=0):
            Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*2}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.init()
            pygame.mixer.music.load("C:\\Users\\prefe\\Downloads\\sounds\\Winning.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_seven.destroy()
            balance = balance + bet_guess
            Current_balance_seven1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_seven1.configure(font=Balance_tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

        else:
            Congratulations = Label(root,text=f"OOPS ! You Lost :- ${bet_guess}",background="black",foreground="orange")
            Congo_Tuple = ("Arial",40,"bold")
            Congratulations.configure(font=Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady=25,columnspan=35)
            pygame.mixer.init()
            pygame.mixer.music.load("C:\\Users\\prefe\\Downloads\\sounds\\Lost.wav")
            pygame.mixer.music.play(loops=0)
            Current_balance_seven.destroy()
            balance = balance - bet_guess
            Current_balance_seven1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
            Balance_tuple = ("Arial",25)
            Current_balance_seven1.configure(font=Balance_tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)
    
        Play_tuple = ("Arial",20,"bold")
        Play_again_btn = Button(root,text="Play Again",background="blue", foreground="light blue",font=Play_tuple,command=destroy_call_seven)
        Play_again_btn.grid(row=8,column=4,columnspan=10,padx=10)
            




def SEVEN():
    global e,Current_balance_seven,Back_Btn,Bet,Start_Btn,Try
    rules_btn.destroy()
    guess_btn.destroy()
    seven_btn.destroy()
    Welcome.destroy()
    Current_balance_main.destroy()
    roulette_btn.destroy()

    Back_Btn = Button(root,text="Back",background="yellow",foreground="red",bd=5,height=1,width=4,command=destroy_to_main_seven)
    Back_Tuple = ("Arial",15)
    Back_Btn.configure(font=Back_Tuple)
    Back_Btn.grid(row=0,column=0,padx=10,pady=10)

    Current_balance_seven = Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_seven.configure(font=Balance_tuple)
    Current_balance_seven.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=5)

    Try = Label(root,text="Let's Try Your Luck !!",bg="black",fg="yellow")
    Try_Tuple = ("Arial",50,"bold")
    Try.configure(font=Try_Tuple)
    Try.grid(row=3,column=1,padx=60,pady=5,columnspan=30,rowspan=2)

    Bet = Label(root,text="Place Your Bet :-- ",bg="black",fg="green")
    Bet_tuple = ("Arial",20,"bold")
    Bet.configure(font=Bet_tuple)
    Bet.grid(row=5,column=1,pady=5,columnspan=10)

    e = Entry(root,width=20,bg="light blue",fg="blue")
    e.grid(row=5,column=5,pady=5,columnspan=10)

    Start_Tuple = ("Arial",10,"bold")
    Start_Btn = Button(root,text="Place",background="yellow",foreground="red",font=Start_Tuple,bd=3,command=bet_try_seven)
    Start_Btn.grid(column=12,row=5,columnspan=5)
#GUESS THE NUMBER GAME

def destroy_call_guess():
    e_choose.destroy()
    Choose.destroy()
    Congratulations.destroy()
    num_label.destroy()
    Current_balance_guess1.destroy()
    Play_again_btn.destroy()
    Current_balance_guess.destroy()
    Back_Btn.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Start_Btn.destroy()
    Start_Btn1.destroy()
    GUESS()

def destroy_call_main():
    e_choose.destroy()
    Choose.destroy()
    Congratulations.destroy()
    num_label.destroy()
    Current_balance_guess1.destroy()
    Play_again_btn.destroy()
    Current_balance_guess.destroy()
    Back_Btn.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Start_Btn.destroy()
    Start_Btn1.destroy()
    main()



def bet_choosed():
    global balance,Congratulations,Current_balance_guess1,num_label,Play_again_btn
    try:
        choosen_num = int(e_choose.get())
    except ValueError:
        choosen_num = 0

    num_list = [1,2,3,4,5]
    num = random.choice(num_list)
    num_label = Label(root,text=f"Computer choosed :- {num}",background="black",foreground="light blue")
    num_tuple = ("Arial",45,"bold")
    num_label.configure(font=num_tuple)
    num_label.grid(row=7,column=1,padx=10,pady=10,columnspan=30)
    time.sleep(2)

    if(choosen_num==num):
        Congratulations = Label(root,text=f"CONGO YOU WON :- ${bet_guess*2}",background="black",foreground="orange")
        Congo_Tuple = ("Arial",40,"bold")
        Congratulations.configure(font=Congo_Tuple)
        Congratulations.grid(row=8,column=2,padx=10,pady=10,columnspan=35)
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\prefe\\Downloads\\sounds\\Winning.wav")
        pygame.mixer.music.play(loops=0)
        Current_balance_guess.destroy()
        balance = balance + bet_guess
        Current_balance_guess1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
        Balance_tuple = ("Arial",25)
        Current_balance_guess1.configure(font=Balance_tuple)
        Current_balance_guess1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)

    else:
        Congratulations = Label(root,text=f"OOPS ! You Lost :- ${bet_guess}",background="black",foreground="orange")
        Congo_Tuple = ("Arial",40,"bold")
        Congratulations.configure(font=Congo_Tuple)
        Congratulations.grid(row=8,column=2,padx=10,pady=10,columnspan=35)
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\prefe\\Downloads\\sounds\\Lost.wav")
        pygame.mixer.music.play(loops=0)
        Current_balance_guess.destroy()
        balance = balance - bet_guess
        Current_balance_guess1 = Label(root,text=f"Your current balance is :- ${balance}",bg = "black",fg = "yellow")
        Balance_tuple = ("Arial",25)
        Current_balance_guess1.configure(font=Balance_tuple)
        Current_balance_guess1.grid(row=0,column=1,pady=5,rowspan=2,columnspan=5)
    
    Play_tuple = ("Arial",20,"bold")
    Play_again_btn = Button(root,text="Play Again",background="blue", foreground="light blue",font=Play_tuple,command=destroy_call_guess)
    Play_again_btn.grid(row=9,column=3,columnspan=10,padx=10)


def bet_try_guess():

    global e_choose,bet_guess,Choose,Start_Btn

    try:
        bet_guess = int(e.get())
    except ValueError:
        bet_guess = 100

    if(bet_guess<=balance):
        Choose = Label(root,text="Choose a number b/w [1-5] :-         ",bg="black",fg="green")
        Choose_Tuple = ("Arial",20,"bold")
        Choose.configure(font=Choose_Tuple)
        Choose.grid(row=6,column=1,pady=5,columnspan=10)

        e_choose = Entry(root,width=10,bg="light blue",fg="blue")
        e_choose.grid(row=6,column=6,pady=5,columnspan=5)

        Start_Tuple = ("Arial",10,"bold")

        Start_Btn = Button(root,text="Done",background="yellow",foreground="red",font= Start_Tuple,command=bet_choosed)
        Start_Btn.grid(column=12,row=6,columnspan=5)

def GUESS():
    global Current_balance_guess,e,Bet,Back_Btn,Try,Start_Btn1,balance
    rules_btn.destroy()
    guess_btn.destroy()
    seven_btn.destroy()
    Welcome.destroy()
    Current_balance_main.destroy()
    roulette_btn.destroy()

    Back_Btn = Button(root,text="Back",background="yellow",foreground="red",bd=5,height=1,width=4,command=destroy_call_main)
    Back_Tuple = ("Arial",15)
    Back_Btn.configure(font=Back_Tuple)
    Back_Btn.grid(row=0,column=0,padx=10,pady=10)

    Current_balance_guess = Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_guess.configure(font=Balance_tuple)
    Current_balance_guess.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=5)

    Try = Label(root,text="Let's Try Your Luck !!",bg="black",fg="yellow")
    Try_Tuple = ("Arial",50,"bold")
    Try.configure(font=Try_Tuple)
    Try.grid(row=3,column=1,padx=60,pady=5,columnspan=30,rowspan=2)

    Bet = Label(root,text="Place Your Bet :-- ",bg="black",fg="green")
    Bet_tuple = ("Arial",20,"bold")
    Bet.configure(font=Bet_tuple)
    Bet.grid(row=5,column=1,pady=5,columnspan=10)

    e = Entry(root,width=20,bg="light blue",fg="blue")
    e.grid(row=5,column=5,pady=5,columnspan=10)

    Start_Tuple = ("Arial",10,"bold")
    Start_Btn1 = Button(root,text="Place",background="yellow",foreground="red",font=Start_Tuple,bd=3,command=bet_try_guess)
    Start_Btn1.grid(column=12,row=5,columnspan=5)
    
def main():
    global rules_btn, guess_btn,seven_btn,roulette_btn,Current_balance_main,Welcome

    Current_balance_main = Label(root,text=f"Your current balance is :- ${balance}",bg="black",fg="yellow")
    Balance_tuple = ("Arial",25)
    Current_balance_main.configure(font=Balance_tuple)
    Current_balance_main.grid(row=0,column=0,padx=0,pady=10,rowspan=2,columnspan=8)

    Welcome = Label(root,text="The Casino Game",bg="black",fg="yellow")
    Welcome_tuple = ("Arial",60,"bold")
    Welcome.configure(font= Welcome_tuple)
    Welcome.grid(row=2,column=1,rowspan=2,columnspan=30,padx=150)

    #BUTTONS

    guess_btn = Button(root,text="Guess",background="light blue",height=1,width=5,bd=10,command=GUESS)
    guess_tuple = ("Arial",40,"bold")
    guess_btn.configure(font=guess_tuple)
    guess_btn.grid(row=4,column=6,columnspan=1,padx=150)


    seven_btn = Button(root,text="Seven",background="orange",foreground="dark red",bd=10,width=6 ,height=1,command=SEVEN)
    seven_btn.configure(font=guess_tuple)
    seven_btn.grid(row=4,column=8,columnspan=2)

    roulette_btn = Button(root,text="Roulette",background="orange",foreground="dark red",bd=10,width=7,command=ROULETTE)
    roulette_btn.configure(font=guess_tuple)
    roulette_btn.grid(row=5,column=6,padx=150,pady=10,columnspan=1)

    rules_btn = Button(root,text="Rules",background="light blue",width=5,bd=10)
    rules_btn.configure(font=guess_tuple)
    rules_btn.grid(row=5,column=8,padx=20,pady=10)



    




    

main()
root.mainloop()
