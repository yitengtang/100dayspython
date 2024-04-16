from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_txt = question['text']
    question_answer = question['answer']
    questions = Question(question_txt, question_answer)
    new_question = Question(question_txt, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed your quiz")
print(f"Your final score is {quiz.score}/{quiz.q_number}")