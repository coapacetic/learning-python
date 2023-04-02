# ecoo13r1p1, take a number

n_late = 0
n_served = 0
n_ticket = int(input())
actions = []

while True:
    action = str(input())
    if action == 'EOF':
        break
    actions.append(action)

n_line = 0

for action in actions:
    if action == 'TAKE':
        n_ticket += 1
        n_late += 1
        if n_ticket == 1000:
            n_ticket = 1
    if action == 'SERVE':
        n_served += 1
    if action == 'CLOSE':
        print(f'{n_late} {n_late - n_served} {n_ticket}')
        n_served = 0
        n_late = 0 
        
