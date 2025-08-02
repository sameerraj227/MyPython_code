# have to create a new array as array is immutable
#axis=0 means row-wise operation 
#axis=1 means column-wise operation

'''
operations: Insert
2d array me ek element krne pe pura size ussi element se bhar jayega
'''
import numpy as np
array = np.array([[1, 2, 3,4, 5,6, 7, 8, 9]])
new_array=np.insert(array,2,10)
print(new_array)

import numpy as np
array=np.array([[1,2,3],[3,2,8 ],[4,5,6]])
new_array=np.insert(array,1,10,axis=0)
print(new_array) 

import numpy as np
array=np.array([[1,2,3],[3,2,8 ],[4,5,6]])
new_array=np.insert(array,1,[10,43,23],axis=1)
print(new_array) 


# append
import numpy as np
arr=np.array([1, 2, 3,4, 5,6, 7, 8, 9])
new_array=np.append(arr,10)
print(new_array)

# append 2d array
import numpy as np  
array=np.array([[1,2,3],[3,2,8 ],[4,5,6]])
new_array=np.append(array,[[10],[11],[12]],axis=1)  #adding column
print(new_array)


#conc
import numpy as np
arr1=np.array([1, 2, 3,4, 5,6])
arr2=np.array([7, 8, 9])
print(np.concatenate((arr1,arr2)))

#removing elements(array_name, index, axis)
import numpy as np
array=np.array([[1,2,3],[3,2,8 ],[4,5,6]])
new_array=np.delete(array,1,axis=1)  #removing column
print(new_array)

#split
import numpy as np
array=np.array([[1,2,3],[3,2,8 ],[4,5,6]])
new_array=np.split(array,3,axis=0)  #splitting into 3 parts column-wise
print(new_array)

