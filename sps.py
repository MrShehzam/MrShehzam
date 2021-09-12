#stone paper scissor game
import random
import inquirer
lst= ["stone","paper", "scissors"]
num=int(input("how many time you want to play\n"))
cpu = 0
human = 0
while(1):
    b=random.choice(lst)
    num=num-1
    question=[
        inquirer.List('q',
                          message="select an option",
                          choices=['stone','paper','scissors'])
    ]
    answers = inquirer.prompt(question)

    if num==0 and human>cpu:
        print("\t\t\tCongratulations!\t\t\t\nYou won the game")
        print(f"you won by {human-cpu} points")
        question = [
            inquirer.List('ad',
                          message="Do You Want To Play Again?",
                          choices=['YES', 'NO'])
        ]
        ans = inquirer.prompt(question)
        if ans=={'ad': 'YES'}:
            num=int(input("How many times do you want to play?\n" ))
            continue
        else:
            break
    elif num==0 and human<cpu:
        print("\tBetter Luck Next Time!\nYou Lose The Game!")
        print(f"you lose by {cpu-human} points")
        question = [
            inquirer.List('ad',
                          message="Do You Want To Play Again?",
                          choices=['YES', 'NO'])
        ]
        ans = inquirer.prompt(question)
        if ans=={'ad': 'YES'}:
            num=int(input("How any times do you want to play?\n"))
            continue
        else:
            break

    elif num==0 and human==cpu:
        print("\t\t\tDRAW!\nBetter Luck Next Time")
        print(f"you both have {human} points")
        question = [
            inquirer.List('ad',
                          message="Do You Want To Play Again?",
                          choices=['YES', 'NO'])
        ]
        ans = inquirer.prompt(question)
        if ans=={'ad': 'YES'}:
            num=int(input("How many times do you want to play?\n"))
            continue
        else:
            break

    elif b=="stone" and answers=={'q': 'stone'}:
        print("\t \t \t \t DRAW \nYou have choosen stone and cpu have choosen stone")
        print(f"you have {num} tries left")
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="paper" and answers=={'q': 'paper'}:
        print("\t \t \t \t DRAW \nYou have choosen paper and cpu have choosen paper")
        print(f"you have {num} tries left")
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="scissors" and answers=={'q': 'scissors'}:
        print("\t \t \t \t DRAW \nYou have choosen scissors and cpu have choosen scissors")
        print(f"you have {num} tries left")
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="stone" and answers=={'q': 'paper'}:
        print("\t \t \t \t You Win \nYou have choosen paper and cpu have choosen stone")
        print(f"you have {num} tries left")
        human=human+1
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="stone" and answers=={'q': 'scissors'}:
        print("\t \t \t \t YOU LOSE \nYou have choosen scissors and cpu have choosen stone")
        print(f"you have {num} tries left")
        cpu = cpu + 1
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="paper" and answers=={'q': 'stone'}:
        print("\t \t \t \t You Lose \nYou have choosen stone and cpu have choosen paper")
        print(f"you have {num} tries left")
        cpu = cpu + 1
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="paper" and answers=={'q': 'scissors'}:
        print("\t \t \t \t You Win \nYou have choosen scissors and cpu have choosen paper")
        print(f"you have {num} tries left")
        human = human + 1
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="scissors" and answers=={'q': 'stone'}:
        print("\t \t \t \t You Win \nYou have choosen stone and cpu have choosen scissors")
        print(f"you have {num} tries left")
        human = human + 1
        print(f"you have {human} points and cpu have {cpu} points")
        continue
    elif b=="scissors" and answers=={'q': 'paper'}:
        print("\t \t \t \t You Lose \nYou have choosen paper and cpu have choosen scissors")
        print(f"you have {num} tries left")
        human = human + 1
        print(f"you have {human} points and cpu have {cpu} points")
        continue

