import math

def binary_search(arr, search_el):

    start = 0
    end = len(arr) - 1
    found = False
      
    while (end - start) > 1:
        middle = start + (end-start)/2      
        middle = math.floor(middle)
        if search_el == arr[middle]:
            print('found')
            found = True
            return middle
        elif search_el < arr[middle]:
            end = middle
        else:
            start = middle
            
    if found == False: return 'not found' 
    
    

print(binary_search([4, 3, 24, 89, 33, 56], 100))