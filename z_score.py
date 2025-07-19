import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset={1,22,2,3,4,34,45,53,65,44,74,43,5,25,64,56,5,100,107,117}

outlier=[]

def detect_outliers():
    mean=np.mean(dataset)
    threshold=3
    std=np.std(dataset)

    for i in dataset:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:
            outlier.append()
    return outlier

plt.hist(dataset)