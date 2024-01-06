print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total = 0
total1 = 0

#step1 create list of names to apply logic to , create list of charcters to check
names = [name1, name2]
trues = ["t", "r", "u", "e"]
loves = ["l", "o", "v", "e"]
#step2 print first for loop variable
for word in names:
  for ch in word:
    if ch in trues:
      total += 1
    if ch in loves:
      total1 += 1

score = total * 10 + total1
if 10 > score > 90:
  print(f"Your score is {score}, you go like coke and mentos.")
elif 40 < score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
