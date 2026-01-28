import random

# Dice simulation
rolls = []
for i in range(20):
    rolls.append(random.randint(1, 6))
print("Dice Rolls:", rolls)
print("Number of 1s:", rolls.count(1))
print("Number of 6s:", rolls.count(6))


# Jumping Jacks
completed = 0
for i in range(10):
    completed += 10
    tired = input("Are you tired? ")

    if tired.lower() in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? ")
        if skip.lower() in ["yes", "y"]:
            break
print("You completed", completed, "jumping jacks")
