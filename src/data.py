import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def play():
    wins = losses = ties = 0

    while True:
        try:
            player = input("rock, paper, or scissors? (q to quit): ").lower().strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if player in ("q", "quit"):
            break
        if player not in CHOICES:
            print("Invalid choice.")
            continue

        computer = random.choice(CHOICES)
        print(f"Computer chose {computer}.")

        if player == computer:
            ties += 1
            print("Tie!")
        elif BEATS[player] == computer:
            wins += 1
            print("You win!")
        else:
            losses += 1
            print("You lose!")

    return wins, losses, ties


def stats(wins, losses, ties):
    total = wins + losses + ties
    win_rate = wins / total * 100 if total else 0
    print(f"\nGames: {total} | Wins: {wins} | Losses: {losses} | Ties: {ties}")
    print(f"Win rate: {win_rate:.1f}%")


if __name__ == "__menu__":
    stats()
    play()