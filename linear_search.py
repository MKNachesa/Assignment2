import get_random

def linear_search(lst, target, n=0):
    try:
        if lst[n] == target:
            return n
        else:
            return linear_search(lst, target, n+1)
    except IndexError:
        return -1


if __name__ == "__main__":
    lst = get_random.get_random(10)
    print(lst)
    target = lst[4]
    print(linear_search(lst, target))
