# coci16c1p1, data plan

X = int(input()) # allowance awarded per month
N = int(input()) # number of months

# Get usage by month in a list
month_usage = list()

for i in range(N):
    this_month = int(input())
    month_usage.append(this_month)

balance = 0 # initial balance

for month in month_usage:
    balance += X
    balance -= month

print(balance + X)
