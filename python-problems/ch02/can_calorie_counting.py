# Input
burger = int(input()) - 1
side = int(input()) - 1
drink = int(input()) - 1
dessert = int(input()) - 1

# Process
burgers = [461, 431, 420, 0]
drinks = [130, 160, 118, 0]
sides = [100, 57, 70, 0]
desserts = [167, 266, 75, 0]

total_calories = burgers[burger] + drinks[drink] + sides[side] + desserts[dessert]

# Output
print(f'Your total Calorie count is {total_calories}.')