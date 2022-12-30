# ccc08j2, Do the Shuffle

# b = button, n = number of times

## Solution with string slicing

songs = 'ABCDE'

button = 0

while button != 4:
    button = int(input())
    n = int(input())

    for i in range(n):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ""

for song in songs:
    output = output + song + ' '

print(output[:-1])



## Initial Solution

# b = 0
# n = 0
# playlist = ["A","B","C","D","E"]

# buttons = []
# presses = []

# while b != 4:
#     b = int(input())
#     n = int(input())
#     buttons.append(b)
#     presses.append(n)

# for i in range(len(buttons)):
#     if buttons[i] == 1:
#         for j in range(presses[i]): 
#             song = playlist[0]
#             playlist.pop(0)
#             playlist.append(song)
#     elif buttons[i] == 2:
#         for j in range(presses[i]): 
#             song = playlist[-1]
#             playlist.pop(-1)
#             playlist.insert(0, song)
#     elif buttons[i] == 3:
#         for j in range(presses[i]): 
#             song = playlist[0]
#             playlist.pop(0)
#             playlist.insert(1, song)
#     else:
#         break

# for song in playlist:
#     print(song, end=" ")
