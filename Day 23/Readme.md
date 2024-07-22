# Turtle Crossing Game

## Overview
This Turtle Crossing Game is a simple yet engaging game created using Python's Turtle module. The objective of the game is to help the player (a turtle) cross a busy road filled with moving cars without getting hit. As the player progresses through levels, the game difficulty increases.

## Game Components
- **Player**: The turtle that the player controls.
- **Cars**: Obstacles that the player must avoid while crossing the road.
- **Scoreboard**: Keeps track of the current level and the high score.

## How to Play
1. **Start the Game**: Run the script to start the game.
2. **Move the Player**: Use the "Up" arrow key to move the turtle upwards.
3. **Avoid Cars**: Avoid getting hit by the cars moving horizontally across the screen.
4. **Level Up**: Reach the top of the screen to advance to the next level.
5. **Game Over**: If the turtle collides with a car, the game is over. The game will save the high score to a file named `highscore.txt`.

## Increasing Difficulty
- The speed of the cars increases as the player levels up.
- The frequency of car spawns also adjusts with each level, making it more challenging to navigate through the cars.

## Files and Modules
- **main.py**: The main game script containing the game loop and logic.
- **Player.py**: Contains the `Player` class, which manages the turtle's movements and resets.
- **car_manager.py**: Contains the `CarManager` class, which handles car creation, movement, and collision detection.
- **scoreboard.py**: Contains the `Scoreboard` class, which manages the level display and high score.

## Setup and Execution
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Ensure Dependencies**: Make sure you have Python installed along with the Turtle module.
3. **Run the Game**: Execute the `main.py` script to start the game.

