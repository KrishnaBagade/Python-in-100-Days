from art import logo

print(logo)
while True:
  bidder_dic = {}
  bidder = input("What is your name?\n")
  bid_amt = input("What is the amount you wish to bid for?\n$")
  if bid_amt.isdigit():
   bid_amtint = int(bid_amt)
   bidder_dic[bidder] = bid_amtint
  else:
    print("Please enter proper numbers and avoid disrupting the auction.")
  check = input("Are there any other bidders?\n")
  if check == "no":
    break
bid_value = 0
bid_name = ""
for bidder in bidder_dic:
  if bidder_dic[bidder] > bid_value:
    bid_value = bidder_dic[bidder]
    bid_name = bidder
  else:
    continue
print(f"The highest bidder is {bid_name} who bid for ${bid_value}.")
with open("bids.txt",mode="a") as file:
  file.write(f"\nThe highest bidder is {bid_name} who bid for ${bid_value}.")

  