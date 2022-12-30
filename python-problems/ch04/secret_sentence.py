# coci08c3p2, secret sentence

s = str(input())

d = str()

i = 0

while i < len(s):
    if s[i] in ['a','e','i','o','u']:
        d = d + s[i]
        i = i + 3
    else:
        d = d + s[i]
        i = i + 1

print(d)