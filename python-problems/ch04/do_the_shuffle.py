# ccc08j2, Do the Shuffle

# b = button, n = number of times

b = 0
n = 0
playlist = ["A","B","C","D","E"]

buttons = []
presses = []

while b != 4:
    b = int(input())
    n = int(input())
    buttons.append(b)
    presses.append(n)

for i in range(len(buttons)):
    if buttons[i] == 1:
        for j in range(presses[i]): 
            song = playlist[0]
            playlist.pop(0)
            playlist.append(song)
    elif buttons[i] == 2:
        for j in range(presses[i]): 
            song = playlist[-1]
            playlist.pop(-1)
            playlist.insert(0, song)
    elif buttons[i] == 3:
        for j in range(presses[i]): 
            song = playlist[0]
            playlist.pop(0)
            playlist.insert(1, song)
    else:
        break

for song in playlist:
    print(song, end=" ")
