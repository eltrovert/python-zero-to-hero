from data import question_data
from quetion_model import Question
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    questionText = question["text"]
    # print(questionText)
    questionAnswer = question["answer"]
    # print(questionAnswer)
    questionGenerator = Question(questionText, questionAnswer)

    questionBank.append(questionGenerator)

quiz = QuizBrain(questionBank)

while quiz.questionExist():
    quiz.nextQuestion()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")