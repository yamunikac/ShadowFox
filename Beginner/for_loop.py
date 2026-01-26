import random
# dice rolling
rolls = []
for i in range(20):
    rolls.append(random.randint(1, 6))
print(rolls)
print(rolls.count(6))
print(rolls.count(1))
count = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        count += 1
print(count)
