from bubble_sort import bubble_sort
from linear_search import linear_search
from binary_search import binary_search
from get_random import get_random
import time
import random


if __name__ == "__main__":
    # runs a long time!
    
    # open csv to write results to
    outfile = open("experiments_results.csv", "w")
    outfile.write("Search Alg\tList size\tSearch time\n") # header of file
    functions = [linear_search, binary_search]  # two search functions to check

    for f in functions:
        for lenlist in [10, 100, 1000]: # different list lengths to search
            total_run_time = 0
            for i in range(10000):      # number of times to average over
                lst = get_random(lenlist)   # list of random numbers
                if f == binary_search:      # if binary search
                    lst = bubble_sort(lst)  # sort list first
                target = random.randint(0,1000) # random target to find
                search_start = time.time()  # start timer
                f(lst, target)              # perform search
                search_stop = time.time()   # end timer
                search_running_time = search_stop - search_start # how long?
                total_run_time += search_running_time # add to running time
            total_run_time /= 10000 # average running time

            # append result to file
            outfile.write(f"{f}\t{lenlist}\t{total_run_time}\n")
            #print(f"{search_running_time: .20f}")

outfile.close() # close file :)
