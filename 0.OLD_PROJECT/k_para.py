import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

wafer_size=150.0
shotsize=25.950, 32.950 #shot size 불러오기 or 숫자 넣기
Map_offset= 0.0, 16.475

fig, ax= plt.subplots(1,1,figsize=(6.5,6))
# plt.quvier(Wx,Wy,dx,dy)
# plt.scatter(shotsize,Map_offset)
circle1=plt.Circle((0,0), 150, color='black', fill=False)
ax.add_artist(circle1)
xshotp=int(divmod(wafer_size-Map_offset[0],shotsize[0])[0])
xshotm=-int(divmod(wafer_size+Map_offset[0],shotsize[0])[0])
yshotp=int(divmod(wafer_size-Map_offset[1],shotsize[1])[0])
yshotm=-int(divmod(wafer_size+Map_offset[1],shotsize[1])[0])

xs=abs(max(xshotp,xshotm))
ys=abs(max(yshotp,yshotm))

print(xshotp,xshotm,yshotp,yshotm)
y_line=Map_offset[1]+(+0.5)*shotsize[1]
x_to_edge=np.sqrt(wafer_size**2 - y_line**2)
temp=(divmod((xshotp)*shotsize[0]-x_to_edge,shotsize[0])[1])
print(temp)

for xn in range(xshotm-1,xshotp+1):
    x_line=Map_offset[0]+(xn+0.5)*shotsize[0]
    y_to_edge=np.sqrt(abs(wafer_size**2 - x_line**2))
    a,temp=divmod((ys+0.5)*32.950-y_to_edge,32.950)
    ax.vlines(x_line,-y_to_edge-temp,y_to_edge+temp,color='black',linestyles='dashed')

for yn in range(yshotm-1,yshotp+1):
    y_line=Map_offset[1]+(yn+0.5)*shotsize[1]
    x_to_edge=np.sqrt(abs(wafer_size**2 - y_line**2))
    # print((xshotp)*25.950-x_to_edge)
    a,temp=divmod((xs+0.5)*25.950-x_to_edge,25.950)
    ax.hlines(y_line,-x_to_edge-temp,x_to_edge+temp,color='black',linestyles='--')

# for xn in range(xshotm-2,xshotp+2):
#     x_line=Map_offset[0]+(xn+0.5)*shotsize[0]
#     ax.vlines(x_line,(yshotm-2+abs(xn))*shotsize[1],(yshotp+2-abs(xn))*shotsize[1],color='red',linestyles='dashed')



plt.show()