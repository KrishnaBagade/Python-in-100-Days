# The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random


def draw_card():
  card_drawn=cards[random.randint(0,12)]
  return card_drawn

def check_for_ace(user_drawn_card,index):
  if "11" in user_drawn_card[index]:
    print(user_drawn_card)
    user_choice=input("You have drawn an ace do you want to use it as 1 or 11? ")
    user_drawn_card.remove("11")
    if user_choice == "11":
      user_drawn_card.append(user_choice)
      return user_drawn_card
    else:
      user_drawn_card.append("1")
      return user_drawn_card

def check_for_winner(card_value,count=0):
  if card_value > 21 :
    card_value-=1
    count =check_for_winner(card_value, count+1)
  elif card_value < 21 :
    card_value+=1
    count=check_for_winner(card_value, count+1)
  return count

bet=1000

while True:
  if bet==0:
    print("You added $100 to your stakes.")
    bet+=100
  print(f"Amount you can bet on ${bet}")
  bet_amount=input("How much would you like to bet for?")
  if bet_amount.isdigit():
    bet_amount_i=int(bet_amount)
    if bet_amount_i>bet:
      print("You chose to go All in")
      bet_amount_i=bet
    cards=["11","2","3","4","5","6","7","8","9","10","10","10","10"]
    card_category=["Hearts","Diamond","Spades","Clubs"]
    user_drawn_card=[]
    computer_drawn_card=[]
    user_card_value=0
    computer_card_value=0
    user_drawn_card.append(draw_card())
    check_for_ace(user_drawn_card,len(user_drawn_card)-1)
    print(f"You drew a {user_drawn_card[len(user_drawn_card)-1]} of {card_category[random.randint(0,3)]}")
    user_drawn_card.append(draw_card())
    check_for_ace(user_drawn_card,len(user_drawn_card)-1)
    print(f"You drew a {user_drawn_card[len(user_drawn_card)-1]} of {card_category[random.randint(0,3)]}")
    user_card_value=int(user_drawn_card[0])+int(user_drawn_card[1])
    print(user_drawn_card)
    print(f"current score = {user_card_value}")
    if user_card_value== 21:
      print("you win")
    else:
      computer_drawn_card.append(draw_card())
      print(f"Dealer drew a {computer_drawn_card[len(computer_drawn_card)-1]} of {card_category[random.randint(0,3)]}")
      computer_drawn_card.append(draw_card())
      computer_card_value_show=(computer_drawn_card[0],"?")
      print(computer_card_value_show)
      computer_card_value=(int(computer_drawn_card[0])+int(computer_drawn_card[1]))
      while True:
        user_chose=input("Type 'hit' to draw another card or type 'stand' to pass: ")
        if user_chose == "hit":
          user_drawn_card.append(draw_card())
          check_for_ace(user_drawn_card,len(user_drawn_card)-1)
          user_card_value+=int(user_drawn_card[2])
          if user_card_value == 21:
            print(f"You drew a {user_drawn_card[2]} of {card_category[random.randint(0,3)]}, You win")
            bet+=bet_amount_i
          elif user_card_value>21:
            print(f"You drew a {user_drawn_card[2]} of {card_category[random.randint(0,3)]}, You went over 21. You lose.")
            bet-=bet_amount_i
            break
          if computer_card_value<17:
           computer_drawn_card.append(draw_card())
          print(f"The dealer drew a {computer_drawn_card}")
        elif user_chose == "stand":
          print("You chose not to draw a card.")
          if computer_card_value<17:
           computer_drawn_card.append(draw_card())
          print(f"The dealer drew a {computer_drawn_card}")
          break
        else:
          print("You entered a value other than hit or stand starting hand reset.")
        continue
      if len(computer_drawn_card)>2:
       computer_card_value+=int(computer_drawn_card[2])
      user_count=check_for_winner(user_card_value)
      computer_count=check_for_winner(computer_card_value)
      if user_count>computer_count and user_count <= 21 :
        print(f"Your hand score was {user_card_value} and Dealer's hand score was {computer_card_value}, You lose ${bet_amount_i}.")
        bet-=bet_amount_i
        continue_=input("Do you wish to go again 'y' or 'n' ? ").lower()
        if continue_=="n":
         break
      elif user_count<computer_count and user_count <= 21 :
       print(f"Your hand score was {user_card_value} and Dealer's hand score was {computer_card_value}, You win ${bet_amount_i}.")
       bet+=bet_amount_i
       continue_=input("Do you wish to go again 'y' or 'n' ? ").lower()
       if continue_=="n":
         break
      elif user_count==computer_count:
        print(f"Your hand score was {user_card_value} and Dealer's hand score was {computer_card_value}, Its a draw you keep your ${bet_amount_i}.")
        continue_=input("Do you wish to go again 'y' or 'n' ? ").lower()
        if continue_=="n":
         break
  else:
    print("Please enter a proper number to bet on")
print(f"Your winnings were ${bet-1000}")
#hit to drawn card stand to not draw card