from bubble_sort import bubble_sort
from linear_search import linear_search
from get_random import get_random
import time
import random


if __name__ == "__main__":
    lenlist = 20
    lst = get_random(lenlist)
    search_start = time.time()
    target = random.choice([lst[random.randint(0, lenlist-1)], 100001])
    print(linear_search(lst, target))
    search_stop = time.time()
    search_running_time = search_stop - search_start
    print(f"{search_running_time: .20f}")
