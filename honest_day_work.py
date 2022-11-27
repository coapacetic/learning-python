# Input
P = int(input()) # Litres of paint
B = int(input()) # Litres / bottle cap
D = int(input()) # Pokedollars / badge

# Process
badges = P // B # note to self, `//` is used for integer division
remaining_paint = P % B
profit = badges * D + remaining_paint * 1

# Output
print(profit)