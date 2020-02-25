import numpy as np 
import pandas as pd 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error 



def beijing(n):
	'''
	n is the degree of polinomial features
	'''
	df = pd.read_csv("beijing_house_price.csv")
	#remove unuseable columns
	df.drop(labels = ['小区名字','商场','房型'], axis = 1)
	#clean data set
	df.dropna(inplace = True)
	df.drop_duplicates(inplace = True)
	#select top 3 features based on pearson correlation coefficients
	corr_coef = np.abs(df.corr(method = 'pearson').iloc[-1])
	corr_coef = corr_coef.sort_values(ascending = False)[1:4]
	features = df[corr_coef.index.values]
	target = df['每平米价格']

	#train test splits
	X_train, X_test, y_train, y_test = train_test_split(features, target, test_size =  0.3, random_state = 10)

	#create polynomial combinations of the fetures with n degree
	poly_features = PolynomialFeatures(degree = n, include_bias = False)
	poly_x_train = poly_features.fit_transform(X_train)
	poly_x_test = poly_features.fit_transform(X_test)

	#fit linear regression model
	lm = LinearRegression()
	lm.fit(poly_x_train, y_train)
	y_pred = lm.predict(poly_x_test)

	#calculate Mean absolute error
	mae = mean_absolute_error(y_test, y_pred)

	return mae

	
