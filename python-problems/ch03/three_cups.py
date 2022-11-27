# coci06c5p1, Three Cups

moves = str(input())

# execute the moves in the string

position = 1

for move in moves:
    # print(move)
    if move == 'A':
        if position == 1:
            position = 2
        elif position == 2:
            position = 1
        else:
            continue
    elif move == 'B':
        if position == 2:
            position = 3
        elif position == 3:
            position = 2
        else:
            continue
    else:
        if position == 3:
            position = 1
        elif position == 1:
            position = 3
        else:
            continue
    # print(position)

print(position)