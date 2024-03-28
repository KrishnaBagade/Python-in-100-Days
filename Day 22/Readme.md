# Pong-Pong Game

## Introduction
This Python script implements a simple version of the classic Pong game using the Turtle graphics library. The game involves two paddles and a ball, with players using the paddles to hit the ball back and forth. The objective is to score points by successfully hitting the ball past the opponent's paddle.

## Functionality
- The script imports necessary modules: `Screen` from the Turtle library, `sleep` from the `time` module, `paddle` from a custom module `paddle_command`, `Ball` from a custom module `ball_class`, and `ScoreBoard` from a custom module `Score_Board`.
- The game window is created with specific dimensions and properties.
- Two paddles (`r_paddle` and `l_paddle`) are initialized at specific positions.
- The game loop runs continuously until the `game_is_on` variable is `True`.
- Inside the loop:
  - The screen is updated to show changes, with a delay controlled by `game_speed`.
  - The ball moves according to its current heading.
  - The ball's collision with the walls is detected and handled.
  - The ball's collision with the paddles is partially implemented but commented out.
  - If the ball collides with the right paddle (`r_paddle`), its direction is adjusted to simulate a bounce.
  - If the ball collides with the left paddle (`l_paddle`), its direction is adjusted similarly.
  - If the ball goes beyond the right boundary, the left player scores a point, and the ball is reset to the center, heading towards the left player.
  - If the ball goes beyond the left boundary, the right player scores a point, and the ball is reset to the center, heading towards the right player.
  - Event listeners are set up to detect key presses for controlling the paddles' movements.
- The game window exits when clicked.

## Usage
1. Ensure you have Python installed on your system.
2. Copy and paste the provided code into a Python file (e.g., `pong_game.py`).
3. Make sure you have the necessary custom modules (`paddle_command.py`, `ball_class.py`, `Score_Board.py`) containing the logic for the paddles, ball, and scoreboard, respectively.
4. Run the script using a Python interpreter.
5. Use the arrow keys and "w" / "s" keys to control the paddles' movements.
6.Click on the game window to exit.

Have fun playing Pong!