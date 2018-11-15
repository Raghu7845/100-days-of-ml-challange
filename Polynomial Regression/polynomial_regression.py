
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


plt.scatter(X, y, color = 'black')
plt.plot(X, lin_reg.predict(X), color = 'blue',label = 'linear regression')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'red',label = 'poly')
plt.legend(loc='upper right')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.save('poly vs linear')
plt.show()


print lin_reg.predict(10)
print lin_reg_2.predict(poly_reg.fit_transform(10))
dataset['Salary'][9]