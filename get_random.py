import random

def get_random(n):
    """returns a list of numbers of length n between 0 and 100000"""
    return [random.randint(0,100000) for _ in range(n)]

if __name__ == "__main__":
    print(get_random(10))

