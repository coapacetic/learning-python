# ccc15j1, Special Day

month = int(input())
day = int(input())

# we will compare the given date to February 18

if month < 2:
    print('Before')
elif month > 2:
    print('After')
else:
    if day < 18:
        print('Before')
    elif day > 18:
        print('After')
    else:
        print('Special')