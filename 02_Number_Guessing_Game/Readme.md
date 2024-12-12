# Number Guessing Game
This python program is a fun and interactive number guessing game (console-based) where the user guesses
a randomly generated number between 1-100. The program provides hints and tracks the previous guesses
made by the user.

## Features
- User can either choose the number of attempts themselves or can select the system defined number of attempts.
- User defined guess have been limited to 15 so the game remains fun.
- Guess the number between 1-100 with hints provide:
  - High: the guessed number is higher than the target.
  - Low: the guessed number is lowe than the target.
  - Correct: the guess matches the target.
- Tracks and displays the previous guesses in a list.
- Handles Exception:
  - Ensures the guesses and number of tries are integers.
- User can quit the game by typing 'Q' or 'q' after confirming to quit.
- Prompts the user to play another round after the game ends (attempts = 0 or guessed correctly).

## Installation
To run the program, simpy clone it and run `app.py` using python.

## Usage
- Run the script using python:
```bash
python app.py
```