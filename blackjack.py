
import random
from art import logo
def deal_card():
    """return random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards)
    return card

def calculate_score(cards):
    """take list of cards nd return the score calculated form cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw 🙃"
    elif c_score == 0:
        return "lose😢"
    elif u_score == 0:
        return "win🏅"
    elif u_score > 21:
        return " lose😢"
    elif c_score >21:
        return " win🏅 "
    elif u_score > c_score:
        return " win 🤗"
    else:
        return "lose🥺"



def play_game():
    print(logo)
    user_card = []
    computer_card= []
    computer_score = -1
    user_score = -1
    is_game_over= False
    for _ in range (2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your cards: { user_card } current score: {user_score}")
        print(f"computer's first  card: { computer_card [0]}")


        if user_score == 0 or computer_score == 0 or user_score> 21:
            is_game_over = True

        else:
            user_deal= input("type  'y' for another care and 'n' to pass: ").lower()

            if user_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"your final hand is {user_card},score is {user_score}")
    print(f"computer's final hand is{ computer_card}, score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play a game of blackjacks ? If so, type 'yes' or 'no\n").lower() == 'yes':
    print("\n"*20)
    play_game()




