import random
from replit import clear
from Word_list import word_list
from Hangman_ascii_art import logo,stages

def letter_in_word(letter,word):
  return letter in word

lives=6
print(logo)
v=random.randint(0,len(word_list))
chosen_word=word_list[v]
length_word=len(chosen_word)
display=[]
user_guessed_letters=[]
for letter in chosen_word:
  display.append("_")
while "_" in display:
  if len(user_guessed_letters) > 1 :  
    print(f'You have already used these letters {" ".join(user_guessed_letters)}')
  guess=input("Guess a letter:\n").lower()
  clear()
  if guess.isalpha == 1 :
    print("Please enter one alphabet only")
    lives-=1
    print(stages[lives])
  if letter_in_word(guess,user_guessed_letters):
    print(f"You have already used this letter {guess} to guess.")
  if not letter_in_word(guess,user_guessed_letters):
    user_guessed_letters.append(guess)
  for index in range(length_word):
    letter=chosen_word[index]
    if guess == letter:
      display[index]=guess
  if not letter_in_word(guess,chosen_word) and not letter_in_word(guess,user_guessed_letters):
    print(f"the letter you have guessed {guess} is not in the letter. You lose a life.")
    lives-=1
    print(stages[lives])
    if lives == 0:
      print("You lose.")
      print(f'the letter was {" ".join(chosen_word)}')
      break
  print(f'{" ".join(display)}')
  if "_" not in display:
    print(f'{"".join(display)}')
    print("You win!")