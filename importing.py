import random
import datetime

# Generate 2 random number

# Between 0 - 1
first_number = random.random()
# Between 1 - 10
second_number = random.randrange(1, 10)
print(first_number)
print(second_number)

# Use of datetime to get another random number
dt = datetime.datetime.timestamp(datetime.datetime.now())

random_number = random.randint(second_number, int(round(dt)))

print(random_number)
