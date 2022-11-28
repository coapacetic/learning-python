# ccc18j2, occupy parking

ps_count = int(input())
day1 = str(input())
day2 = str(input())

both_days = 0

for i in range(ps_count):
    if day1[i] == 'C' and day2[i] == 'C':
        both_days += 1

print(both_days)
