# coci18c4p1, elder

elder_wiz = str(input())
N = int(input())

duels = []
holders = [elder_wiz]

for i in range(N):
    duels.append(str(input()))

for duel in duels:
    winner = duel[0]
    loser = duel[2]
    if loser == elder_wiz:
        elder_wiz = winner
        if elder_wiz not in holders:
            holders.append(elder_wiz)

print(elder_wiz)
print(len(holders))
