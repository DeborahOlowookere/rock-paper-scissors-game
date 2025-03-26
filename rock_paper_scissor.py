import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ("r", "p", "s")

while True:
    user_choice = input("rock, paper, scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    print(f'you chose {emojis[user_choice]}')
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
            (user_choice == "p" and computer_choice == "r")):
        print("You win!")
    else:
        print("You lose!")
    should_continue = input("Play again? (y/n): ").lower()
    if should_continue == "n":
        break
