# ccc15j2, happy or sad

input_message = str(input())

happy = ':-)'
sad = ':-('

happy_count = input_message.count(happy)
sad_count = input_message.count(sad)

if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count > sad_count:
    print('happy')
elif happy_count < sad_count:
    print('sad')
else:
    print('unsure')