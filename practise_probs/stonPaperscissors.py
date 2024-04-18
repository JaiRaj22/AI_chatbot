import random

while True:
    print("enter rock or paper or scissor")
    words = ["rock","paper",'scissor']
    text = input()
    if text == "rock" or text == "paper" or text == "scissor":
        random_choice = random.choice(words)
        if text == random_choice:
            print(random_choice)
            print("try again")
            continue
        
        elif text == "rock" and random_choice == "paper":
            print(random_choice)
            print("you lost")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
        elif text == "rock" and random_choice == "scissor":
            print(random_choice)
            print("you won")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
        elif text == "paper" and random_choice == "rock":
            print(random_choice)
            print("you won")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
        elif text == "paper" and random_choice == "scissor":
            print(random_choice)
            print("you lost")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
        elif text == "scissor" and random_choice == "rock":
            print(random_choice)
            print("you lost")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
        elif text == "scissor" and random_choice == "paper":
            print(random_choice)
            print("you won")
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('game over.')
            break
        
    else:
        print("wrong input")
        break
        