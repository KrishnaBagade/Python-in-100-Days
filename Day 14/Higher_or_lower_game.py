from random import randint

from art import logo, vs
from game_data import data


def compare(user_choice,data,a,b,score):
  fcv = data[a]['follower_count']
  fcb = data[b]['follower_count']
  if (fcv > fcb and user_choice == "a") or (fcv < fcb and user_choice == "b"):
    score += 1
    print(f"You guessed it right. Current score: {score}")
    a = b
    b = randint(0,49)
    while a == b:
     b = randint(0,49)
    game(score,a,b)
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    should_continue = False
    return should_continue

def game(score, a, b):
  print(logo)
  print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
  print(vs)
  print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
  while True:
    user_choice = input("Who has more followers? Type 'A' or 'B', E:Exit ").lower()
    if user_choice != "a" and user_choice != "b":
      print("Please enter either a or b only.")
    elif user_choice == 'e':
      break
    else:
      should = compare(user_choice,data,a,b,score)
      if should == False:
        break

with open("high_score.txt",mode="r") as file:
  highest_score = file.read()
highscore = int(highest_score)
score = 0
a = 0
b = 0
while a == b:
  a = randint(0,49)
  b = randint(0,49)
game(score,a,b)
if highscore < score:
  with open("high_score.txt", mode="w") as file:
    file.write(f"{score}")