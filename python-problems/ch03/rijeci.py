# coci13c3p1, rijeci

K = int(input())

## Method 1 - Using strings
# new_word = 'A'

# for i in range(K):
#     old_word = new_word
#     new_word = str()
#     for char in old_word:
#         if char == 'A':
#             new_word += 'B'
#         elif char == 'B':
#             new_word += 'BA'

# a_count = new_word.count('A')
# b_count = new_word.count('B')

# print(str(a_count) + ' ' + str(b_count))

## Method 2 - Another approach

a_current = 1
b_current = 0
a_next = 0
b_next = 0

for i in range(K):
    # calculate new counts
    b_next = b_current + a_current
    a_next = a_current - a_current + b_current

    # set new currents
    b_current = b_next
    a_current = a_next

print(str(a_current)+ ' ' +str(b_current))

    