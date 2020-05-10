from sklearn.datasets import load_boston
import operator
import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import RadiusNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from pyearth import Earth
import statsmodels.api as sm

# train = pd.read_csv('boston_data.csv')
# X = np.array(train.iloc[:, 0:13])
# y = np.array(train.iloc[:, 13])
#
# test = pd.read_csv('boston_test_data.csv')
# X_test = np.array(test.iloc[:, 0:13])
# X_test_id = test.iloc[:, 0]

np.random.seed(0)
m = 1000
n = 10
X = 80*np.random.uniform(size=(m,n)) - 40
y = np.abs(X[:,6] - 4.0) + 1*np.random.normal(size=m)

#Fit an Earth model
model = Earth()
model.fit(X,y)

#Print the model
print(model.trace())
print(model.summary())


X,y = load_boston(return_X_y=True)
model_rsq_dic = {}

# # % lower status of the population
lstat_x = []
[lstat_x.append(row[12]) for row in X]


lstat_x = np.array(lstat_x).reshape(-1,1)

#lstat_x = X
print(lstat_x.shape)
y = y.reshape(-1,1)
print(y.shape)


lr = LinearRegression()
lr.fit(lstat_x,y)
print("linear equation coef",lr.coef_," intercept ",lr.intercept_)
y_lr_pred = lr.predict(lstat_x)
print("r^2 of lr",lr.score(lstat_x,y))
print("mse of lr",mean_squared_error(y,y_lr_pred))

model_rsq_dic['lr'] = (lr.score(lstat_x,y),mean_squared_error(y,y_lr_pred))
plt.scatter(lstat_x,y,s=10)
plt.plot(lstat_x,y_lr_pred, color='red', label='Linear Regression - rsq: 0.544')

poly = PolynomialFeatures(degree=2)
lstat_x_transformed = poly.fit_transform(lstat_x)

poly = LinearRegression()
poly.fit(lstat_x_transformed,y)
print("poly equation",poly.coef_," intercept ",poly.intercept_)
y_poly_pred = poly.predict(lstat_x_transformed)
print("r^2 of poly",poly.score(lstat_x_transformed,y))
print("mse of poly",mean_squared_error(y,y_poly_pred))
model_rsq_dic['poly'] = (poly.score(lstat_x_transformed,y),mean_squared_error(y,y_poly_pred))


#REALLY IMPT to sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(lstat_x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)

plt.plot(x,y_poly_pred, color='green', label='Poly Regression - rsq: 0.641')


mars = Earth()
mars.fit(lstat_x,y,)
print("mars equation \n",mars.summary()," trace \n",mars.trace(),mars.basis_)
y_mars_pred = mars.predict(lstat_x)
print("r^2 of mars",r2_score(y,y_mars_pred))
print("mse of mars",mean_squared_error(y,y_mars_pred))
model_rsq_dic['mars'] = (r2_score(y,y_mars_pred),mean_squared_error(y,y_mars_pred))

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(lstat_x,y_mars_pred), key=sort_axis)
x, y_mars = zip(*sorted_zip)
plt.plot(x,y_mars, color='black', label='MARS Regression - rsq: 0.687')
plt.legend()
plt.title('Regression Comparision Graph')
plt.ylabel("LSTAT - % lower status of the population")
plt.xlabel("MEDV - Median value of owner-occupied homes in $1000's")
plt.show()


# print(lstat_x.reshape(1,-1)[0].tolist())
# print(y.reshape(1,-1)[0].tolist())
#lowess = sm.nonparametric.lowess(y.reshape(1,-1)[0].tolist(),lstat_x.reshape(1,-1)[0].tolist())


# lowess_x = list(zip(*lowess))[0]
# lowess_y = list(zip(*lowess))[1]
#
# # plt.plot(lowess_x,lowess_y, color='black')
# print("r^2 of lowess",r2_score(y,lowess_y))
# print("mse of lowess",mean_squared_error(y,lowess_y))


# loess_rg = sm.nonparametric.KernelReg(lstat_x,y,var_type='c')
# print("r^2 of loess", loess_rg.r_squared())

# neigh = RadiusNeighborsRegressor(weights='distance', algorithm='auto')
# neigh.fit(lstat_x,y)
# y_neigh_pred = neigh.predict(lstat_x)
# print("r^2 of neigh",neigh.score(lstat_x,y))
# print("mse of neigh",mean_squared_error(y,y_neigh_pred))
# model_rsq_dic['neigh'] = (neigh.score(lstat_x,y),mean_squared_error(y,y_neigh_pred))
#

# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(lstat_x,y_neigh_pred), key=sort_axis)
# x, y_neigh_pred = zip(*sorted_zip)

# plt.plot(x,y_neigh_pred, color='blue')

rndm_forest = RandomForestRegressor(n_estimators=60,random_state=0)
rndm_forest.fit(lstat_x,y)
y_rndm_forest_pred = rndm_forest.predict(lstat_x)
# print(y_rndm_forest_pred.shape)
# #How to create a dataframe from array to submission file
# prediction = pd.DataFrame({'id':np.array(range(0,102)),'price':y_rndm_forest_pred}).to_csv('Boston_housing.csv',index=False)
# print(prediction)



# print("r^2 of rndm_forest",rndm_forest.score(lstat_x,y))
# print("mse of rndm_forest",mean_squared_error(y,y_rndm_forest_pred))
# model_rsq_dic['rndm_forest'] = (rndm_forest.score(lstat_x,y),mean_squared_error(y,y_rndm_forest_pred))

# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(lstat_x,y_rndm_forest_pred), key=sort_axis)
# x, y_rndm_forest_pred = zip(*sorted_zip)

# plt.plot(x,y_rndm_forest_pred, color='blue')
# plt.show()

gbr = GradientBoostingRegressor(random_state=0)
gbr.fit(lstat_x,y)
y_gbr_pred = gbr.predict(lstat_x)
print("r^2 of gbr",gbr.score(lstat_x,y))
print("mse of gbr",mean_squared_error(y,y_gbr_pred))
model_rsq_dic['gbr'] = (gbr.score(lstat_x,y),mean_squared_error(y,y_gbr_pred))

# sort_axis = operator.itemgetter(0)
# sorted_zip = sorted(zip(lstat_x,y_gbr_pred), key=sort_axis)
# x, y_gbr_pred = zip(*sorted_zip)
#
# plt.plot(x,y_gbr_pred, color='blue')
# plt.show()


def n_estimator_optimiser(x,y):
    r_score = {}
    for n in range(1,100):
        #plt.scatter(x, y, s=10)
        rndm_forest = RandomForestRegressor(n_estimators=n,random_state=0)
        rndm_forest.fit(x, y)
        y_rndm_forest_pred = rndm_forest.predict(x)
        rsq = rndm_forest.score(x, y)
        r_score[n] = rsq
        sort_axis = operator.itemgetter(0)
        sorted_zip = sorted(zip(lstat_x,y_rndm_forest_pred), key=sort_axis)
        x, y_rndm_forest_pred = zip(*sorted_zip)
        #plt.plot(x, y_rndm_forest_pred, color=str(n/100))
        #plt.show()
        print(str(n)+' done fitting r_score = '+ str(rsq))
    print(max(r_score,key=r_score.get))
    plt.scatter(r_score.keys(),r_score.values())
    plt.show()

print(model_rsq_dic)
print(max(model_rsq_dic,key=model_rsq_dic.get))

