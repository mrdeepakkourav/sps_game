import streamlit as st
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="✊",
    layout="centered"
)

# ---------- GAME LOGIC ----------
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw 🤝"

    if (
        (user_choice == "Stone" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Stone") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You Win 🎉"
    else:
        return "Computer Wins 💻"


# ---------- UI ----------
st.title("✊ Stone Paper Scissors ✋✌")
st.write("Play against the computer!")

# Initialize session state
if "score_user" not in st.session_state:
    st.session_state.score_user = 0
if "score_computer" not in st.session_state:
    st.session_state.score_computer = 0

# User choice
user_choice = st.radio(
    "Choose your move:",
    ("Stone", "Paper", "Scissors"),
    horizontal=True
)

# Play button
if st.button("Play"):
    computer_choice = random.choice(["Stone", "Paper", "Scissors"])
    result = get_winner(user_choice, computer_choice)

    st.subheader("Result")
    st.write(f"**You chose:** {user_choice}")
    st.write(f"**Computer chose:** {computer_choice}")
    st.write(f"### {result}")

    # Update score
    if result == "You Win 🎉":
        st.session_state.score_user += 1
    elif result == "Computer Wins 💻":
        st.session_state.score_computer += 1

# ---------- SCOREBOARD ----------
st.divider()
st.subheader("🏆 Scoreboard")
st.write(f"**You:** {st.session_state.score_user}")
st.write(f"**Computer:** {st.session_state.score_computer}")

# Reset button
if st.button("Reset Game"):
    st.session_state.score_user = 0
    st.session_state.score_computer = 0
    st.success("Game reset successfully 🔄")
