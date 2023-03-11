amount = input('How much is the check?\n')
tip = input('What percentage do you want to tip?\n')

total = int(amount) + int(amount) * float(tip)

print('$',total) 