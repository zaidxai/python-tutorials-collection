import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Dictionaries for choices
yourDict = {"r": -1, "p": 0, "s": 1}
reverseDict = {-1: "Rock", 0: "Paper", 1: "Scissors"}

# Score tracking
wins = 0
losses = 0
draws = 0

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Game loop
while True:
    # Speak and ask for input
    speak("\nR for Rock, P for Paper, S for Scissors. Enter your choice:")
    yourchoice = input("Enter your choice: ").lower()

    if yourchoice not in yourDict:
        speak("Invalid input! Please enter R, P, or S.")
        continue

    computer = random.choice([-1, 0, 1])
    you = yourDict[yourchoice]

    # Speak the choices
    speak(f"You chose {reverseDict[you]}")
    speak(f"Computer chose {reverseDict[computer]}")

    # Determine result
    if computer == you:
        speak("It's a draw!")
        draws += 1
    elif (you == -1 and computer == 1) or (you == 1 and computer == 0) or (you == 0 and computer == -1):
        speak("You win!")
        wins += 1
    else:
        speak("You lose!")
        losses += 1

    # Show and speak score
    score_text = f"Scoreboard: Wins: {wins}, Losses: {losses}, Draws: {draws}"
    speak(score_text)

    # Ask to play again
    speak("Do you want to play again? Press Y for Yes, or any other key to quit.")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        final_score = f"Final Score Summary: Wins: {wins}, Losses: {losses}, Draws: {draws}"
        speak(final_score)
        speak("Thanks for playing! Goodbye!")
        break
