import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question.question)
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        answer = input("Enter the \033[31mnumber[1 or 2 or 3 or 4]\033[0m of your answer: ")
        if question.options[int(answer) - 1] == question.answer:
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is {question.answer}.\n")

    def start_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.ask_question(question)
        print(f"Quiz finished. Your final score is {self.score}/{len(self.questions)}")

# Create questions
question1 = Question("What is 2 + 2?", ["8", "4", "6", "10"], "4")
question2 = Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "Jupiter")
question3 = Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"], "Leonardo da Vinci")

# Create quiz
quiz = Quiz([question1, question2, question3])

# Start quiz
quiz.start_quiz()   