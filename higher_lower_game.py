import random
from art import logo, vs
from game_data import data

def formate_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_desc} from {account_country}:"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
should_continue = True
account_b = random.choice(data)


while should_continue:
    account_a = account_b
    account_b= random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare: {formate_data(account_a)}")
    print(vs)
    print(f"Compare: {formate_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    print("\n"*20)
    print(logo)


    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct= check_answer(guess, a_followers, b_followers)
    if is_correct:
        score += 1
        print(f"correct!. Your score is : {score}")

    else:
        [print(f"sorry thats wrong!!!. Final score : {score}")]
        should_continue = False


