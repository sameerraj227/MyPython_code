import numpy as np

array_2d = np.array([[1,2,3],[4,5,5]])
print(array_2d)

# multi-dimensional array

import numpy as np
matrix= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)   
np.shape(matrix)  # Output: (3, 3)


# array with zeros(rows, columns)

import numpy as np
zero_array = np.zeros((3)) # 3
print(zero_array) 


# array with ones(rows, columns)
import numpy as np  
ones_array = np.ones((3, 3))  # 3 rows, 3 columns
print(ones_array)  

# full function
import numpy as np  
full_array= np.full((3, 3), 7)  # 3 rows, 3 columns, filled with 7
print(full_array)

# array with random values using random function
import numpy as np
random_array = np.random.rand(3, 3)  # 3 rows, 3 columns with random values
print(random_array)

# array with Range func(arange)

import numpy as np
range_array = np.arange(1, 10, 2)
print(range_array)  

# identity matrix (1 in diagonal)  EYE FUNC
import numpy as np
identity_matrix = np.eye(3)
print(identity_matrix)