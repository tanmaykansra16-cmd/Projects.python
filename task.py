rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
image =[rock,paper,scissors]
user = int(input("Enter your choice: type 0 for rock, 1 for paper, 2 for scissors: \n"))
if user >=0 and user<=2:
    print(image[user])
computer = random.randint(0,2)
print("computer chose:")
print(image[computer])
if user ==0 and computer == 2:
    print("you won")
elif user>=3 or user<=0:
    print("type again, you lost")
elif computer>user:
    print("you lost")
elif user == 2 and computer == 0:
    print("you lost")
elif user>computer:
    print("you won")
elif computer == user:
    print("draw")








