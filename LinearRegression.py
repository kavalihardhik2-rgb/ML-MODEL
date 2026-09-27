import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([[3000],[4000],[5000],[6000],[7000]])

model = LinearRegression()
model.fit(x,y)

predicted=model.predict(x)

print("slope (coefficient):",model.coef_)
print("Intercept:",model.intercept_)

plt.scatter(x,y,color='blue',label='Actual data')
plt.plot(x,predicted,color='red',label='Predicted line')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.title('Linear Regression')
plt.legend()
plt.show()

new_value=[[6]]
prediction=model.predict(new_value)
print(prediction[0])
