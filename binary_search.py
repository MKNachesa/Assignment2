import time

def binary_search(lst, target):
    """performs a binary search on lst to find the target.
    Returns the index of the target or -1 if it is not found."""
    
    # we're down to 1 element, is this the element we're looking for?
    if len(lst) == 1 and target != lst[0]:
        return -1   # not the element, so it doesn't exist in the list
    else:   # list size > 2
        i = len(lst) // 2           # find the middle of the list
        if target < lst[i]:         # is the target to the left of the middle?
            i = binary_search(lst[:i], target)  # search in the left side
        elif target > lst[i]:                   # is the target on the right?
            i = binary_search(lst[i:], target)  # search on the right
        return i                    # target was neither larger nor smaller
                                    # so the element at i is the target


if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9,10]
    target = 11
    print(binary_search(lst, target))

    search_start = time.time()
    call_search_function = binary_search(lst, target)
    search_stop = time.time()
    search_running_time = search_stop - search_start
