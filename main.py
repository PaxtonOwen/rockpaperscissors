import random

REGULAR_HANDS = ["Rock", "Paper", "Scissors"]
BIG_BANG_HANDS = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

REGULAR_WINS = {
    "Rock": {"Scissors"},
    "Paper": {"Rock"},
    "Scissors": {"Paper"},
}

BIG_BANG_WINS = {
    "Scissors": {"Paper", "Lizard"},
    "Paper": {"Rock", "Spock"},
    "Rock": {"Lizard", "Scissors"},
    "Lizard": {"Spock", "Paper"},
    "Spock": {"Scissors", "Rock"},
}


def decide_winner(player: str, computer: str, win_map: dict[str, set[str]]) -> str:
    if player == computer:
        return "Tie"
    if computer in win_map[player]:
        return "You win"
    return "You lose"


def choose_mode() -> int:
    while True:
        print("Choose mode:")
        print("1) Regular")
        print("2) Big Bang")
        print("3) Impossible")
        try:
            choice = int(input("Enter mode number: "))
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        if choice in {1, 2, 3}:
            return choice

        print("Invalid input. Please enter 1, 2, or 3.")


def choose_hand(hands: list[str]) -> str:
    while True:
        print("Pick your hand:")
        for i, hand in enumerate(hands, start=1):
            print(f"{i}) {hand}")

        try:
            choice = int(input("Enter hand number: "))
        except ValueError:
            print(f"Invalid input. Please enter a number from 1 to {len(hands)}.")
            continue

        if 1 <= choice <= len(hands):
            return hands[choice - 1]

        print(f"Invalid input. Please enter a number from 1 to {len(hands)}.")


def play_round() -> None:
    mode = choose_mode()

    if mode == 1:
        hands = REGULAR_HANDS
        win_map = REGULAR_WINS
    elif mode == 2:
        hands = BIG_BANG_HANDS
        win_map = BIG_BANG_WINS
    elif mode == 3:
        hands = BIG_BANG_HANDS
        win_map = BIG_BANG_WINS
        print("Impossible mode: 1 in 10,000 chance to win")
    else:
        print("Invalid input")
        raise SystemExit

    player_hand = choose_hand(hands)
    computer_hand = random.choice(hands)

    if mode == 3:
        result = "You win" if random.randint(1, 10000) == 1 else "You lose"
    else:
        result = decide_winner(player_hand, computer_hand, win_map)

    print(f"You chose: {player_hand}")
    print(f"Computer chose: {computer_hand}")
    print(result)


def play_again() -> bool:
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Invalid input. Please enter y or n.")


while True:
    play_round()
    if not play_again():
        print("Thanks for playing!")
        break
