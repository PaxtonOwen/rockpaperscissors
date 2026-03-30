import random

# ---------- Core helpers ----------

def get_choice(prompt, valid_choices):
    valid_lower = [c.lower() for c in valid_choices]
    while True:
        user = input(prompt).strip().lower()
        if user in valid_lower:
            return user
        print(f"Invalid choice. Choose one of: {', '.join(valid_choices)}")

def play_again():
    return get_choice("Play again? (y/n): ", ["y", "n"]) == "y"

def outcome_rps(player, ai):
    """Returns: 'win', 'lose', or 'tie'."""
    if player == ai:
        return "tie"
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "win" if beats[player] == ai else "lose"

def outcome_rpsls(player, ai):
    """Rock Paper Scissors Lizard Spock. Returns: 'win', 'lose', or 'tie'."""
    if player == ai:
        return "tie"
    beats = {
        "scissors": {"paper", "lizard"},
        "paper": {"rock", "spock"},
        "rock": {"lizard", "scissors"},
        "lizard": {"spock", "paper"},
        "spock": {"scissors", "rock"},
    }
    return "win" if ai in beats[player] else "lose"

def print_result(result):
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("Tie!")

# ---------- Game modes ----------

def mode_regular():
    choices = ["rock", "paper", "scissors"]
    print("\n--- Regular Mode (Rock / Paper / Scissors) ---")
    while True:
        player = get_choice("Choose rock, paper, or scissors: ", choices)
        ai = random.choice(choices)
        print(f"AI chose: {ai}")
        result = outcome_rps(player, ai)
        print_result(result)

        if not play_again():
            break

def mode_big_bang():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    print("\n--- Big Bang Mode (Rock / Paper / Scissors / Lizard / Spock) ---")
    print("Rules summary:")
    print("- Scissors cuts Paper, decapitates Lizard")
    print("- Paper covers Rock, disproves Spock")
    print("- Rock crushes Lizard, crushes Scissors")
    print("- Lizard poisons Spock, eats Paper")
    print("- Spock smashes Scissors, vaporizes Rock")

    while True:
        player = get_choice("Choose rock, paper, scissors, lizard, or spock: ", choices)
        ai = random.choice(choices)
        print(f"AI chose: {ai}")
        result = outcome_rpsls(player, ai)
        print_result(result)

        if not play_again():
            break

def mode_impossible():
    """RPS where the player wins with exactly 1/10000 probability per round."""
    choices = ["rock", "paper", "scissors"]
    beaten_by = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock",
    }
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    print("\n--- Impossible Mode (1/10000 chance to win) ---")
    print("The AI is unfair. You will almost never win.")

    while True:
        player = get_choice("Choose rock, paper, or scissors: ", choices)

        jackpot = (random.randint(1, 10000) == 1)  # exactly 1/10000 chance
        if jackpot:
            ai = beats[player]  # AI picks what the player beats — player wins
            print("Something feels different this round...")
        else:
            # AI beats the player most of the time; occasionally ties to seem natural
            if random.random() < 0.85:
                ai = beaten_by[player]  # AI wins
            else:
                ai = player             # tie

        print(f"AI chose: {ai}")
        result = outcome_rps(player, ai)
        print_result(result)

        if not play_again():
            break

# ---------- Menu ----------

def main():
    print("Rock Paper Scissors - Python")
    while True:
        print("\nChoose a mode:")
        print("1) Regular")
        print("2) Big Bang (RPSLS)")
        print("3) Impossible (1/10000 chance)")
        print("4) Quit")

        choice = get_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"])

        if choice == "1":
            mode_regular()
        elif choice == "2":
            mode_big_bang()
        elif choice == "3":
            mode_impossible()
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
