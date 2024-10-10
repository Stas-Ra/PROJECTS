def get_numbers_ticket(min, max, quantity):
    import random
    if min >= 1 and max <=1000 and max - min >= quantity:
        return random.sample(range(min, max+1), quantity)
    else:
        return []

print(sorted(get_numbers_ticket(1, 36, 6)))