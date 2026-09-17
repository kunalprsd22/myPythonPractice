import numpy as np
import pandas as pd

array_1d = np.array([1,2,3,4,5,6,7])
array_2d = np.array([
                     [1,2,3],
                     [4,5,6],
                     [7,8,9]
                     ])
array_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])


result =  pd.DataFrame(array_2d)
print(result)



