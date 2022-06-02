import random
import time
import pyinputplus as pyint

print("\nWelcome to scissor, rock and papper game".center(100).upper())
'''instructions about the game'''
inst= '\n\n\nINSTRUCTION\nIn the game you are expected to pick from the list below.\nIf your guest is currect you win else you loss \nYou can try again as the case maybe or quit. \nBut I believe since winners never quit you will made it.'
option = '\n\nTHE OPTIONS ARE\nR for Rock.\nP for Papper.\nS for Scissor'

print(inst)
def wrong():
    print('You just enter the wrong value for the game. try again')
    
start= int(input('Press 1 to start\n\n'))
while True:
    if start == 1:
        print(option)
        pick = str(input('Enter your pick below\n>>')).upper()            
        if pick == 'R':
            Choice_picked = 'Rock'
        elif pick == 'P':
            Choice_picked= 'Paper'
        elif pick == 'S':
            Choice_picked = 'Scissor'
        else:
            print(wrong())
            pick = str(input("Enter valid option\n:"))


        #for the user decission or his or her pick
        print('You just choose  ' + Choice_picked)
        time.sleep(3)
        print("\n\nIt's now the computer turn to make his own choice")
        compic = '\n1 for Rock.\n2 for Scissor.\n3 for Papper'
        time.sleep(2)
        #Here the computer need to make a random choice of all the options that are available in the game_plan
        print('the computer choice are:'.upper(), compic)
        valu = ['R', 'S', 'P']
        computer_pick = random.choice(valu)
        while computer_pick ==pick:
            computer_pick = random.choice(valu)
            if computer_pick == 'R':
                computer_choice = 'Rock'
            elif computer_pick == 'S':
                computer_choice = 'Scissors'
            else:
                computer_choice = 'Papper'
            
                time.sleep(4)
                print('Computer has choosen ' + computer_choice)
                print(f"you picked: {Choice_picked} \tV/s\t computer picked: {computer_choice}")

            #consition for winning
        if (Choice_picked == 'R' and computer_pick =='R') or (computer_pick =='R' and Choice_picked=='R'):
            print('Rock win =>', end='')
            result = 'Rock'
        elif (Choice_picked == 'S' and computer_pick =='S') or (computer_pick =='S' and Choice_picked=='S'):
            print('Scissor win =>', end='')
            result = 'Scissor'
        elif (Choice_picked == 'P' and computer_pick =='P') or (computer_pick =='P' and Choice_picked=='P'):
            print("Papper win =>", end="")
            result = 'Papper'
        if Choice_picked == computer_pick:
            print(Restart='')
        print('\nThe game has just come to and end.\nI know you are such a good player')
        print('\n\n')
        print('Do you still want to play')
        ans = pyint.inputYesNo(prompt='1 for Yes \n2 for No\n', yesVal=1, noVal=2)
        if ans == 2:
            break
