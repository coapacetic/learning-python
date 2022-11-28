# ccc11s1, English or French

N = int(input())
lines = list()

for i in range(N):
    line_of_text = str(input())
    lines.append(line_of_text)

t_count = 0
s_count = 0

for line in lines:
    for char in line:
        if char == 'T' or char == 't':
            t_count += 1
        elif char == 'S' or char == 's':
            s_count += 1
        else:
            continue

if t_count > s_count:
    print('English')
else:
    print('French')