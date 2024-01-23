import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > max or quantity < 0:
        return []

    result = set()

    for _ in range(quantity):
        random_int = random.randint(min, max)
        result.add(random_int)

    result = list(result)
    result.sort()
    return result


lottery_numbers = get_numbers_ticket(45, 209, 10)
print(f"Your lottery numbers - {lottery_numbers}")
