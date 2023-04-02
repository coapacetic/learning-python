# coci08c1p2, ptice

N=int(input()) # number of questions
answers=str(input()) # string of correct answers

A = ['A','B','C']
B = ['B','A','B','C']
G = ['C','C','A','A','B','B']

adrian=str()
bruno=str()
goran=str()

n = 0

# create answers for each boy

while n < N:
    adrian += A[n % 3]
    bruno += B[n % 4]
    goran += G[n % 6]
    n += 1

# check scores

a_score = 0
b_score = 0
g_score = 0

for i in range(len(answers)):
    if answers[i] == adrian[i]:
        a_score += 1
    if answers[i] == bruno[i]:
        b_score += 1
    if answers[i] == goran[i]:
        g_score += 1

scores = [a_score, b_score, g_score]
names = ['Adrian','Bruno','Goran']

M = max(a_score, b_score, g_score)

print(M)

for i in range(len(scores)):
    if scores[i] == M:
        print(names[i])