rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
computer_options=["Rock","Paper","Scissors"]
win_count=0
loss_count=0
draw_count=0
result_w=["0Scissors","2Paper","1Rock"]
result_l=["0Paper","1Scissors","2Rock"]
result_d=["0Rock","1Paper","2Scissors"]
while True:
  user_choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  computer_choice = random.randint(0,2)
  computer_chose = computer_options[computer_choice]
  result=user_choice+computer_chose
  user_chose=computer_options[int(user_choice)]
  if user_chose=="Rock":
    print(rock
         )
  elif user_chose=="Paper":
    print(paper)
  elif user_chose=="Scissors":
    print(scissors)
  if computer_chose=="Rock":
      print(rock)
  elif computer_chose=="Paper":
      print(paper)
  elif computer_chose=="Scissors":
      print(scissors)
  if result in result_w:
    print(f"You choose {user_chose} and Computer chose {computer_chose}. Congrats, you win!")
    win_count+=1
  elif result in result_l:
    print(f"You choose {user_chose} and Computer chose {computer_chose}. Sorry, you lose!")
    loss_count+=1
  elif result in result_d:
    print(f"You choose {user_chose} and Computer chose {computer_chose}. It's a draw!")
    draw_count+=1
  option_p=input("Do you want to play again? Type 'y' for yes or 'n' for no.\n")
  if option_p=="n":
    break
  elif option_p=="y":
    continue
play_count=win_count+loss_count+draw_count
print(f"Thank you for playing Rock-Paper-Scissors.\nYou played {play_count} games.\nYou won {win_count} games, lost {loss_count} games and had {draw_count} draws.")
if win_count>loss_count and win_count>draw_count:
  print("You are having an awesome day!")
elif win_count>loss_count:
  print("You are having an awesome day!")
elif win_count>draw_count:
  print("You are having an awesome day!")
elif loss_count>win_count and loss_count>draw_count:
  print("You are having a bad day")
elif loss_count>draw_count:
  print("You are having a bad day")
elif loss_count>win_count:
  print("You are having a bad day")
elif draw_count>win_count and draw_count>loss_count:
  print("You are having an alright day")
elif draw_count>win_count:
  print("You are having an alright day")
elif draw_count>loss_count:
  print("You are having an alright day")
elif win_count==loss_count and win_count==draw_count:
  print("You are having an average day")
  
  
  