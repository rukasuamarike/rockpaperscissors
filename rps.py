import sys
import random

ps = 0
cs = 0


def main():
    global cs, ps
    cs = 0
    ps = 0
    for i in range(5):
        choice = input('[round ' + str(i + 1) + '/5]choose rock, paper, or scissors:')
        if choice == 'rock' or choice == 'paper' or choice == 'scissors':
            cpu = cpu_choice()
            print('player chose ' + choice + ' and cpu chose ' + cpu + ',  ' + win_calc(str(choice), str(cpu)) + ' wins')
            print('scores:')
            print('player: ' + str(ps))
            print('cpu: ' + str(cs))
            print('\n')
            if i >= 4:
                print(finalwin() + ' won the game')
        else:
            print('invalid choice, cpu wins')
            cs += 1


def cpu_choice():
    result = "rock"
    rand = random.randint(0, 2)
    if rand == 1:
        result = "scissors"
    if rand == 2:
        result = "paper"
    return result


def win_calc(c1, c2):
    global ps, cs
    winner = "cpu"
    cs += 1
    if c1 == "rock" and c2 == "scissors":
        winner = playerwin()
    if c1 == "scissors" and c2 == "paper":
        winner = playerwin()
    if c1 == "paper" and c2 == "rock":
        winner = playerwin()
    if c1 == c2:
        winner = 'neither one'
        cs -= 1
    return winner


def playerwin():
    global ps, cs
    ps += 1
    cs -= 1
    return "player"


def finalwin():
    result = "cpu"
    if ps > cs:
        result = 'player'
    if ps == cs:
        result = 'both players'
    return result


if __name__ == '__main__':
    main()

