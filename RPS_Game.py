import random

def single_player():
    print("\n--- Single Player Mode ---")
    print("Choices: R = Rock, P = Paper, S = Scissors")

    user = input("Your choice (R/P/S): ").upper()
    computer = random.choice(["R", "P", "S"])
    print(f"Computer chose: {computer}")

    check_winner(user, computer, "You", "Computer")

def two_player():
    print("\n--- Two Player Mode ---")
    print("Choices: R = Rock, P = Paper, S = Scissors")

    p1 = input("Player 1, enter your choice (R/P/S): ").upper()
    p2 = input("Player 2, enter your choice (R/P/S): ").upper()

    check_winner(p1, p2, "Player 1", "Player 2")

def check_winner(choice1, choice2, name1, name2):
    rules = {"R": "S", "P": "R", "S": "P"}

    if choice1 == choice2:
        print("It's a Draw! 🤝")
    elif rules[choice1] == choice2:
        print(f"{name1} Wins! 🏆")
    else:
        print(f"{name2} Wins! 🏆")

def main():
    print("Welcome to Rock, Paper, Scissors 🎮")
    print("1. Single Player (You vs Computer)")
    print("2. Two Player (Player1 vs Player2)")

    mode = input("Choose mode (1/2): ")

    if mode == "1":
        single_player()
    elif mode == "2":
        two_player()
    else:
        print("Invalid choice. Please restart.")

if __name__ == "__main__":
    main()
