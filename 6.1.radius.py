from math import sqrt
from optparse import Values

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

import seaborn as sns

def RbfModel ():
    from scipy.interpolate import Rbf
    df=pd.read_csv("BIGCSV.csv")
    # df=df[(df.AggregationMethod=="RawSingleColorMeasurement")]
    # df=df[(df.MeasurementDirection=="X")]

    # df['WF_X']=(df['FiledPosition_X[nm]']+df['TargetPosition_X[nm]'])
    # df['WF_Y']=(df['FiledPosition_Y[nm]']+df['TargetPosition_Y[nm]'])
    # df2=df[['WF_X','WF_Y','StackSensitivity','Wavelength[nm]']]
    # df2=df2[df2['Wavelength[nm]']<500]
    df2=df
    
    ti=np.linspace(-150,150,100)
    XI,YI=np.meshgrid(ti,ti)

    rbf_adj = Rbf(df2['WF_X'],df2['WF_Y'],df2['StackSensitivity'],function='gaussian')
    SS=rbf_adj(XI,YI)
    # print(SS)

    r=np.sqrt(XI**2+YI**2)
    circle=r<150
    # print(XI,YI)
    # print(XI[circle],YI[circle])
    # print(r,circle)
    print(r.shape,circle.shape,XI.shape,YI.shape,SS.shape)
    print(XI[circle].shape)
    # plt.pcolor(XI[circle],YI[circle],SS[circle])
    # plt.pcolor(ti,ti,SS)
    plt.show()

#wafer map 만들기

RbfModel()

#%%

#220326 push by mac
