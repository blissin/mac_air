import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
import sklearn

x = np.random.rand(20, 1)
y = 5 * x + 20
y_e=y+1*np.random.rand(20, 1) #오차가 포함된 y

# plt.scatter(x, y, marker = '+')
# print(x,'\n\n',y)

model=LinearRegression()
model.fit(x,y)
y_predict=model.predict(x)
relation_score = model.score(x,y_e) #R^2 상관관계 계수

print(relation_score)

# model.coef_ << 기울기 // model.intercept_ << 절편
plt.scatter(x,y)
plt.scatter(x,y_predict,marker='*')
plt.scatter(x,y_e,marker='+')

plt.show()