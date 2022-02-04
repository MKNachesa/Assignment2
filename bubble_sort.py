def bubble_sort(lst):
    swap = False
    for i, e in enumerate(lst[:-1]):
        if e > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swap = True
    if swap == True:
        bubble_sort(lst)
    return lst


if __name__ == "__main__":
    to_sort = [2,4,1,4,6,8,2,7,10234,1,4134,5345,2]
    print(to_sort)
    to_sort = bubble_sort(to_sort)
    print(to_sort)
