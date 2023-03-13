class QuizBrain:

    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("That's wrong")
        print(f"The correct answer is {correctAnswer}")
        print(f"Your currnect score is: {self.score}/{self.questionNumber}")
        print("\n")
    
    def questionExist(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False)")
        self.checkAnswer(userAnswer, currentQuestion.answer)

    