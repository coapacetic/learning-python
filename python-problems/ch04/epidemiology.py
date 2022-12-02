# ccc20j2, epidemiology

P = int(input())
N = int(input())
R = int(input())

day = 0
infected = N
total_infected = infected

while total_infected <= P:
    day += 1
    infected *= R
    total_infected = total_infected + infected 

print(day)