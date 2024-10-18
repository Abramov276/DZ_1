import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []

    if max - min + 1 < quantity:
        return []

    num = random.sample(range(min, max), quantity)
    return sorted(num)


print(f'Your tiket numbers: {get_numbers_ticket(1, 1000, 15)}')
