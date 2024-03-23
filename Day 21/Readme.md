# Snake Game (Part 2)

## Introduction
This Python script is a continuation of the Snake game implementation,
building upon the initial setup provided in Part 1. In this part, additional
functionalities such as food generation, scoring, and collision detection 
are introduced to enhance the gameplay experience.

## Functionality
- The script imports modules for `Screen`, `sleep` from the `time` module,
`Snake` from a custom module named `snake`, `Food` from a custom module 
named `Food`, and `ScoreBoard` from a custom module named `Score_Board`.
- A list `snake_body` is initialized to track the segments of the 
snake's body.
- The game window is created with specific dimensions and properties.
- The Snake, Food, and ScoreBoard objects are instantiated.
- The game loop continues to run as long as `game_is_on` is `True`.
- Inside the loop:
  - The screen is updated, and a short delay is introduced for controlling
  the game speed.
  - The Snake moves according to the user's input.
  - Event listeners are set up to detect key presses for controlling the 
  Snake's direction.
  - If the Snake's head collides with the food:
    - New food is generated at a random location.
    - The scoreboard is updated to reflect the score.
    - The Snake grows longer.
  - If the Snake's head goes out of the play area:
    - The game ends, and the "Game Over" message is displayed on the
    scoreboard.
  - If the Snake's head collides with its body:
    - The game ends, and the "Game Over" message is displayed on the 
    scoreboard.

## Next Steps
With the completion of Part 2, the Snake game now includes essential
features such as food generation, scoring, and collision detection.

## Usage
1. Ensure you have Python installed on your system.
2. Copy and paste the provided code into a Python file (e.g., 
`snake_game_part2.py`).
3. Make sure you have the necessary custom modules (`snake.py`,
`Food.py`, `Score_Board.py`) containing the logic for Snake, Food,
and ScoreBoard classes, respectively.
4. Run the script using a Python interpreter.
5. Use the arrow keys to control the direction of the Snake.
6. Avoid collisions with the borders of the play area and the Snake's own body.
7. Collect food to increase your score.
8. Click on the game window to exit.

Enjoy the extended gameplay experience of the Snake game!