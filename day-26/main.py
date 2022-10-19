import random
import pandas as pd

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# print(students_scores.items())


passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 60
}
# print(passed_students)

student_dict = {"student": ["Angela", "James", "Lily"], "scores": [56, 72, 90]}

# for (key, value) in student_dict.items():
#     print(key, value)


# student_df = pd.DataFrame(student_dict)

# for (index, row) in student_df.iterrows():
#     print(row.student, row.scores)

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {
    row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()
}
# print(nato_alphabet_dict)

# for (letter, code) in nato_alphabet_dict.items():
#     print(letter, code)

user_input = input("Enter a word: ").upper()
output = [nato_alphabet_dict[letter] for letter in user_input]
print(output)
