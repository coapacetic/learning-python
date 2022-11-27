# coci18c3p1, magnus

word = str(input())

honi_count = 0
last_letter = False

for char in word:
    # print(f'Current Letter: {char}')
    if char == 'H' and last_letter == False:
        last_letter = 'H'
        continue
    elif char == 'O' and last_letter == 'H':
        last_letter = 'O'
        continue
    elif char == 'N' and last_letter == 'O':
        last_letter = 'N'
        continue
    elif char == 'I' and last_letter == 'N':
        honi_count += 1
        last_letter = False
        continue
    else:
        continue

print(honi_count)