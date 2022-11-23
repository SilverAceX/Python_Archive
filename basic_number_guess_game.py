import random

def divisible(i):
    return ((i%3 == 0) and (i%5 == 0))


def input_random():
    user_min = int(input("Enter minimum value: "))
    user_max = int(input("Enter maximum value: "))
    number = random.randint(user_min, user_max)
    return number


def win_results(wins, rounds):
    print(f"Wins: {wins} Rounds: {rounds} Win Ratio: {(wins/rounds):.2f}")
    reset = input("Would you like to reset stats? (y/n): ")
    return reset

rounds = 0
wins = 0
play_again = True


while play_again:
    number = input_random()
    guess = ''

    while guess != number:
        guess = int(input("Guess the number: "))
        rounds+=1
        if guess == number:
            wins+=1

    print(f"The number was: {number}")

    result = win_results(wins,rounds)
    if result.lower() == 'y':
        rounds = 0
        wins =  0

    again = input("Would you like to play again? (y/n): ")
    if again.lower() == 'n':
        play_again = False

