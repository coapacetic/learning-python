# ccc02j2, AmeriCanadian

# inputs

while True:
    word = str(input())

    if word == 'quit!':
        break

    if word[-2:] == 'or' and len(word) > 4 and word[-3] not in ['a','e','i','o','u','y']:
        word = word[0:-2] + 'our'
        print(word)

    else:
        print(word)
