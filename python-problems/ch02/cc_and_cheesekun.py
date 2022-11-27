# dmopc16c1p0, CC and cheesekun

w = int(input()) # width of pizza
c = int(input()) # percentage of pizza with extra cheese

if w == 3 and c >= 95:
    M = 'absolutely'
elif w == 1 and c <= 50:
    M = 'fairly'
else:
    M = 'very'


print(f'C.C. is {M} satisfied with her pizza.')