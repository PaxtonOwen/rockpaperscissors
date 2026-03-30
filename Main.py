import random

import streamlit as st


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


st.title("Rock Paper Scissors")
mode = st.radio("Choose game mode", ["Regular", "Big Bang", "Impossible"], horizontal=True)

if mode == "Regular":
    hands = REGULAR_HANDS
    win_map = REGULAR_WINS
elif mode == "Big Bang":
    hands = BIG_BANG_HANDS
    win_map = BIG_BANG_WINS
else:
    hands = BIG_BANG_HANDS
    win_map = BIG_BANG_WINS

player_hand = st.selectbox("Pick your hand", hands)

if st.button("Play"):
    computer_hand = random.choice(hands)
    if mode == "Impossible":
        result = "You win" if random.randint(1, 10000) == 1 else "You lose"
    else:
        result = decide_winner(player_hand, computer_hand, win_map)

    st.write(f"You chose: {player_hand}")
    st.write(f"Computer chose: {computer_hand}")
    st.subheader(result)

if mode == "Impossible":
    st.caption("Impossible mode: you have a 1 in 10,000 chance to win each round.")
