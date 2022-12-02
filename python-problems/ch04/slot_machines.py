# ccc00s1, slot machines

Q = int(input()) # number of quarters

plays_a = int(input())
plays_b = int(input())
plays_c = int(input())

limit_a = 35
limit_b = 100
limit_c = 10

machine = 'A'

plays = 0

while Q > 0:
    
    if machine == 'A':
        plays_a += 1
        if plays_a == limit_a:
            Q = Q + 30
            plays_a = 0
        machine = 'B'

    elif machine == 'B':
        plays_b += 1
        if plays_b == limit_b:
            Q = Q + 60
            plays_b = 0
        machine = 'C'

    elif machine == 'C':
        plays_c += 1
        if plays_c == limit_c:
            Q = Q + 9
            plays_c = 0
        machine = 'A'

    Q = Q - 1 # drop the number of quarters by one
    plays += 1
print(f'Martha plays {plays} times before going broke.')

