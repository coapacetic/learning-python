# Input
a_three = int(input())
a_two = int(input())
a_one = int(input())
b_three = int(input())
b_two = int(input())
b_one = int(input())

# Process
a_points = a_three * 3 + a_two * 2 + a_one
b_points = b_three * 3 + b_two * 2 + b_one

# Output
if a_points > b_points:
    print('A')
elif a_points < b_points:
    print('B')
else:
    print('T')
