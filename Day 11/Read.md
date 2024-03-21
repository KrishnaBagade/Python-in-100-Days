Blackjack Game
This Python script simulates a simplified version of a Blackjack game. 
The game involves a user who can place bets, draw cards, and compete 
against a computer dealer. The rules follow a basic Blackjack setup 
with the option to draw cards ('hit') or pass ('stand'). The user's 
goal is to have a hand value closer to 21 than the dealer without 
exceeding it.

Game Rules
The deck is unlimited in size, with no jokers.
The Jack, Queen, and King all count as 10.
The Ace can count as either 11 or 1.
The user starts with two initial cards, and additional cards can be
drawn ('hit') or passed ('stand').
The dealer automatically draws cards until their hand value is at least 17.
If the user's hand value exceeds 21, they lose the round.
The winner is determined by the hand value closest to 21 without 
exceeding it.
How to Play
Run the program.
Place a bet from your available funds.
Receive two initial cards.
Choose to 'hit' and draw additional cards or 'stand' to pass.
The dealer draws cards until their hand value is at least 17.
The winner is determined based on the hand values.
Repeat the process to continue playing.
Code Explanation
The script uses a deck of cards represented as a list of integers 
and follows the basic Blackjack rules.

Users start with an initial fund of $1000 and can place bets on each round.

The program checks for user input errors and ensures proper handling
of the drawn cards, including the option to choose the value of an Ace.

The game checks for winners, losers, and draws, updating the user's 
fund accordingly.

The game loop continues until the user decides to stop playing.

How to Run
To run the program, execute the Python script:

bash
Copy code
python filename.py
Ensure that the necessary libraries (e.g., random) are available
or imported at the beginning of the script.

Notes
The game follows a simplified version of Blackjack, and additional
features or rule modifications can be implemented for a more complex 
gameplay experience.

User interaction is handled through the console, with options to 
'hit' or 'stand' during their turn.

The program keeps track of the user's winnings, and the game loop 
continues until the user decides to exit.