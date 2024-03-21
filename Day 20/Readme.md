# Snake Game (Part 1)

## Introduction
This Python script is the initial part of a classic Snake game.
It is implemented using the Turtle graphics library.
The code sets up the game environment, initializes the Snake,
and begins the game loop to handle user input and snake movement.

## Functionality
- The script imports necessary modules: `Screen` from the Turtle library
and `sleep` from the time module.
- It also imports a custom module `Snake`, which presumably contains the logic
for the Snake object.
- The game window is created with specific dimensions and properties using 
the `Screen` class.
- The title of the game window is set to "Snake Game", and the background color
is set to black.
- The game loop (`while` loop) runs as long as the `game_is_on` variable is
`True`.
- Inside the loop, the screen is updated to show changes, and a short delay
(`sleep(0.1)`) is introduced to control the speed of the game.
- The Snake's movement is managed by calling the `move` method of the `Snake` 
object.
- Event listeners are set up to detect key presses for controlling the Snake's
direction (left, right, up, down).
- The game window stays open until the user clicks to exit 
(`screen.exitonclick()`).

## Next Steps
This code serves as the foundation for a fully functional Snake game.
In the subsequent parts of the code, additional features such as collision 
detection with food, growing the snake, scoring, and ending the game when
the snake collides with itself or the boundaries will be implemented.

## Usage
1. Ensure you have Python installed on your system.
2. Copy and paste the provided code into a Python file 
(e.g., `snake_game_part1.py`).
3. If necessary, create a file named `snake.py` containing the logic for
the Snake object.
4. Run the script using a Python interpreter.
5. Use the arrow keys to control the direction of the Snake.
6. Click on the game window to exit.

Enjoy the beginning of your Snake gaming experience!