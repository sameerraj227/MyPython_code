import numpy as np
data = np.array([1, 2, np.inf, 4, -np.inf])
clear_arr=np.nan_to_num(data, posinf=100,neginf=-100)
print(np.isinf(data))