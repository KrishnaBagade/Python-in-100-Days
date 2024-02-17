from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
  q1 = question["text"]
  q2 = question["answer"]
  new_question = Question(q1,q2)
  question_bank.append(new_question)

quiz =  QuizBrain(question_bank)
questions_remain = True

while questions_remain:
  quiz.next_question()
  val = quiz.still_has_questions()
  if val == 0:
    questions_remain = False
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")