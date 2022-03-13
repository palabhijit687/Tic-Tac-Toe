### TIC TAC TOE GAME IN PYTHON ###
### CREATED BY - ABHIJIT PAL ###
### DATED: 06-09-2021 ###

#importing the random library
import random

#Starting the game and giving options to choose
def game_start():
    print("Enter your choice: \n")      #taking the player input
    print("1: Play Manual Mode\n")
    print("2: Play Auto Mode\n")
    print("3: Exit\n")
    n=int(input())
    if n==1:
        print("Playing Manual Mode...")
        print("*********************************************")

        #calling the manual() function to play in manual mode
        manual()        
    
    elif n==2:
        print("Playing Auto Mode...")
        print("*********************************************")
        #Calling the auto() function to play in manual mode
        auto()          
    
    elif n==3:
        print("exiting...")
        print("*********************************************")
        #exit()
        raise SystemExit("Game Ended...") #exit() was working fine in vs code but it was causing problem in notebook
    else:
        print("Invalid Choice")

def check(table):
    #checking the moves of player one to find the result

    #checking row wise
    #checking the first row
    if table['1'] == 'X' and table['2'] == 'X' and table['3'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the second row
    if table['4'] == 'X' and table['5'] == 'X' and table['6'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the third row
    if table['7'] == 'X' and table['8'] == 'X' and table['9'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #Checking columnwise
    #checking the first Column
    if table['1'] == 'X' and table['4'] == 'X' and table['7'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #Checking the second column
    if table['2'] == 'X' and table['5'] == 'X' and table['8'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the third column
    if table['3'] == 'X' and table['6'] == 'X' and table['9'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1

    #checking diagonals
    #checking left diagonal
    if table['1'] == 'X' and table['5'] == 'X' and table['9'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1
    #checking right diagonal
    if table['3'] == 'X' and table['5'] == 'X' and table['7'] == 'X':
        print('Player one won!')
        print("*********************************************")
        game_start()
        return 1


    #checking the moves of player two
    #checking horizontal conditions
    #checking the first row
    if table['1'] == 'O' and table['2'] == 'O' and table['3'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the second row
    if table['4'] == 'O' and table['5'] == 'O' and table['6'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the third row
    if table['7'] == 'O' and table['8'] == 'O' and table['9'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #Checking verticals
    #checking the first column
    if table['1'] == 'O' and table['4'] == 'O' and table['7'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the second column
    if table['2'] == 'O' and table['5'] == 'O' and table['8'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking the third column
    if table['3'] == 'O' and table['6'] == 'O' and table['9'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking diagonals
    #Checking the left diagonal
    if table['1'] == 'O' and table['5'] == 'O' and table['9'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1

    #checking for the right diagonal
    if table['3'] == 'O' and table['5'] == 'O' and table['7'] == 'O':
        print('Player two won!')
        print("*********************************************")
        game_start()
        return 1
    
    #checking for the tie condition
    return 0

#defining auto function to play automatically
def auto():
    #initializing the table
    table = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }

    #creating a list of choices for the computer to choose
    choice_list = ['1','2','3','4','5','6','7','8','9']

    #initializing players and moves
    player = 1
    total_moves = 0

    print('1|2|3')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('7|8|9')
    print('-+-+-')
    print("*********************************************")

    while total_moves<9: #printing the table
        print(table['1']+'|'+table['2']+'|'+table['3'])
        print('-+-+-')
        print(table['4']+'|'+table['5']+'|'+table['6'])
        print('-+-+-')
        print(table['7']+'|'+table['8']+'|'+table['9'])
        end_check = check(table)

        #checking for tie condition
        if total_moves==9 and end_check!=1:
            print("game ended with a tie")
            print("*********************************************")
            game_start()
        
        elif total_moves==9 or end_check == 1:
            break

        while total_moves<9 and end_check!=1 and total_moves!=9:
            if player == 1:
                p1 = input('Player One:\n') #taking the input of player 1
                if p1 in table and table[p1] == ' ':
                    #print(choice_list)
                    if p1 in choice_list:
                        choice_list.remove(p1) #removing the choice so that computer cannot choose it again
                    table[p1] = 'X'
                    player = 2
                    total_moves += 1 #incrementing the total_moves count
                    break

                #if player 1 gives a wrong input
                else:
                    print('Invalid input, Please try again')
                    continue
            
            else:
                p2 = random.choice(choice_list)
                print('Player 2: ')
                print(int(p2))
                #print(choice_list)
                if p2 in table and table[p2] == ' ':
                    if p2 in choice_list:
                        choice_list.remove(p2) #removing the choice so that computer cannot choose it again
                    table[p2] = 'O'
                    player = 1
                    total_moves += 1 #incrementing the total_moves count
                    break
        print("*********************************************")

#defining function to play manually
def manual():
    #initializing the table
    table = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }

    #initializing players and moves
    player = 1
    total_moves = 0

    print('1|2|3')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('7|8|9')
    print('-+-+-')
    print("*********************************************")

    while total_moves<10: #printing the table
        print(table['1']+'|'+table['2']+'|'+table['3'])
        print('-+-+-')
        print(table['4']+'|'+table['5']+'|'+table['6'])
        print('-+-+-')
        print(table['7']+'|'+table['8']+'|'+table['9'])
        end_check = check(table)
        #if total_moves == 9 or end_check == 1:  #checking if there are moves left and game is not ended
            #break

        if total_moves==9 and end_check!=1:
            print("game ended with a tie")
            print("*********************************************")
            game_start()
        
        elif total_moves==9 or end_check == 1:
            break

        while total_moves<10 and end_check!=1:
            if player == 1:
                p1 = input('Player One:\n') #taking the input of player 1
                if p1 in table and table[p1] == ' ':
                    table[p1] = 'X'
                    player = 2
                    total_moves += 1 #incrementing the total_moves count
                    break

                #if player 1 gives a wrong input
                else:
                    print('Invalid input, Please try again')
                    continue
            
            else:
                p2 = input('Player Two:\n') #taking the input of player 2
                if p2 in table and table[p2] == ' ':
                    table[p2] = 'O'
                    player = 1
                    total_moves += 1 #incrementing the total_moves count
                    break

                #if player 2 gives wrong input
                else:
                    print('Invalid input, Please try again')
                    continue

        
        print("*********************************************")
        



#driver code to start
if __name__ == "__main__":
    game_start()
