import random


def play():
    user = input(
        "What's you choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return "you won!"

    return 'You lost!'


def is_win(player, opponent):
    # retunr true if player wins

    if(player == 'r' and opponent == 'r') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
