from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(20, 1)
x=x*10
y = 5 * x + 2
y=y+3*np.random.rand(20,1)

model = LinearRegression()
model.fit(x,y)
y_p= model.predict(x)

print('기울기:',model.coef_,'절편 :', model.intercept_)

plt.scatter(x, y, marker = '+')
plt.scatter(x, y_p, marker = 'o')
# print(x, y)
plt.show()