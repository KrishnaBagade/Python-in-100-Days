import random
while True:
  print(random.randint(0,6))
  print(random.random())
  love_score=random.randint(1,100)
  print(f"Your love score is {love_score}")
  ans = input("Do you want to generate a number again?<Y/ N>")
  if ans.lower() == "n":
    break
    