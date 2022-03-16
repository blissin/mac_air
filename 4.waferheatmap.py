import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def flight_heatmap():
    plt.rcParams['figure.figsize']=[10,8]

    flights=sns.load_dataset('flights')
    # print(flights.head())

    df=flights.pivot('month','year','passengers')
    # print(df.head())
    # test

# test 2222

    plt.pcolor(df)
    plt.xticks(np.arange(0.5, len(df.columns),1), df.columns)
    plt.yticks(np.arange(0.5, len(df.index),1), df.index)
    plt.title('Heatmap',fontsize=14)
    plt.xlabel('year')
    plt.ylabel('month')
    plt.colorbar()
    plt.show()

def figure():
    data = np.array([[ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ],
        [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
        [ 1. ,  2. ,  0.1,  2. ,  2. ,  1. ],
        [ 1. ,  2. ,  2. ,  0.1,  2. ,  1. ],
        [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
        [ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ]])

    plt.figure(1)
    plt.imshow(data ,interpolation='none')
    plt.colorbar()
    plt.show()

flight_heatmap()