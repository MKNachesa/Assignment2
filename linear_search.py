import get_random

def linear_search(lst, target, n=0):
    """Performs a linear search on lst to find the target.
    Returns the index of the target or -1 if the target is not found."""
    try:
        if lst[n] == target:    # is the target is at position n?
            return n
        else:                   # if it isn't, try the next position
            return linear_search(lst, target, n+1)
    except IndexError:  # we're outside the list, so the target doesn't exist
        return -1


if __name__ == "__main__":
    lst = get_random.get_random(10)
    print(lst)
    target = lst[4]
    print(linear_search(lst, target))
