import random
from art import logo

def check_guess(num_to_guess,user_guess,try_number):
  if num_to_guess > user_guess:
    print("Too low")
    return try_number - 1
  elif num_to_guess < user_guess:
    print("Too high")
    return try_number - 1
  elif num_to_guess == user_guess:
    print(f"You guessed it right. The number is {num_to_guess}.")
    return


def game(num_to_guess, try_number):
  if try_number == 0:
    print(f"You lose. the number was {num_to_guess}")
  else:
    user_guess = int(input("Make a guess: "))
    try_number = check_guess(num_to_guess, user_guess, try_number)
    if num_to_guess != user_guess:
      print(f"Number of remaining guesses {try_number}.")
    if num_to_guess == user_guess:
      print("Game is over. Would you like to go again?")
    else:
      game(num_to_guess, try_number)


try_number = 0
while True:
  print(logo)
  print("Welcome to the guess which number I am thinking game.")
  print("I am thinking of a number between 1 to 100")
  mode = input("Would you like to try hard mode or easy mode?\n").lower()
  num_to_guess = random.randint(1, 100)
  if mode == "hard":
    try_number += 5
    game(num_to_guess, try_number)
  elif mode == "easy":
    try_number += 10
    game(num_to_guess, try_number)
  else:
    print("Please enter either 'hard' or 'easy' mode")
  go_again = input("Enter any key to go again or 'n' to exit.\n").lower()
  if go_again == 'n':
    break
