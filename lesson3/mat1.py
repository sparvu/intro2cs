A = [[1, 2, 3], [4, 5, 6], [7,8,9]]

for row in A:
  
    # Traversing each element
    # in the current row
    for x in row:
        print(x, end=" ")
    print()

print("First element of first row:", A[0][0])
print("Second element of second row:", A[1][2])
print("Second element of third row:", A[2][1])
