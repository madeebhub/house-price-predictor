import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import joblib
dataframe = pd.read_csv('data.csv')
print(dataframe.head())
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
# fig = px.histogram(data_frame=dataframe, x='bedrooms', nbins=50)
# fig.show()
# fig = px.histogram(dataframe , x="price" ,nbins=50)
# fig.show()

print(dataframe.price.corr(dataframe.bedrooms))
print(dataframe.price.corr(dataframe.bathrooms))
print(dataframe.price.corr(dataframe.sqft_living))
print(dataframe.price.corr(dataframe.sqft_above))
print(dataframe.price.corr(dataframe.sqft_basement))
print(dataframe.price.corr(dataframe.view))
print(dataframe.price.corr(dataframe.condition))
print(dataframe.price.corr(dataframe.yr_built))
print(dataframe.price.corr(dataframe.yr_renovated))
print(dataframe.price.corr(dataframe.floors))


# print(dataframe.price.corr(dataframe.street))
# print(dataframe.price.corr(dataframe.city))
# fig = px.histogram(data_frame=dataframe, x='sqft_living', nbins=50)
# fig.show()
# fig = px.scatter(data_frame=dataframe, x='sqft_living', y='price', color='bedrooms')
# fig.show()
# fig = px.scatter(data_frame=dataframe, x='sqft_above', y='price', color='bedrooms')
# fig.show()

dataframe['log_price'] = np.log(dataframe['price'])


def rmse(prediction , actual):
    return np.sqrt(np.mean((prediction - actual)**2))
input_featutres = ['bedrooms','bathrooms','sqft_living','sqft_above','sqft_basement','waterfront','view','condition','yr_built','yr_renovated']
inputs,target = dataframe[input_featutres],dataframe.price
x_train,x_test,y_train,y_test = train_test_split(inputs,target,test_size=0.2 ,random_state=42)
# print(x_test , 'lines are here and this is for test')
# print(dataframe , 'these numbers of rows these are complete dataframe')

model = LinearRegression()
model.fit(x_train,y_train)
# prediction = model.predict(x_test)
# print(prediction , 'here are all your predictions see')
# print(rmse(prediction,y_test), 'this is the error')
# print(dataframe.price > 2000000)
# print('for new house price are again is also what now', model.predict([[5,3,3000,2000,800,1,1,4,2002,0]]))

joblib.dump(model, 'house_price_predictor.joblib')
print("model saved successfully")





# print(dataframe.info())
