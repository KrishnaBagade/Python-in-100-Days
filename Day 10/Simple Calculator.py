from art import logo
from replit import clear
print(logo)
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def remainder(n1,n2):
  return n1%n2

def floor(n1,n2):
  return n1//n2

def exponent(n1,n2):
  return n1**n2

operations= {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  "%":remainder,
  "//":floor,
  "**":exponent,
}

def calculator():
  num1=(input("What is the first number?: "))
  if num1.isdigit():
    num1f=float(num1)
    should_continue=True
    while should_continue:
      num2=(input("What is the next number?: "))
      if num2.isdigit():
        num2f=float(num2)
        for key in operations:
          print(key)
        operation_chosen=input("Pick an operation from the above line: ")
        answer=operations[operation_chosen](num1f,num2f)
        print(f"{num1f} {operation_chosen} {num2f} = {answer}")
        user_choice=input(f"Type 'y' to continue calculating with {answer}, or Type 'z' to enter new numbers. or 'n to exit the program.': ")
        clear()
        if user_choice == "n":
          should_continue=False
        elif user_choice == 'y':
          num1f=(answer)
          continue
        elif user_choice == 'z':
          calculator()
      else:
        print("please enter a number")
  else:
    print("please enter a number")

calculator()
        