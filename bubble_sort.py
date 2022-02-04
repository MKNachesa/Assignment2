def bubble_sort(lst):
    """Uses bubble sort to sort lst. Returns the sorted list"""
    swap = False
    for i, e in enumerate(lst[:-1]):
        if e > lst[i+1]:    # if the current element is larger than the next
            lst[i], lst[i+1] = lst[i+1], lst[i] # swap the two elements
            swap = True
    if swap == True:        # if a swap has been performed
        bubble_sort(lst)
    return lst              # no swap was performed, so list is sorted


if __name__ == "__main__":
    to_sort = [2,4,1,4,6,8,2,7,10234,1,4134,5345,2]
    #to_sort = [9,8,3,30,38,20,24,40,38,19,81]
    print(to_sort)
    to_sort = bubble_sort(to_sort)
    print(to_sort)
