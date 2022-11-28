# coci12c5p1, Ljestvica

sequence = str(input())

# Break up the string into a list by measure
sequence = sequence.split('|')

c_major_count = 0
a_minor_count = 0

for i in range((len(sequence))):
    measure = sequence[i]
    if measure[0] in ['C','F','G']:
        c_major_count += 1
    elif measure[0] in ['A','D','E']:
        a_minor_count += 1

if c_major_count > a_minor_count:
    print('C-dur')
elif c_major_count < a_minor_count:
    print('A-mol')
else:
    if sequence[-1][-1] == 'C': # check the first tone of the final measure
        print('C-dur')
    else:
        print('A-mol')