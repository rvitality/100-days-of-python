from multiprocessing import current_process


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        q_text = current_question.text
        q_answer = current_question.answer

        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {q_text} (t/f): ")

        self.check_answer(q_answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        formatted_user_answer = "True" if user_answer == "t" else "False"
        is_correct = correct_answer.lower() == formatted_user_answer.lower()

        if is_correct:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
            print(f"The correct answer was: {correct_answer}")

        print(f"Your current score is: {self.score}/{self.question_number}")
