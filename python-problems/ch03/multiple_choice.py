# ccc11s2, multiple choice

number_of_questions = int(input())

# responses
responses = list()

for i in range(number_of_questions):
    responses.append(str(input()))

# answers
answers = list()

for i in range(number_of_questions):
    answers.append(str(input()))

# grade

score = 0

for i in range(number_of_questions):
    if responses[i] == answers[i]:
        score += 1
    else:
        continue

print(score)
