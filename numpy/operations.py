#shape (rows, columns)
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 5], [5, 6, 6], [6, 7, 8], [9, 10, 9]])
print(array.shape)

#size(total number of elements)

import numpy as np
array = np.array([[1, 2, 3], [4, 5, 5], [5, 6, 6], [6, 7, 8], [9, 10, 9]])
print(array.size)

# dtype(data type of elements)
import numpy as np  
array = np.array([[1, 2, 3], [4, 5, 5], [5, 6, 6], [6, 7, 8], [9, 10, 9]])
print(array.dtype)

# ndim(number of dimensions)
import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 5], [5, 6, 6], [6, 7, 8], [9, 10, 9]])
array_3d=np.array([[[1,2,2],[2,3,3],[3,4,4]],[[5,6,6],[6,7,7],[7,8,8]]])

print(array_2d.ndim)
print(array_3d.ndim) 

# dtype
import numpy as np
array=np.array([2,2,34,3,3.55])
print(array.dtype)

# dtype conversion
import numpy as np  
array= np.array([2, 2, 3.34, 3.44, 3.55])
con_array=array.astype(int)  # Convert to integer type
print(con_array)