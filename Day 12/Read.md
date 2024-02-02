Number Guessing Game
This Python script implements a simple number guessing game where the player tries to guess a randomly generated number between 1 and 100. The game offers two modes: "hard" and "easy," each with a different number of allowed guesses.

How to Play
Run the program.
Choose between "hard" and "easy" modes.
Make a guess, and the program will provide feedback if the guess is too high or too low.
Keep guessing until you correctly identify the hidden number or run out of guesses.
The game will inform you whether you've won or lost.
Optionally, you can choose to play again or exit the game.
Code Explanation
The script uses the random module to generate a random number between 1 and 100 for the player to guess.

The game has two modes:

Hard Mode: Allows 5 guesses.
Easy Mode: Allows 10 guesses.
The check_guess function compares the user's guess with the randomly generated number, providing feedback and returning the remaining number of guesses.

The game function handles the main game loop, allowing the player to make guesses until they either correctly guess the number or run out of attempts.

The game loop continues until the player decides to exit.

How to Run
To run the program, execute the Python script:

bash
Copy code
python filename.py
Ensure that the necessary modules (e.g., random, art, replit) are available or imported at the beginning of the script.

Notes
The game provides a simple and enjoyable experience for guessing a randomly generated number.

User input is handled through the console, and clear screen functionality is provided using the replit module.

Players can choose between "hard" and "easy" modes, with different difficulty levels.

The game loop allows for multiple rounds, with the option to play again or exit after each round.




