#######################################################################
# Name: selectionSort 
# Parameters: i, j, n, ...
# Author: XXXX
def selectionSort(array, n):
    
    for i in range(n):
        jMin = i
 
        for j in range(jMin + 1, n):
            # select the minimum element in every iteration
            if array[j] < array[jMin]:
                jMin = j
         # swapping the elements to sort the array
        (array[i], array[jMin]) = (array[jMin], array[i])

#######################################################################


### Original array to sort
a = [7, 34, 8, 6, 12, 2, 1, 5,3,4]

### get the length
n = len(a)

### call the selectionSort
selectionSort(a, n)

print('Sorted array:')
print(a)
