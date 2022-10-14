from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))

q_brain = QuizBrain(question_bank)

correct_answers = 0
wrong_answers = 0

print(
    """
     *
    _|                              __
   (__  What's the correct answer?   _)
                                     |
                                     *
"""
)

while q_brain.still_has_questions():
    print("\n")
    q_brain.next_question()

# if the user answered all the questions

print("\n---------------------------------------------------------")
print("You've completed the quiz!")
print(f"Final score: {q_brain.score}/{len(q_brain.question_list)}")
print("-----------------------------------------------------------")
