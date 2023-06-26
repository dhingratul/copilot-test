from functools import lru_cache

FIVE_NAMES = ['A', 'B', 'C', 'D', 'E']

AGES = [10, 20, 30, 40, 50]

MAP_NAME_TO_AGES = dict(zip(FIVE_NAMES, AGES))

def average_age():
    return sum(AGES) / len(AGES)

def fibonnaci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

@lru_cache(maxsize=None)
def fibonnaci_cached(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnaci_cached(n - 1) + fibonnaci_cached(n - 2)

LAST_NAMES = ['A', 'B', 'C', 'D', 'E']

if __name__ == "__main__":
    print(average_age())