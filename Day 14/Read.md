Higher-Lower Game
This Python script implements a Higher-Lower game using data on social
media followers. The player is presented with two profiles (A and B) and
must guess which profile has more followers. The game continues until the
player makes an incorrect guess.

How to Play
Run the program.
Two profiles (A and B) are presented, each with a name, description, 
and country.
The player guesses which profile has more followers by typing 'A' or 'B'.
The program provides feedback and updates the score.
The game continues with new profiles until the player makes an incorrect
guess.
The final score is displayed.
Code Explanation
The script uses data on social media profiles stored in the game_data
module.

The compare function compares the follower counts of profiles A and B,
updating the score and restarting the game if the player's guess is correct.

The game function presents two profiles and prompts the player to guess
which one has more followers.

The game loop continues until the player makes an incorrect guess.

The script uses the randint function to randomly select profiles for 
comparison.

How to Run
To run the program, execute the Python script:

bash
Copy code
python filename.py
Ensure that the necessary modules (e.g., game_data, art, replit) are
available or imported at the beginning of the script.

Notes
The game offers a simple and engaging experience by leveraging social 
media follower data.

User input is handled through the console, with clear screen functionality
provided using the replit module.

The game loop continues until the player makes an incorrect guess, and 
the final score is displayed at the end.

Players can guess whether profile A or B has more followers based on 
the presented data.