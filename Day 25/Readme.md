# U.S. States Game

## Overview
The U.S. States Game is an interactive educational game designed to help players
learn and identify the states of the United States. Using the Turtle graphics library,
the game displays a blank map of the U.S., and players are prompted to guess the names
of the states. Correct guesses are displayed on the map, and players can exit the game 
at any time to save their progress.

## Game Components
- **Turtle Graphics**: Used for displaying the map and state names.
- **Pandas Library**: Utilized for reading and manipulating state data from a CSV file.
- **CSV Files**: 
  - `50_states.csv`: Contains the names and coordinates of all 50 U.S. states.
  - `States_to_Learn.csv`: Generated file listing states that the player has yet to guess.

## How to Play
1. **Start the Game**: Run the script to start the game. A blank map of the U.S. will be 
displayed.
2. **Guess States**: A prompt will ask you to guess the name of a state. Type your guess
and press enter.
3. **Correct Guesses**: If the guess is correct, the state's name will be displayed on the
map at the appropriate location.
4. **Exit the Game**: Type "Exit" to end the game. A CSV file named `States_to_Learn.csv`
will be generated, listing the states you have not yet guessed correctly.

## Instructions
1. **Prepare the Input Files**:
    - Ensure you have `50_states.csv` in the same directory as the script. This file 
   should contain the names and coordinates of all 50 states.
    - The `blank_states_img.gif` file should also be in the same directory.

2. **Run the Script**: Execute the script in your Python environment.

3. **Interact with the Game**:
    - Type in the name of a state when prompted.
    - The name will appear on the map if the guess is correct.
    - Type "Exit" to stop the game and generate the `States_to_Learn.csv` file.

## Notes
- Ensure the required files (`50_states.csv` and `blank_states_img.gif`) are in the correct
paths.
- The game continues until all 50 states are guessed or the player types "Exit".

## Dependencies
- Python 3.x
- Turtle module
- Pandas library
