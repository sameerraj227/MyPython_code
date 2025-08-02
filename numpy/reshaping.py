#changing rows and columns
import numpy as np 
arr = np.array([1, 2, 3,4, 5, 7, 8, 9])
arr.shape = (2, 4)  # Reshape to 2 rows and 4 columns
print(arr)
#doesn't change the original array just return the view(modify the original array)

# multi-dimensional array into 1d

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr.flatten())  # Convert to 1D array  (returns a copy doesn't modify the original array)
print(arr.ravel())    # Convert to 1D array (returns a view if possible)
