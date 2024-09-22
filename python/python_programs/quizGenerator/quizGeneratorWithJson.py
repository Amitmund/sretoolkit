import json
import random

class QuizGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()

    def load_questions(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def generate_quiz(self, num_questions):
        questions = random.sample(self.questions, num_questions)
        return questions

    def ask_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        answer = input("Enter the correct option number: ")
        if question['options'][int(answer) - 1] == question['correct']:
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is {question['correct']}")

    def start_quiz(self, num_questions):
        questions = self.generate_quiz(num_questions)
        for question in questions:
            self.ask_question(question)

if __name__ == "__main__":
    quiz = QuizGenerator('/Users/amitmund/Downloads/github.com/Amitmund/sretoolkit/python/python_programs/quizGenerator/questions.json')
    quiz.start_quiz(5)  
