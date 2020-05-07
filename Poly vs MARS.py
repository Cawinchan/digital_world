from sklearn.datasets import load_boston
import operator
import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import RadiusNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from pyearth import Earth
import statsmodels.api as sm




X,y = load_boston(return_X_y=True)

# % lower status of the population
lstat_x = []
[lstat_x.append(row[12]) for row in X]

#average number of rooms per dwelling
rm_x = []
[rm_x.append(row[5]) for row in X]

rsq_dic = {}

lstat_x = np.array(lstat_x).reshape(-1,1)
print(lstat_x.shape)
y = y.reshape(-1,1)
print(y.shape)


lr = LinearRegression()
lr.fit(lstat_x,y)
print("linear equation",lr.coef_,lr.intercept_)
y_lr_pred = lr.predict(lstat_x)
print("r^2 of lr",lr.score(lstat_x,y))
print("mse of lr",mean_squared_error(y,y_lr_pred))

plt.scatter(lstat_x,y,s=10)
plt.plot(lstat_x,y_lr_pred, color='red')

poly = PolynomialFeatures(degree=2)
lstat_x_transformed = poly.fit_transform(lstat_x)

poly = LinearRegression()
poly.fit(lstat_x_transformed,y)
print("poly equation",poly.coef_,poly.intercept_)
y_poly_pred = poly.predict(lstat_x_transformed)
print("r^2 of poly",poly.score(lstat_x_transformed,y))
print("mse of poly",mean_squared_error(y,y_poly_pred))

#REALLY IMPT to sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(lstat_x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)

plt.plot(x,y_poly_pred, color='green')


mars = Earth()
mars.fit(lstat_x,y,)
print("mars equation",mars.coef_)
y_mars_pred = mars.predict(lstat_x)
print("r^2 of mars",r2_score(y,y_mars_pred))
print("mse of mars",mean_squared_error(y,y_mars_pred))

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(lstat_x,y_mars_pred), key=sort_axis)
x, y_mars = zip(*sorted_zip)
plt.plot(x,y_mars, color='orange')


# print(lstat_x.reshape(1,-1)[0].tolist())
# print(y.reshape(1,-1)[0].tolist())
lowess = sm.nonparametric.lowess(y.reshape(1,-1)[0].tolist(),lstat_x.reshape(1,-1)[0].tolist())

lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

plt.plot(lowess_x,lowess_y, color='black')
print("r^2 of lowess",r2_score(y,lowess_y))
print("mse of lowess",mean_squared_error(y,lowess_y))


loess_rg = sm.nonparametric.KernelReg(lstat_x,y,var_type='c')
print("r^2 of loess", loess_rg.r_squared())

neigh = RadiusNeighborsRegressor(weights='distance', algorithm='auto')
neigh.fit(lstat_x,y)
y_neigh_pred = neigh.predict(lstat_x)
print("r^2 of neigh",neigh.score(lstat_x,y))
print("mse of neigh",mean_squared_error(y,y_neigh_pred))

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(lstat_x,y_neigh_pred), key=sort_axis)
x, y_neigh_pred = zip(*sorted_zip)

# plt.plot(x,y_neigh_pred, color='blue')

# rndm_forest = RandomForestRegressor()
# rndm_forest.fit(lstat_x,y)
# y_rndm_forest_pred = rndm_forest.predict(lstat_x)
# print("r^2 of rndm_forest",rndm_forest.score(lstat_x,y))
# print("mse of rndm_forest",mean_squared_error(y,y_rndm_forest_pred))
#
# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(lstat_x,y_rndm_forest_pred), key=sort_axis)
# x, y_rndm_forest_pred = zip(*sorted_zip)
#
# plt.plot(x,y_rndm_forest_pred, color='blue')
plt.show()

def n_estimator_optimiser(x,y):
    for n in range(1,100):
        rndm_forest = RandomForestRegressor()
        rndm_forest.fit(lstat_x, y)