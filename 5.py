import random

def roll_dice():
    return random.randint(1, 6)

def series_of_ones():
    count = 0
    for _ in range(1000):
        roll = roll_dice()
        count += 1
        if roll == 1:
            count_ones = 1
            for _ in range(2):
                next_roll = roll_dice()
                count += 1
                if next_roll == 1:
                    count_ones += 1
                    if count_ones == 3:
                        return count
    return float('inf')  # Return infinity if the series of ones doesn't occur within 1000 rolls

def series_of_not_ones():
    count = 0
    for _ in range(1000):
        roll = roll_dice()
        count += 1
        if roll != 1:
            count_not_ones = 1
            for _ in range(13):
                next_roll = roll_dice()
                count += 1
                if next_roll != 1:
                    count_not_ones += 1
                    if count_not_ones == 14:
                        return count
    return float('inf')  # Return infinity if the series of not ones doesn't occur within 1000 rolls

def monte_carlo_simulation(num_simulations):
    success_count = 0
    for _ in range(num_simulations):
        ones_series = series_of_ones()
        not_ones_series = series_of_not_ones()
        if ones_series < not_ones_series:
            success_count += 1
    return success_count / num_simulations

num_simulations = 10000
probability = monte_carlo_simulation(num_simulations)
print("Вероятность:", probability)
