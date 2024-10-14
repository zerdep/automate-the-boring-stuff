import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_list = ''
    for i in range(100):
        coin_list += str(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    print(coin_list)
    if ('111111' in coin_list) or ('000000' in coin_list):
        numberOfStreaks += 1

print(numberOfStreaks)
print('Chance of streak: %s%%'  %(numberOfStreaks / 100))