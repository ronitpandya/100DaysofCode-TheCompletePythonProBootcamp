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

# I need to write a code to
import random
game_images = [rock, paper, scissors]
choices = [0, 1, 2]

user_choice = int(input("What would you like to choose? 0 for rock, 1 for paper or 2 for scissors. Type your choice"))
machine_choice = int(choices[random.randint(0,2)])
print(f"You chose {game_images[user_choice]}")
print(f"Machine chose {game_images[machine_choice]}")
if 0 < user_choice > 2:
    print("input invalid, please enter 0, 1 or 2 for rock, paper and scissors")
elif user_choice == machine_choice :
    print("You draw")
else :
    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.
    if user_choice == 0 and machine_choice == 2 :
        print("You Win")
    elif user_choice == 2 and machine_choice == 0 :
        print("You lose")
    elif user_choice < machine_choice :
        print("You lose")
    else :
        print("You win")