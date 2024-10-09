def get_numbers_ticket(min, max, quantity):
    import random
    if min >= 1 and max <=1000 and min < quantity < max:
        return random.sample(range(min, max), quantity)
    else:
        return []

print(get_numbers_ticket(1, 89, 7))