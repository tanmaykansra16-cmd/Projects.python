from random import randint
from art import logo
Easy_level_turns =10
Hard_level_turns =5


def game():
    print(logo)
    def check_answer(guess, answer, turns):
        """checks answer against guess and return the number of turn remaining"""
        if guess > answer:
            print("YOU GUESS TOO HIGH ")
            return turns - 1

        elif guess < answer:
            print("YOU GUESS TOO LOW ")
            return turns - 1
        else:
            print(f"YOU GUESSED THE NUMBER 😍 {answer}")

    def set_difficulty():
        level = input("CHOOSE A DIFFICULTY: 'EASY' OR 'HARD'!").lower()
        if level == "easy":
            return Easy_level_turns
        else:
            return Hard_level_turns


    print("WELCOME TO THE NUMBER GUESSING GAME!!!")
    print("I AM THINKING OF A NUMBER BETWEEN 1 AND 100 🤔")

    answer = randint(1,100)
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"YOU HAVE {turns} ATTEMPTS TO GUESS THE NUMBER")
        guess = int(input("make a guess: "))

        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("YOU RAN OUT OF GUESSES , YOU LOSE😢")
            return
        elif guess != answer:
            print("GUESS AGAIN!!!")


game()


