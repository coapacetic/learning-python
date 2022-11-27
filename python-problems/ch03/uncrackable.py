# wc17c3j3, uncrackable

password = str(input())

length = len(password) 

lower_count = 0
upper_count = 0
num_count = 0

for char in password:
    if char >= 'a' and char <= 'z':
        lower_count += 1
    elif char >='A' and char <= 'Z':
        upper_count += 1
    elif int(char) >= 0 and int(char) <= 9:
        num_count += 1

if lower_count >= 3 and upper_count >= 2 and num_count >= 1 and length >= 8 and length <= 12:
    print('Valid')
else:
    print('Invalid')

