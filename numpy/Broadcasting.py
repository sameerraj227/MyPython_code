#broadcasting is a powerful mechanism in NumPy that allows for operations on arrays of different shapes and sizes.
# It enables element-wise operations without the need for explicit replication of data.
import numpy as np
prices = np.array([100, 200, 300, 400, 500])
discount=10
final_prices = prices - (prices * discount / 100)
print(final_prices)  



# Broadcasting allows for operations between arrays of different shapes.
import numpy as np
prices = np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])
discount = np.array([[10], [20], [30]])
final_prices = prices - (prices * discount / 100)
print(final_prices)

import numpy as np
prices = np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])
discount=np.array([[10],[20],[30]])
res=prices+discount
print(res)