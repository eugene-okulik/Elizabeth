import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])

if bonus:
    print(f'${salary + random.randrange(10, 1000)}')
else:
    print(f'${salary}')
