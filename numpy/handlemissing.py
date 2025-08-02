#nan - not a number use to represent missing values returns boolean array
import numpy as np
data = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(data))  # Returns boolean array indicating NaN positions


#nan_to_num- replace NaN with a specified number or default value-0
import numpy as np
data = np.array([1, 2, np.nan, 4, 5])
clear_arr=np.nan_to_num(data, nan=10)
print(clear_arr) 


#isinf- check for infinite values in an array
import numpy as np
data = np.array([1, 2, np.inf, 4, -np.inf])
clear_arr=np.nan_to_num(data, posinf=100,neginf=-100)
print(np.isinf(data))