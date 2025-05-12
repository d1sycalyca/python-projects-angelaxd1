from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
'''write a for loop to iterate over the question data'''
'''create a question object for each entry in the question class'''
'''Append each question object to the question bank'''
question_bank = []
for each_question in question_data:
    question_text = each_question["text"]
    question_answer = each_question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
if quiz.score/quiz.question_number < 0.5:
    print(f"Oh hell nah twin! {quiz.score} out of {quiz.question_number}. {quiz.score}!!! Not even 50%. "
          f"Yo ahh finna get swish cheesed if you don't stop playing!!")
else:
    print("Ayyy lesss go. You finished the quiz cuhhh.")
    print(f" Your final score is {quiz.score}/{quiz.question_number}")