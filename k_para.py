import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

wafer_size=150.0
shotsize=25.950, 32.950 #shot size 불러오기 or 숫자 넣기
Map_offset= 0.0, 16.475

fig, ax= plt.subplot(1,1, figsize(6.5,6))
# plt.quvier(Wx,Wy,dx,dy)
circle1=plt.Circle((0,0), 150, color='black', fill=False)
ax.add_artist(circle1)
