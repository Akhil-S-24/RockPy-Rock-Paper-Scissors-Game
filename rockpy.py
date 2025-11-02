import random
import time

# Title
print("🎮 Welcome to RockPy – Rock Paper Scissors Game 🎮")
print("--------------------------------------------------")

# Choices
choices = ["rock", "paper", "scissors"]

# Game loop
while True:
    print("\nYour options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_input = input("Enter your choice (1/2/3/4): ")

    if user_input == '4':
        print("👋 Thanks for playing RockPy! Goodbye!")
        break

    if user_input not in ['1', '2', '3']:
        print("❌ Invalid choice! Please select 1, 2, or 3.")
        continue

    user_choice = choices[int(user_input) - 1]
    computer_choice = random.choice(choices)

    print("\n🕹️ You chose:", user_choice.capitalize())
    time.sleep(0.5)
    print("💻 Computer chose:", computer_choice.capitalize())
    time.sleep(0.5)

    # Determine the winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🏆 You win!")
    else:
        print("💀 You lose!")

    time.sleep(1)

    # Play again option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing RockPy! See you next time.")
        break
