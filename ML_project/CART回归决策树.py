import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


x=np.array(list(range(1,11))).reshape(-1,1)
y=np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.0,9.05])

model1=LinearRegression()
model2=DecisionTreeRegressor(max_depth=1)
model3=DecisionTreeRegressor(max_depth=3)
model4=DecisionTreeRegressor(max_depth=10)

model1.fit(x,y)
model2.fit(x,y)
model3.fit(x,y)
model4.fit(x,y)

x_test=np.arange(0.0,10.0,0.1).reshape(-1,1)
y_predict1=model1.predict(x_test)
y_predict2=model2.predict(x_test)
y_predict3=model3.predict(x_test)
y_predict4=model4.predict(x_test)

plt.figure(figsize=(10,5))
plt.scatter(x,y,c='gray',label='data')
plt.plot(x_test,y_predict1,color='r',label='liner')
plt.plot(x_test,y_predict2,color='b',label='max_depth=1')
plt.plot(x_test,y_predict3,color='g',label='max_depth=3')
plt.plot(x_test,y_predict4,color='y',label='max_depth=10')

plt.legend()
plt.xlabel('data')
plt.ylabel('target')
plt.show()
