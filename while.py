import math

def binary_sesarch(arr, search_el):
    #Find the middle of the arr

    start = arr[0]
    end = arr[-1]
    
    while True:
        middle = (start - end) / 2
        middle = math.floor(middle)
        if search_el == middle:
            return search_el
        elif search_el < middle:
            end = arr[middle]
        else:
            start = arr[middle]

binary_search()