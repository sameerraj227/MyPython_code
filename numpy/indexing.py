import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1=np.array([1,2,32,3,43,453,543,453,45,34,5,34,5,34,5,34,5,34,5,34,5])
print(arr[0, 1])  # Access element at row 0, column 1
print(arr1[5])    # Access element at index 5
print(arr1[-6])  # Access element at index -6 (from the end)



#slicing 
import numpy as np
arr1=np.array([1,2,32,3,43,453,543,453,45,34,5,34,5,34,5,34,5,34,5,34,5])
print(arr1[2:5])  # Slice from index 2 to 4 (5 is exclusive)
print(arr1[5:])   # Slice from index 5 to the end   
print(arr1[:5])   # Slice from the start to index 4
print(arr1[-5:])  # Slice from the last 5 elements
print(arr1[::2])  # Slice with a step of 2 (every second element)

# filtering
import numpy as np
arr1 = np.array([1, 2, 32, 3, 43, 453, 543, 453, 45, 34, 5, 34, 5, 34, 5, 34, 5, 34, 5, 34])
print(arr1[arr1 > 100])  # Filter elements greater than 100
print(arr1[arr1 % 2 == 0])  # Filter even elements

#fancy indexing
import numpy as np
arr1 = np.array([1, 2, 32, 3, 43, 453, 543, 453, 45, 34, 5, 34, 5, 34, 5, 34, 5, 34, 5, 34])
print(arr1[[0,2,4]])  # Access elements at indices 0, 2, and 4