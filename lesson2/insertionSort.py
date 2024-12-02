#######################################################################
# Name: insertionSort 
# Parameters: i, j, n, ...
# Author: XXXX
def insertionSort(array, n):
   
    # loop through all array
    for i in range(n):

        j = i

        while j > 0 and array[j-1] > array[j]:
            # swapping the elements to sort the array
            (array[j], array[j-1]) = (array[j-1], array[j])
            j = j -1
        i = i +1

#######################################################################


### Original array to sort
a = [7, 34, 8, 6, 12, 2, 1, 5,3,4]

### get the length
n = len(a)
print('Length A=%d' % n)

### call the selectionSort
insertionSort(a, n)

print('Sorted array:')
print(a)
