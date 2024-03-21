Overview
The QuizBrain class is designed to facilitate a simple quiz game.
It keeps track of questions, user answers, and scores during the quiz.

Class Attributes
question_number: Integer representing the current question number.
question_list: List of Question objects containing questions and answers.
count: Integer representing the remaining number of questions.
score: Integer representing the user's score.
Class Methods
1. __init__(self, q_list)
Description: Initializes a new instance of the QuizBrain class.
Parameters:
q_list: List of Question objects representing the quiz questions.
2. next_question(self)
Description: Presents the next question to the user and checks the answer.
User Input: Accepts the user's True/False answer via the input prompt.
Output: Checks the user's answer against the correct answer and updates 
3. the score.
3. still_has_questions(self)
Description: Checks if there are still questions remaining in the quiz.
Output: Returns True if there are remaining questions, otherwise False.
4. check_answer(self, user_answer, correct_answer)
Description: Compares the user's answer with the correct answer and updates
5. the score.
Parameters:
user_answer: User's True/False answer.
correct_answer: Correct True/False answer for the current question.
Example Usage
python
Copy code
# Example Quiz
questions = [
    Question("Is the sky blue?", "True"),
    Question("Are dogs mammals?", "True"),
    Question("Is water wet?", "False"),
]

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz completed! Your final score is:", quiz.score)
Notes
Ensure that the Question class is defined before using the QuizBrain class.
The Question class is assumed to have attributes text for the question 
and answer for the correct answer.
The quiz runs until there are no more questions remaining.
User input is case-insensitive when comparing answers.
The correct answer for each question is displayed after the user responds.



