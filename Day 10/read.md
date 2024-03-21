Calculator Program
This Python program is a simple calculator that allows the user 
to perform basic arithmetic operations on two numbers. The program 
includes addition, subtraction, multiplication, division, remainder,
floor division, and exponentiation.

How to Use
Run the program.
Enter the first number when prompted.
Choose an operation from the available options: +, -, *, /, %, //, **.
Enter the second number.
The program will display the result of the chosen operation.
You can choose to continue using the result for further calculations,
enter new numbers, or exit the program.
Code Structure
logo: The calculator's ASCII art logo is imported from the art module.

clear: The clear function from the replit module is used to clear the 
console screen.

Basic Arithmetic Functions:

add(n1, n2): Addition
subtract(n1, n2): Subtraction
multiply(n1, n2): Multiplication
divide(n1, n2): Division
remainder(n1, n2): Remainder after division
floor(n1, n2): Floor division
exponent(n1, n2): Exponentiation
operations Dictionary:

Maps operation symbols to their respective functions.
calculator Function:

Takes user input for the first number.
Validates the input to ensure it is a digit.
Continues to prompt the user for the next number and the operation
until the user decides to exit.
Clears the console screen after each iteration.
Handles user choices to continue with the result, enter new numbers,
or exit.
How to Run
To run the program, make sure you have the art module installed:

bash
Copy code
pip install art
Then, execute the Python script:

bash
Copy code
python filename.py
Notes
The program uses float for numerical operations to handle both integer 
and decimal inputs.

Users can choose to continue calculations, enter new numbers, or exit 
the program at each step.

The program provides a clear and user-friendly interface for performing 
basic arithmetic operations.